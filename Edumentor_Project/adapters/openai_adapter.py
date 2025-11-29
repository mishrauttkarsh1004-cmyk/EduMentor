import os
import time
try:
    import openai
    _HAS_OPENAI = True
except Exception:
    _HAS_OPENAI = False

class OpenAIAdapter:
    """
    Lightweight adapter for OpenAI. If OPENAI_API_KEY is present and openai is installed,
    it will call the API. Otherwise, it returns deterministic stub responses for demo.
    """
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if self.api_key and _HAS_OPENAI:
            openai.api_key = self.api_key

    def call_llm(self, prompt: str):
        # If API is available, make a real call (simple completion).
        if self.api_key and _HAS_OPENAI:
            try:
                resp = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=500, temperature=0.7)
                text = resp.choices[0].text.strip()
                # We return a simple structured object; production adapters should use robust parsing.
                return {"text": text, "questions": []}
            except Exception as e:
                return {"text": f"[LLM call failed: {e}]", "questions": []}
        # Demo stub: create simple lesson and questions
        stub_text = "This is a demo lesson content generated without OpenAI. Explain core ideas, show examples, and provide practice."
        stub_questions = [
            {"q": "What is the main idea?", "answer": "main idea"},
            {"q": "Give one example", "answer": "example"},
            {"q": "Solve a simple problem", "answer": "solution"}
        ]
        return {"text": stub_text, "questions": stub_questions}
