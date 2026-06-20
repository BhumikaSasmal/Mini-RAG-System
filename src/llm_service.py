import os


class LLMService:

    def __init__(self):

        self.mode = os.getenv(
            "LLM_MODE",
            "mock"
        ).lower()

        self.api_key = os.getenv(
            "LLM_API_KEY"
        )

    def generate_answer(
        self,
        question,
        context
    ):

        if self.mode == "mock":

            return self._mock_answer(
                question,
                context
            )

        return self._api_answer(
            question,
            context
        )

    def _mock_answer(
        self,
        question,
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

    def _api_answer(
        self,
        question,
        context
    ):

        if not self.api_key:

            return (
                "LLM API configuration is missing. "
                "Please check environment settings."
            )

        try:


            return (
                "LLM API mode is configured, "
                "but no provider has been connected yet."
            )

        except Exception:

            return (
                "Unable to generate a response "
                "from the language model."
            )