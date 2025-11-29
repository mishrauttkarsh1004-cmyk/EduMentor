from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.orchestrator import Orchestrator
from pydantic import BaseModel

app = FastAPI(title="EduMentor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

orch = Orchestrator()

class StudentCreate(BaseModel):
    student_id: str
    name: str
    grade: int

class LessonRequest(BaseModel):
    student_id: str
    topic: str
    difficulty: str = "medium"

class AnswerSubmission(BaseModel):
    student_id: str
    lesson_id: str
    answer: str

@app.post("/register_student")
async def register_student(s: StudentCreate):
    orch.register_student(s.student_id, s.name, s.grade)
    return {"status":"ok"}

@app.post("/generate_lesson")
async def generate_lesson(req: LessonRequest):
    lesson = orch.create_personalized_lesson(req.student_id, req.topic, req.difficulty)
    return lesson

@app.post("/submit_answer")
async def submit_answer(sub: AnswerSubmission):
    feedback = orch.evaluate_and_update(sub.student_id, sub.lesson_id, sub.answer)
    return feedback

@app.get("/student_progress/{student_id}")
async def student_progress(student_id: str):
    return orch.get_student_profile(student_id)
