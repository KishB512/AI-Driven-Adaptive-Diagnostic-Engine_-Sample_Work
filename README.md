# AI-Driven Adaptive Diagnostic Engine

## Overview

This project implements a **1-Dimension Adaptive Testing Prototype** designed to evaluate a student's proficiency by dynamically adjusting question difficulty based on previous answers.

Instead of presenting questions randomly, the system updates the student's estimated ability after every response and selects the next question accordingly.

Additionally, the system integrates an **LLM (Groq API)** to generate a **personalized learning plan** based on the student's weak topics and performance.

This prototype demonstrates how **adaptive algorithms, modern APIs, and AI tools** can be combined to build intelligent educational systems.

---

# Tech Stack

Backend Framework  
- FastAPI

Programming Language  
- Python

Database  
- MongoDB

AI Integration  
- Groq API (LLM for learning plan generation)

Other Tools  
- Uvicorn (ASGI server)

---

# Project Structure

adaptive-quiz-engine/

│

├── main.py  
FastAPI application entry point and API endpoints

├── database.py  
MongoDB connection and database configuration

├── seed_questions.py  
Script used to populate MongoDB with GRE-style questions

├── adaptive_logic.py  
Core adaptive testing algorithm

├── ai_insights.py  
Generates personalized learning plans using Groq API

├── adaptive-test.ipynb  
Notebook used for testing and experimenting with adaptive logic

│

├── requirements.txt  
Project dependencies

---

# MongoDB Data Model

The system uses two main collections.

## Questions Collection

Stores GRE-style questions with difficulty and topic metadata.

Example structure:

```json
{
  "question": "Solve: 5x = 45",
  "options": {
    "A": "7",
    "B": "8",
    "C": "9",
    "D": "10"
  },
  "correctAnswer": "C",
  "difficulty": 0.4,
  "topic": "Algebra",
  "tags": ["linear equation"]
}
```

Fields

question → Question text  
options → Multiple choice answers  
correctAnswer → Correct option  
difficulty → Value between **0.1 and 1.0**  
topic → Subject area (Algebra, Vocabulary, Arithmetic)  
tags → Additional metadata

---

## UserSession Collection

Tracks the student's quiz progress.

Example structure

```json
{
  "session_id": "abc123",
  "ability_score": 0.5,
  "answers": [],
  "questions_answered": 0
}
```

Fields

session_id → Unique identifier for a quiz session  
ability_score → Current estimated ability level  
answers → List of answers submitted by the user  
questions_answered → Total questions attempted

---

# How to Run the Project

## 1 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2 Start MongoDB

Make sure MongoDB is running locally.

```
mongodb://localhost:27017
```

---

## 3 Seed the Question Database

Populate MongoDB with GRE-style questions.

```bash
python seed_questions.py
```

---

## 4 Set Environment Variables

Create a `.env` file and add your Groq API key.

```
GROQ_API_KEY=your_api_key_here
```

---

## 5 Start the FastAPI Server

```bash
uvicorn main:app --reload
```

---

## 6 Open API Documentation

FastAPI automatically provides interactive documentation.

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## GET /next-question

Returns the next question based on the student's current ability level.

Example Response

```json
{
  "question_id": "12345",
  "question": "What is the square root of 144?",
  "options": {
    "A": "10",
    "B": "11",
    "C": "12",
    "D": "13"
  },
  "topic": "Arithmetic"
}
```

---

## POST /submit-answer

Submits an answer for a question.

Request

```json
{
  "question_id": "12345",
  "selected_option": "C"
}
```

Response

```json
{
  "correct": true,
  "topic": "Arithmetic"
}
```

---

## GET /learning-plan/{session_id}

Returns weak topics and generates a personalized learning plan.

Example Response

```json
{
  "weak_topics": {
    "Algebra": 4,
    "Arithmetic": 3
  },
  "learning_plan": "1. Review algebraic equations and solve at least 20 practice problems. 2. Strengthen arithmetic fundamentals like fractions and square roots. 3. Practice timed GRE-style quizzes to improve speed and accuracy."
}
```

---

# Adaptive Algorithm Logic

The adaptive testing engine estimates the student's ability dynamically.

Initial State

The student begins with a **baseline ability score of 0.5**.

Adaptive Process

1. A question is selected based on the student's current ability score.
2. The student submits an answer.
3. If the answer is correct:
   - The student's ability score increases.
   - A more difficult question is selected next.
4. If the answer is incorrect:
   - The ability score decreases.
   - An easier question is selected next.
5. This process continues for multiple questions.

Weak Topic Detection

All incorrect answers are analyzed to identify topics where the student made the most mistakes.

These topics are used to generate personalized study recommendations.

---

# AI Insights (Learning Plan)

After the quiz session ends, the system sends the student's performance data to the **Groq LLM API**.

The model analyzes

- weak topics
- question difficulty reached
- incorrect answers

Based on this data, it generates a **3-step personalized study plan** that helps the student improve in weaker areas.

---

# AI Log

AI tools were used during development to improve productivity and accelerate problem solving.

Tools Used

- ChatGPT
- GroqAPI

How AI helped

- Generated initial FastAPI boilerplate
- Assisted with MongoDB schema design
- Helped structure the adaptive algorithm
- Assisted in debugging API errors
- Helped generate prompts for the Groq LLM integration
- Assisted in writing project documentation

Challenges AI could not fully solve

- Some runtime errors required manual debugging
- MongoDB query logic needed manual adjustments
- Adaptive logic tuning required testing and refinement

AI significantly accelerated development but understanding system behavior and debugging issues required manual reasoning.

---

# Future Improvements

Possible improvements for future versions include

- Implement full **Item Response Theory (IRT)** for more accurate ability estimation
- Store long-term student performance history
- Add user authentication
- Introduce difficulty calibration using historical performance data
- Build a frontend dashboard for students

---

# Conclusion

This project demonstrates a prototype of an **AI-powered adaptive testing system** that dynamically evaluates student proficiency and provides personalized learning insights. The system combines adaptive algorithms, MongoDB data modeling, and LLM integration to deliver a smarter assessment experience.
