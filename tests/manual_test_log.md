# Manual Test Log

## Test Summary

| Test Case | Input File | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Upload TXT File | sample_policy.txt | TXT file processed successfully with page count shown as N/A | Chunks generated successfully and page count displayed as N/A | Pass |
| TXT Chunk Preview | sample_policy.txt | Chunk preview displayed without page labels | Expandable chunk preview displayed correctly | Pass |
| Upload PDF File | sample_report.pdf | PDF processed page-wise with correct page numbers | Chunks generated with correct page metadata | Pass |
| PDF Chunk Preview | sample_report.pdf | Chunk preview should display page numbers | Page numbers displayed correctly in preview | Pass |
| Upload Scanned PDF | sample_scanned.pdf | Text extraction should fail because OCR is not implemented | No readable text extracted from scanned PDF | Out of Scope |
| Build Vector Index | sample_policy.txt | Chunks embedded and indexed successfully | Vector index created successfully | Pass |
| Semantic Search | sample_policy.txt | Relevant chunks retrieved for query | Relevant chunks retrieved but ranking quality still basic | Partial Pass |

---

## Semantic Retrieval Test Cases

| Query | Expected Match | Actual Result | Status |
|---|---|---|---|
| What is the purpose of a sample policy? | Purpose/introduction section | Retrieved partially relevant section | Partial Pass |
| Why is communication important in a policy? | Communication-related section | Relevant chunk retrieved | Pass |
| What are the review and update requirements? | Review/update section | Retrieved nearby but not exact section | Partial Pass |

---

## Known Limitations

| Limitation | Notes |
|---|---|
| Retrieval quality is still basic | Results are sometimes only partially relevant |
| Messy PDFs create inconsistent chunks | Extraction works but chunk quality varies |
| Scanned PDFs are unsupported | OCR is not implemented yet |
| Initial model loading is slow | First embedding load takes time |

---

## OCR Note

Scanned PDFs are currently out of scope unless OCR support is added later.

---


