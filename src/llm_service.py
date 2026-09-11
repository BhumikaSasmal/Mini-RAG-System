import os
from google import genai
from src.prompt_template import build_rag_prompt

class LLMService:
    def __init__(self, mode=None):
        self.mode = (mode or os.getenv("LLM_MODE", "mock")).lower()

        if self.mode == "gemini":
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("Missing GEMINI_API_KEY environment variable.")
            self.client = genai.Client(api_key=api_key)
            self.model = os.getenv("LLM_MODEL_NAME", "gemini-3.6-flash")
        elif self.mode == "mock":
            self.client = None
        else:
            raise ValueError(
                f"Unsupported LLM_MODE: '{self.mode}'. "
                "Supported modes are 'mock' and 'gemini'."
            )

    def generate_answer(self, question, context):
        if not context.strip():
            return "The available document context is insufficient to answer this question."

        prompt = build_rag_prompt(question, context)

        if self.mode == "mock":
            return self._mock_answer(context)
        elif self.mode == "gemini":
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=prompt,
                )
                return response.text.strip()
            except Exception as e:
                return f"Error communicating with LLM Provider: {str(e)}"

    def _mock_answer(self, context):
        sentences = context.split(". ")
        answer = ". ".join(sentences[:2])
        if answer and not answer.endswith("."):
            answer += "."
        return answer
