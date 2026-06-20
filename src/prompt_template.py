def build_rag_prompt(
    question,
    context
):
    return f"""
You are a document question-answering assistant.

Rules:
1. Answer only using the provided document context.
2. Do not use outside knowledge.
3. If the context does not contain enough information,
   respond with:

   The available document context is insufficient
   to answer this question.

4. Keep answers concise and clear.
5. Base all statements on the retrieved context.

Document Context:
{context}

Question:
{question}

Answer:
""".strip()