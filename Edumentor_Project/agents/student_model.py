import time

class StudentModel:
    def __init__(self, student_id: str, name: str, grade: int):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.lessons = []  # list of lessons with metadata
        self.knowledge = {}  # simple topic->proficiency

    def save_lesson(self, lesson: dict):
        # add lesson metadata
        record = dict(lesson)
        record['saved_at'] = time.time()
        self.lessons.append(record)

    def get_lesson(self, lesson_id: str):
        for l in self.lessons:
            if l.get('lesson_id') == lesson_id:
                return l
        return None

    def update_with_evaluation(self, lesson_id: str, eval_result: dict):
        # update knowledge score for the topic (naive)
        lesson = self.get_lesson(lesson_id)
        if not lesson:
            return
        topic = lesson.get('title', 'unknown').replace('Lesson: ','')
        old = self.knowledge.get(topic, 0.0)
        new = eval_result.get('score',0.0)
        # moving average update
        self.knowledge[topic] = (old + new) / 2 if old else new
        # append eval to lesson record
        lesson.setdefault('evaluations', []).append(eval_result)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grade": self.grade,
            "knowledge": self.knowledge,
            "lessons": self.lessons
        }
