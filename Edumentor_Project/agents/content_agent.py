from adapters.openai_adapter import OpenAIAdapter
from typing import Dict, Any

class ContentAgent:
    def __init__(self):
        # adapter will use real OpenAI if key set, otherwise stub
        self.adapter = OpenAIAdapter()

    def generate_lesson(self, plan: Dict[str,Any]) -> Dict[str,Any]:
        # Create a prompt from the plan and ask adapter to generate content
        prompt = f"""
Create a short lesson for grade {plan.get('grade')} on the topic: {plan.get('topic')}.
Objectives: {plan.get('objectives')}
Scaffolding: {plan.get('scaffolding')}
Include {plan.get('assessment').get('num_questions')} short-answer practice questions (with expected answers).
"""
        response = self.adapter.call_llm(prompt)
        # adapter returns structured dict in demo mode
        lesson = {"title": f"Lesson: {plan.get('topic')}", "content": response.get("text"), "questions": response.get("questions")}
        return lesson
