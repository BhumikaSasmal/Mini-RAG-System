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

| Test Scenario | Question | Status | Generated Answer / Result | Retrieved Sources |
|---------------|----------|--------|---------------------------|-------------------|
| TXT Answer Generation | What is a sample policy? | Pass | Returns the policy introduction extracted from the TXT document. | `sample_policy.txt (N/A, c0)`, `sample_policy.txt (N/A, c3)`, `sample_policy.txt (N/A, c1)` |
| PDF Answer Generation | What is the document about? | Pass | Returns the policy introduction extracted from the PDF document. | `sample_report.pdf (Page 1, p1_c0)`, `sample_report.pdf (Page 1, p1_c1)`, `sample_report.pdf (Page 2, p2_c3)` |
| Insufficient Context | Who wrote Harry Potter? | Pass | Displays: **"The available document context is insufficient to answer this question."** | No relevant sources. |
| Source Display | What are roles and responsibilities? | Pass | Returns the relevant "Roles and Responsibilities" section with associated source references. | `sample_report.pdf (Page 2, p2_c3)`, `sample_policy.txt (N/A, c2)`, `sample_report.pdf (Page 1, p1_c0)` |
| Retrieved Context Preview | What are the review and update requirements? | Pass | Returns the relevant policy section. Retrieved chunks are available in the **Retrieved Context** expandable section. | `sample_policy.txt (N/A, c2)`, `sample_report.pdf (Page 2, p2_c3)`, `sample_policy.txt (N/A, c3)` |
| Duplicate Indexing | What are the review and update requirements? | Pass | Displays: **"No new chunks were added. This document appears to have already been indexed."** Existing indexed content is still retrieved successfully. | `sample_policy.txt (N/A, c2)`, `sample_report.pdf (Page 2, p2_c3)`, `sample_policy.txt (N/A, c3)` |
| Multiple Documents | What is the file about? | Pass | Retrieves the most relevant content across multiple indexed documents. | `sample_report.pdf (Page 1, p1_c0)`, `sample_policy.txt (N/A, c0)` |
| Mock Mode Clarity | What is the file about? | Pass | Returns an extraction-based answer and displays: **"Mock Mode: Answers are extraction-based and do not use full LLM reasoning."** | `sample_report.pdf (Page 1, p1_c0)`, `sample_policy.txt (N/A, c0)` |

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
- Retrieved context and context used for the answer can be checked in an expandable section
