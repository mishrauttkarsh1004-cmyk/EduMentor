from agents.pedagogy_agent import PedagogyAgent
from agents.content_agent import ContentAgent
from agents.evaluation_agent import EvaluationAgent
from agents.student_model import StudentModel
import uuid
import time

class Orchestrator:
    def __init__(self):
        self.pedagogy = PedagogyAgent()
        self.content = ContentAgent()
        self.evaluator = EvaluationAgent()
        # in-memory student store (for demo). Replace with DB in production.
        self.students = {}

    def register_student(self, student_id, name, grade):
        profile = StudentModel(student_id=student_id, name=name, grade=grade)
        self.students[student_id] = profile
        return profile.to_dict()

    def create_personalized_lesson(self, student_id, topic, difficulty="medium"):
        student = self.students.get(student_id)
        if not student:
            raise ValueError("student not found")
        plan = self.pedagogy.design_learning_path(student, topic, difficulty)
        lesson = self.content.generate_lesson(plan)
        # attach metadata
        lesson_id = str(uuid.uuid4())
        lesson['lesson_id'] = lesson_id
        lesson['created_at'] = time.time()
        # save to student history
        student.save_lesson(lesson)
        return lesson

    def evaluate_and_update(self, student_id, lesson_id, answer_text):
        student = self.students.get(student_id)
        if not student:
            raise ValueError("student not found")
        # find lesson
        lesson = student.get_lesson(lesson_id)
        if not lesson:
            raise ValueError("lesson not found")
        eval_result = self.evaluator.assess_answer(lesson, answer_text, student)
        # update student model
        student.update_with_evaluation(lesson_id, eval_result)
        return eval_result

    def get_student_profile(self, student_id):
        student = self.students.get(student_id)
        if not student:
            return {"error":"student not found"}
        return student.to_dict()
