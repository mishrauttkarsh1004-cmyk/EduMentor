from adapters.openai_adapter import OpenAIAdapter

class EvaluationAgent:
    def __init__(self):
        self.adapter = OpenAIAdapter()

    def assess_answer(self, lesson, answer_text, student):
        """
        For demo we compare answer_text to expected answers and call LLM for natural-language feedback.
        """
        # simple heuristic: check keywords from lesson questions if available
        questions = lesson.get("questions", [])
        # if no questions, give neutral evaluation
        if not questions:
            return {"score": 0.0, "feedback": "No questions to assess."}
        # naive matching:
        correct = 0
        details = []
        for q in questions:
            expected = q.get("answer", "").lower()
            if expected and expected in answer_text.lower():
                correct += 1
                details.append({"question": q.get("q"), "result":"correct"})
            else:
                details.append({"question": q.get("q"), "result":"incorrect", "expected": expected})
        score = correct / max(len(questions),1)
        # generate LLM feedback (adapter will stub if no API key)
        prompt = f"Student answer: {answer_text}\nEvaluation details: {details}\nProvide friendly feedback and next steps."
        fb = self.adapter.call_llm(prompt)
        return {"score": score, "details": details, "feedback": fb.get("text")}
