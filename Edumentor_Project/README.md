# EduMentor — Capstone Project
A multi-agent AI architecture for personalized STEM tutoring using LLM-powered pedagogy, content generation, and learning evaluation.

## Contents
- `backend/` — FastAPI backend implementing agents and APIs.
- `agents/` — core agent classes (PedagogyAgent, ContentAgent, EvaluationAgent, StudentModel, Orchestrator).
- `adapters/` — LLM adapter for OpenAI (placeholder — add API key and runtime).
- `frontend/` — minimal static frontend (HTML + JS) to demo the system.
- `data/` — sample student profiles and lessons.
- `scripts/` — helper scripts to run and demo.

## Quick start (local)
1. Create a Python venv and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r backend/requirements.txt
   ```
2. Set your OpenAI API key as environment variable `OPENAI_API_KEY` if you plan to enable LLM calls (adapter uses `openai`).
3. Run the backend:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```
4. Open `frontend/index.html` in a browser and use the demo UI (it will call `http://localhost:8000`).

## Notes
- The included OpenAI adapter is a placeholder. The project will run in demo mode without a real API key, using deterministic stub responses. To enable real LLM responses, install `openai` and provide `OPENAI_API_KEY`.
- This scaffold is intentionally concise to be easy to run and extend. Use it as the starting point for your capstone: add richer pedagogy rules, agent orchestration policies, and more sophisticated student modeling and evaluation.
