# Retrieval Tests

---
## NOTE

In mock mode, no LLM inference is performed. The response is an
extractive answer formed from the first retrieved context sentences
and is intended only for testing the RAG pipeline.

Rather than generating a response from the prompt, this method
returns the first one or two sentences from the retrieved context.
This provides a deterministic, extractive answer and should not be
interpreted as true LLM reasoning.

The prompt in prompt_template.py is unused in mock mode. The prompt is designed to be consistent with the production LLM workflow.
In mock mode, it is intentionally ignored because the response is generated directly from the retrieved context.

Mock mode does not send a prompt to an LLM.

All Outputs have been generated using mock mode. The answer quality may be limited due to the usage of mock mode and chunk boundaries.

--- 

## TXT answer generation

### Question
What is a sample policy?

### Generated Answer
#SAMPLE POLICY DOCUMENT ## Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

---

## PDF answer generation

### Question
What is the document about?

### Generated Answer
SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.


---

## Insufficient context

### Question
Who wrote Harry Potter?

### Generated Answer
The available document context is insufficient to answer this question.

---

## Source display

### Question
What are roles and responsibilities?

### Generated Answer
Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority.

---

## Retrieved context preview

### Question
What are the review and update requirements?

### Generated Answer
carry out their tasks in alignment with the policy’s objectives. Clear implementation guidelines enhance usability and make the policy practical rather than purely theoretical.

---

## Duplicate indexing

### Question
What are the review and update requirements?

### Generated Answer
NOTE: The following message appears -> No new chunks were added. This document appears to have already been indexed.

carry out their tasks in alignment with the policy’s objectives. Clear implementation guidelines enhance usability and make the policy practical rather than purely theoretical.

---

## Multiple documents

### Question
What is the file about?

### Generated Answer
SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

---

## Mock mode clarity

### Question
What is the file about?

### Generated Answer
SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

NOTE: The following message appears beneath retrieved answer -> "Mock Mode: Answers are extraction-based and do not use full LLM reasoning."


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
- Use of Mock Mode is clarified.
- Retrieved context can be checked in an expandable section.
