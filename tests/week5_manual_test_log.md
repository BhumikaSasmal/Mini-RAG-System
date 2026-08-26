# Manual Test Log Week 5

---

## NOTE

In mock mode, no LLM inference is performed. The response is an
extractive answer formed from the first retrieved context sentences
and is intended only for testing the RAG pipeline.

Rather than generating a response from the prompt, this method
returns the first one or two sentences from the retrieved context.
This provides a deterministic, extractive answer and should not be
interpreted as true LLM reasoning.

The prompt in `prompt_template.py` is unused in mock mode. The prompt
is designed to be consistent with the production LLM workflow.

In mock mode, it is intentionally ignored because the response is
generated directly from the retrieved context.

Mock mode does not send a prompt to an LLM.

All outputs have been generated using mock mode. The answer quality may
be limited due to the usage of mock mode and chunk boundaries.

---

| Test Scenario | Question | Expected Result | Actual Result | Status | Remarks | Retrieved Sources |
|---------------|----------|-----------------|---------------|--------|---------|-------------------|
| TXT Answer Generation | What is a sample policy? | The system should retrieve relevant chunks from the TXT document and generate an answer grounded in the retrieved context. | Returns the policy introduction extracted from the TXT document. | Pass | Answer is extraction-based because mock mode is active. | `sample_policy.txt (N/A, c0)`, `sample_policy.txt (N/A, c3)`, `sample_policy.txt (N/A, c1)` |
| PDF Answer Generation | What is the document about? | The system should retrieve relevant chunks from the PDF document and generate an answer grounded in the retrieved context. | Returns the policy introduction extracted from the PDF document. | Pass | PDF page metadata and chunk IDs match the returned source information. | `sample_report.pdf (Page 1, p1_c0)`, `sample_report.pdf (Page 1, p1_c1)`, `sample_report.pdf (Page 2, p2_c3)` |
| Insufficient Context | Who wrote Harry Potter? | The system should detect that no sufficiently relevant document context is available and return an insufficient-context response without displaying relevant sources. | Displays: **"The available document context is insufficient to answer this question."** | Pass | No relevant chunks passed the relevance threshold. | No relevant sources. |
| Source Display | What are roles and responsibilities? | The system should display formatted source metadata for the chunks used to generate the answer, including source file, page number, and chunk ID. | Returns the relevant "Roles and Responsibilities" section with associated source references. | Pass | Source page metadata matches the corresponding chunk IDs. | `sample_report.pdf (Page 2, p2_c3)`, `sample_policy.txt (N/A, c2)`, `sample_report.pdf (Page 1, p1_c0)` |
| Retrieved Context Preview | What are the review and update requirements? | The system should retrieve relevant policy chunks and make the retrieved context available separately for expanded review or debugging. | Returns the relevant policy section. Retrieved chunks are available in the **Retrieved Context** expandable section. | Pass | Retrieved context can be reviewed separately from the answer and source list. | `sample_policy.txt (N/A, c2)`, `sample_report.pdf (Page 2, p2_c3)`, `sample_policy.txt (N/A, c3)` |
| Duplicate Indexing | What are the review and update requirements? | Re-indexing the same document should not create duplicate chunks. The system should report that no new chunks were added while preserving existing indexed content. | Displays: **"No new chunks were added. This document appears to have already been indexed."** Existing indexed content is still retrieved successfully. | Pass | Duplicate chunk IDs are intentionally skipped during indexing. | `sample_policy.txt (N/A, c2)`, `sample_report.pdf (Page 2, p2_c3)`, `sample_policy.txt (N/A, c3)` |
| Multiple Documents | What is the file about? | The system should search across all indexed documents and return the most relevant chunks regardless of which indexed file they originate from. | Retrieves the most relevant content across multiple indexed documents. | Pass | Sources confirm retrieval from both the PDF and TXT documents. | `sample_report.pdf (Page 1, p1_c0)`, `sample_policy.txt (N/A, c0)` |
| Mock Mode Clarity | What is the file about? | The application should clearly indicate when mock mode is active and explain that answers are extraction-based rather than full LLM reasoning or synthesis. | Returns an extraction-based answer and displays: **"Mock Mode: Answers are extraction-based and do not use full LLM reasoning."** | Pass | Mock mode behavior is documented and visibly communicated in the application. | `sample_report.pdf (Page 1, p1_c0)`, `sample_policy.txt (N/A, c0)` |

# Summary

The RAG system successfully demonstrated:

- Retrieval from TXT documents
- Retrieval from PDF documents
- Source attribution through metadata
- Handling of insufficient document context
- Handling duplicate indexing
- Retrieval across multiple indexed documents
- Grounded answers based on retrieved chunks
- Mock mode behavior is clearly communicated
- Retrieved context and context used for the answer can be checked separately for expanded review
