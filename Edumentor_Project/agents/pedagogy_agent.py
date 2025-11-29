from typing import Dict, Any

class PedagogyAgent:
    """
    Implements simple pedagogical rules to convert a topic and student profile
    into a learning plan (learning objectives, scaffolding steps, assessment type).
    """
    def design_learning_path(self, student, topic: str, difficulty: str="medium") -> Dict[str,Any]:
        # Very simple rule-set for demo:
        grade = getattr(student, "grade", 6)
        objectives = [
            f"Understand core concepts of {topic}",
            f"Solve basic problems on {topic}"
        ]
        if difficulty == "hard":
            objectives.append(f"Apply {topic} to novel problems")
        scaffolding = [
            {"step":1, "type":"explain", "detail": f"Intro to {topic}"},
            {"step":2, "type":"example", "detail": f"Worked example of {topic}"},
            {"step":3, "type":"practice", "detail": f"Practice problems"}
        ]
        assessment = {"type":"short_answer", "num_questions":3}
        plan = {"topic":topic, "objectives":objectives, "scaffolding":scaffolding, "assessment":assessment, "grade":grade}
        return plan
