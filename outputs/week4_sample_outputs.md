# Sample RAG Outputs

---

## Example 1

### Question
What are the roles and responsibilities?

### Generated Answer
Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority.

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |

---

## Example 2

### Question
What is this document about?

### Generated Answer
SAMPLE POLICY DOCUMENT Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_report.pdf | 1 | sample_report.pdf_p1_c0 |
| sample_report.pdf | 1 | sample_report.pdf_p1_c1 |
| sample_policy.txt | N/A | sample_policy.txt_c0 |

---

## Example 3

### Question
How should policies be maintained?

### Generated Answer
are necessary to keep a sample policy relevant over time. As organizations evolve and external conditions change, policies must be updated to reflect new requirements, technologies, or regulations.

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |

---

## Example 4

### Question
What is Artemis II?

### Generated Answer
The available document context is insufficient to answer this question.

### Retrieved Sources

No relevant sources were returned.

---

## Example 5

### Question
What are the review and update requirements?

### Generated Answer
carry out their tasks in alignment with the policy's objectives. Clear implementation guidelines enhance usability and make the policy practical rather than purely theoretical.

### Retrieved Sources

| Source File | Page | Chunk ID |
|-------------|------|----------|
| sample_policy.txt | N/A | sample_policy.txt_c2 |
| sample_report.pdf | 2 | sample_report.pdf_p2_c3 |
| sample_policy.txt | N/A | sample_policy.txt_c3 |

---

# Summary

The RAG system successfully demonstrated:

- Retrieval from TXT documents
- Retrieval from PDF documents
- Semantic retrieval using alternate wording
- Source attribution through metadata
- Handling of insufficient document context
- Retrieval across multiple indexed documents
- Grounded answers based on retrieved chunks
