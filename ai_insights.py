from groq import Groq
from database import questions_collection
from bson import ObjectId

client = Groq(api_key="grok-api here")


def analyze_performance(answers):

    weak_topics = {}

    for ans in answers:

        if not ans["correct"]:

            question = questions_collection.find_one(
                {"_id": ObjectId(ans["question_id"])}
            )

            if question:

                topic = question["topic"]

                weak_topics[topic] = weak_topics.get(topic, 0) + 1

    return weak_topics


def generate_learning_plan(weak_topics):

    prompt = f"""
You are a GRE tutor.

Weak topics:
{weak_topics}

Create a **simple 3 step study plan** for the student.

Rules:
- Only return the study plan
- No code
- No explanations
- Each step should be short

Example format:

Step 1: ...
Step 2: ...
Step 3: ...
"""

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    plan = chat.choices[0].message.content

    steps = [step.strip() for step in plan.split("\n") if step.strip()]

    return steps