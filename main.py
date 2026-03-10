from fastapi import FastAPI
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Literal

from database import sessions_collection, questions_collection
from adaptive_logic import update_ability
from ai_insights import analyze_performance, generate_learning_plan


# ----------------------------------
# FastAPI App Configuration
# ----------------------------------
app = FastAPI(
    title="Adaptive GRE Practice API",
    description="An adaptive GRE practice testing system using FastAPI, MongoDB, and AI-powered learning insights.",
    version="1.0"
)


# ----------------------------------
# Request Model (MCQ Answer)
# ----------------------------------
class AnswerRequest(BaseModel):

    session_id: str = Field(
        ...,
        description="Unique session ID generated when the test session starts",
        example="Enter_Your_Session_ID"
    )

    answer: Literal["A", "B", "C", "D"] = Field(
        ...,
        description="Selected option for the current question",
        example="Option_Choosen"
    )


# ----------------------------------
# Home Route
# ----------------------------------
@app.get("/", tags=["Home"])
def home():
    """
    Root endpoint showing API usage instructions
    """
    return {
        "message": "Adaptive GRE Practice API",
        "instructions": [
            "1. Start session → POST /start-session",
            "2. Get question → GET /next-question/{session_id}",
            "3. Submit answer → POST /submit-answer",
            "4. Test stops automatically after 20 questions",
            "5. Get AI learning plan → GET /learning-plan/{session_id}"
        ]
    }


# ----------------------------------
# Start New Session
# ----------------------------------
@app.post("/start-session", tags=["Session"])
def start_session():
    """
    Creates a new adaptive testing session
    """

    session = {
        "ability_score": 0.5,
        "answers": [],
        "current_question": None
    }

    result = sessions_collection.insert_one(session)

    return {
        "session_id": str(result.inserted_id),
        "ability_score": 0.5,
        "message": "Session started successfully"
    }


# ----------------------------------
# Get Next Adaptive Question
# ----------------------------------
@app.get("/next-question/{session_id}", tags=["Quiz"])
def next_question(session_id: str):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    if not session:
        return {"error": "Session not found"}

    # Stop after 20 questions
    if len(session["answers"]) >= 20:
        return {
            "message": "Test completed",
            "next_step": f"/learning-plan/{session_id}"
        }

    ability = session["ability_score"]

    # Already answered questions
    answered_ids = [ObjectId(a["question_id"]) for a in session["answers"]]

    # Fetch remaining questions
    questions = list(
        questions_collection.find({"_id": {"$nin": answered_ids}})
    )

    if not questions:
        return {"message": "No more questions available"}

    # Select question closest to ability score
    question = min(
        questions,
        key=lambda q: abs(q["difficulty"] - ability)
    )

    # Save question as current
    sessions_collection.update_one(
        {"_id": ObjectId(session_id)},
        {"$set": {"current_question": question["_id"]}}
    )

    return {
        "question": question["question"],
        "options": question["options"],
        "difficulty": question["difficulty"]
    }


# ----------------------------------
# Submit Answer
# ----------------------------------
@app.post("/submit-answer", tags=["Quiz"])
def submit_answer(data: AnswerRequest):

    session = sessions_collection.find_one({"_id": ObjectId(data.session_id)})

    if not session:
        return {"error": "Session not found"}

    question_id = session.get("current_question")

    if not question_id:
        return {"error": "No active question. Call /next-question first."}

    question = questions_collection.find_one({"_id": question_id})

    # Check if answer is correct
    correct = data.answer == question["correct_answer"]

    # Update ability score using IRT logic
    new_ability = update_ability(
        session["ability_score"],
        question["difficulty"],
        correct
    )

    # Store answer history
    sessions_collection.update_one(
        {"_id": ObjectId(data.session_id)},
        {
            "$set": {"ability_score": new_ability},
            "$push": {
                "answers": {
                    "question_id": str(question_id),
                    "answer": data.answer,
                    "correct": correct
                }
            }
        }
    )

    return {
        "correct": correct,
        "new_ability": round(new_ability, 3),
        "questions_answered": len(session["answers"]) + 1
    }


# ----------------------------------
# AI Learning Plan Endpoint
# ----------------------------------
@app.get("/learning-plan/{session_id}", tags=["AI Insights"])
def learning_plan(session_id: str):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    if not session:
        return {"error": "Session not found"}

    if len(session["answers"]) < 20:
        return {
            "message": "Complete all 20 questions first",
            "questions_completed": len(session["answers"])
        }

    weak_topics = analyze_performance(session["answers"])

    plan = generate_learning_plan(weak_topics)

    return {
        "weak_topics": weak_topics,
        "learning_plan": plan
    }