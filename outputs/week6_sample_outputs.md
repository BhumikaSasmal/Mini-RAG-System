# Week 6 Evaluation & Retrieval Sample Outputs

---

## NOTE

In LLM mode (Gemini), answers are dynamically synthesized from retrieved document chunks while maintaining strict grounding constraints to prevent hallucinations. In Mock mode, answers revert to raw sentence extractions for deterministic pipeline testing.

All outputs below reflect live LLM generation unless explicitly noted in Mock comparison runs.

---

## TXT Answer Generation

### Question

What is a sample policy?

### Generated Answer

A sample policy is a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It serves as a vital tool for guiding behavior, ensuring consistency, and maintaining order within an organization or system.

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

> #- SAMPLE POLICY DOCUMENT ## Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively...

**`sample_policy.txt_c3`**

> are necessary to keep a sample policy relevant over time. As organizations evolve and external conditions change, policies must be updated to reflect new requirements, technologies, or regulations. Regular reviews ensure that the policy remains effective and aligned with current needs...

**`sample_policy.txt_c1`**

> clear statement of its objective and scope. The objective explains why the policy exists, while the scope defines who and what it applies to. This section is crucial as it sets the context for the entire document and ensures that readers can quickly determine its relevance to their roles or responsibilities...

---

## PDF Answer Generation

### Question

What is the document about?

### Generated Answer

The document provides an overview of a sample policy, explaining its foundational role in outlining rules, principles, and expectations within an organization, system, or activity. It covers the primary purpose of a sample policy—such as standardizing processes and ensuring consistency—as well as its key components, including objective and scope, definition of key terms, implementation guidelines, and compliance and enforcement mechanisms.

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

> SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively...

**`sample_report.pdf_p1_c1` — Page 1**

> objective and scope. The objective explains why the policy exists, while the scope defines who and what it applies to. This section is crucial as it sets the context for the entire document and ensures that readers can quickly determine its relevance to their roles or responsibilities. Definition of Key Terms...

**`sample_report.pdf_p2_c3` — Page 2**

> Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority...

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

No chunks passed the relevance threshold. Therefore, no document context was used to generate the answer.

---

## Source Display & Traceability

### Question

What are roles and responsibilities?

### Generated Answer

In a sample policy, roles and responsibilities clarify who is responsible for what. This section ensures tasks are appropriately assigned, eliminates overlap or confusion regarding authority, contributes to smoother operations, and helps prevent conflicts within an organization.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 1 | sample_report.pdf_p1_c0 |

### Retrieved Context Preview

**`sample_report.pdf_p2_c3` — Page 2**

> Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority. Clearly defined roles contribute to smoother operations and help prevent conflicts within the organization...

**`sample_policy.txt_c2`**

> carry out their tasks in alignment with the policy’s objectives. Clear implementation guidelines enhance usability and make the policy practical rather than purely theoretical. ## Compliance and Enforcement Compliance and enforcement mechanisms are also essential elements of a sample policy. These mechanisms outline how adherence to the policy will be monitored...

**`sample_report.pdf_p1_c0` — Page 1**

> SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making...

---

## Multi-Document Synthesis

### Question

What are the review and update requirements?

### Generated Answer

Based on the provided document, policies must be updated to reflect new requirements, technologies, or regulations as organizations evolve and external conditions change. Regular reviews are required to keep the policy relevant over time and to ensure it remains effective and aligned with current needs.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |

### Retrieved Context Preview

**`sample_policy.txt_c2`**

> carry out their tasks in alignment with the policy’s objectives. Clear implementation guidelines enhance usability and make the policy practical rather than purely theoretical. ## Compliance and Enforcement Compliance and enforcement mechanisms are also essential elements of a sample policy...

**`sample_report.pdf_p2_c3` — Page 2**

> Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority. Review and Revision Procedures Review and revision procedures are necessary to keep a sample policy relevant over time...

**`sample_policy.txt_c3`**

> are necessary to keep a sample policy relevant over time. As organizations evolve and external conditions change, policies must be updated to reflect new requirements, technologies, or regulations. Regular reviews ensure that the policy remains effective and aligned with current needs...

---

## Duplicate Indexing Handling

### Question

What are the review and update requirements?

### Generated Answer

**Indexing Result:**

No new chunks were added. This document appears to have already been indexed.

**Retrieved Answer:**

Based on the provided document, policies must be updated to reflect new requirements, technologies, or regulations as organizations evolve and external conditions change. Regular reviews are required to keep the policy relevant over time and to ensure it remains effective and aligned with current needs.

### Status

Pass

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |

### Retrieved Context Preview

**`sample_policy.txt_c2`**

> carry out their tasks in alignment with the policy’s objectives. Clear implementation guidelines enhance usability and make the policy practical rather than purely theoretical...

**`sample_report.pdf_p2_c3` — Page 2**

> Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what...

**`sample_policy.txt_c3`**

> are necessary to keep a sample policy relevant over time. As organizations evolve and external conditions change, policies must be updated to reflect new requirements, technologies, or regulations...

---

## Mock Mode vs. LLM Mode Comparison

### Question

What is the document about?

### Generated Answer (Mock Mode)

SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

> **Note:** Mock Mode: Answers are extraction-based and do not use full LLM reasoning.

### Generated Answer (LLM Mode - Gemini)

The document provides an overview of a sample policy, explaining its foundational role in outlining rules, principles, and expectations within an organization, system, or activity. It covers the primary purpose of a sample policy—such as standardizing processes and ensuring consistency—as well as its key components, including objective and scope, definition of key terms, implementation guidelines, and compliance and enforcement mechanisms.

### Status

Pass

### Comparison Remarks

While both modes retrieved the exact same underlying context chunks (`sample_report.pdf_p1_c0`, `sample_policy.txt_c0`), Mock Mode strictly extracted raw initial sentences, whereas LLM Mode successfully synthesized context across multiple chunks into a natural, complete response.
