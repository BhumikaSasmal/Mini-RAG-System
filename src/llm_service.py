import os

from src.prompt_template import build_rag_prompt


class LLMService:

    def __init__(self):

        self.mode = os.getenv(
            "LLM_MODE",
            "mock"
        ).lower()

    def generate_answer(
        self,
        question,
        context
    ):

        prompt = build_rag_prompt(
            question,
            context
        )

        return self._mock_answer(
            prompt,
            context
        )

    def _mock_answer(
        self,
        prompt,
        context
    ):

        if not context.strip():

            return (
                "The available document context "
                "is insufficient to answer "
                "this question."
            )

        sentences = context.split(". ")

        answer = ". ".join(
            sentences[:2]
        )

        if answer and not answer.endswith("."):
            answer += "."

        return answer
