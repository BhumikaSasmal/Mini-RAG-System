# Retrieval Tests

---

## NOTE

In mock mode, no LLM inference is performed. The response is an
extractive answer formed from the first retrieved context sentences
and is intended only for testing the RAG pipeline.

Rather than generating a response from the prompt, this method returns
the first one or two sentences from the retrieved context. This provides
a deterministic, extractive answer and should not be interpreted as true
LLM reasoning.

The prompt in `prompt_template.py` is unused in mock mode. The prompt is
designed to be consistent with the production LLM workflow. In mock mode,
it is intentionally ignored because the response is generated directly
from the retrieved context.

Mock mode does not send a prompt to an LLM.

All outputs have been generated using mock mode. The answer quality may
be limited due to the usage of mock mode and chunk boundaries.

---

## TXT Answer Generation

### Question

What is a sample policy?

### Generated Answer

#SAMPLE POLICY DOCUMENT ## Introduction A sample policy serves as a
foundational document that outlines the rules, principles, and
expectations governing a particular organization, system, or activity.
It is designed to provide clarity, ensure consistency in decision-making,
and establish a framework within which individuals can operate
effectively.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c0 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c1 |

### Retrieved Context Preview

**`sample_policy.txt_c0`**

> # SAMPLE POLICY DOCUMENT ## Introduction A sample policy serves as a
> foundational document that outlines the rules, principles, and
> expectations governing a particular organization, system, or activity.
> It is designed to provide clarity, ensure consistency in decision-making,
> and establish a framework within which individuals can operate effectively...

**`sample_policy.txt_c3`**

> are necessary to keep a sample policy relevant over time. As organizations
> evolve and external conditions change, policies must be updated to reflect
> new requirements, technologies, or regulations. Regular reviews ensure
> that the policy remains effective and aligned with current needs...

**`sample_policy.txt_c1`**

> clear statement of its objective and scope. The objective explains why
> the policy exists, while the scope defines who and what it applies to.
> This section is crucial as it sets the context for the entire document
> and ensures that readers can quickly determine its relevance to their
> roles or responsibilities...

---

## PDF Answer Generation

### Question

What is the document about?

### Generated Answer

SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a
foundational document that outlines the rules, principles, and
expectations governing a particular organization, system, or activity.
It is designed to provide clarity, ensure consistency in decision-making,
and establish a framework within which individuals can operate
effectively.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 1 | sample_report.pdf_p1_c0 |
| sample_report.pdf | 1 | sample_report.pdf_p1_c1 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |

### Retrieved Context Preview

**`sample_report.pdf_p1_c0` — Page 1**

> SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a
> foundational document that outlines the rules, principles, and
> expectations governing a particular organization, system, or activity.
> It is designed to provide clarity, ensure consistency in decision-making,
> and establish a framework within which individuals can operate effectively...

**`sample_report.pdf_p1_c1` — Page 1**

> objective and scope. The objective explains why the policy exists, while
> the scope defines who and what it applies to. This section is crucial as
> it sets the context for the entire document and ensures that readers can
> quickly determine its relevance to their roles or responsibilities.
> Definition of Key Terms...

**`sample_report.pdf_p2_c3` — Page 2**

> Roles and Responsibilities A sample policy often includes roles and
> responsibilities to clarify who is responsible for what. This section
> ensures that tasks are appropriately assigned and that there is no overlap
> or confusion regarding authority...

---

## Insufficient Context

### Question

Who wrote Harry Potter?

### Generated Answer

The available document context is insufficient to answer this question.

### Status

Pass

### Retrieved Sources

No relevant sources.

### Retrieved Context Preview

No chunks passed the relevance threshold. Therefore, no document context
was used to generate the answer.

---

## Source Display

### Question

What are roles and responsibilities?

### Generated Answer

Roles and Responsibilities A sample policy often includes roles and
responsibilities to clarify who is responsible for what. This section
ensures that tasks are appropriately assigned and that there is no
overlap or confusion regarding authority.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 1 | sample_report.pdf_p1_c0 |

---

## Retrieved Context Preview

### Question

What are the review and update requirements?

### Generated Answer

carry out their tasks in alignment with the policy’s objectives. Clear
implementation guidelines enhance usability and make the policy practical
rather than purely theoretical.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |

Exact chunks can be checked using the Retrieved Context expandable
section.

---

## Duplicate Indexing

### Question

What are the review and update requirements?

### Generated Answer

NOTE: The following message appears:

**No new chunks were added. This document appears to have already been
indexed.**

carry out their tasks in alignment with the policy’s objectives. Clear
implementation guidelines enhance usability and make the policy practical
rather than purely theoretical.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |

Exact chunks can be checked using the Retrieved Context expandable
section.

---

## Multiple Documents

### Question

What is the file about?

### Generated Answer

SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a
foundational document that outlines the rules, principles, and
expectations governing a particular organization, system, or activity.
It is designed to provide clarity, ensure consistency in decision-making,
and establish a framework within which individuals can operate
effectively.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 1 | sample_report.pdf_p1_c0 |
| sample_policy.txt | N/A | sample_policy.txt_c0 |

---

## Mock Mode Clarity

### Question

What is the file about?

### Generated Answer

SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a
foundational document that outlines the rules, principles, and
expectations governing a particular organization, system, or activity.
It is designed to provide clarity, ensure consistency in decision-making,
and establish a framework within which individuals can operate
effectively.

**NOTE:** The following message appears beneath the retrieved answer:

> Mock Mode: Answers are extraction-based and do not use full LLM
> reasoning.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 1 | sample_report.pdf_p1_c0 |
| sample_policy.txt | N/A | sample_policy.txt_c0 |

---

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
- Representative TXT, PDF, and insufficient-context scenarios include
  retrieved-context previews for independent review
- Retrieved context and context used for the answer can be checked in
  an expandable section
