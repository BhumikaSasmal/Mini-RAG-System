# Week 3 Manual Test Log

## Upload and Chunking Tests

| Test Case | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Upload TXT File | sample_policy.txt | File uploads successfully and chunks are generated | TXT processed successfully | Pass |
| TXT Page Handling | sample_policy.txt | Page count should display as N/A | Page count displayed as N/A | Pass |
| TXT Chunk Preview | sample_policy.txt | Chunk preview should not show page labels | Preview displayed correctly | Pass |
| Upload PDF File | sample_report.pdf | PDF pages extracted individually | PDF processed page-wise | Pass |
| PDF Metadata | sample_report.pdf | Chunks should contain page metadata | Page metadata displayed correctly | Pass |
| Upload Scanned PDF | sample_scanned.pdf | Extraction expected to fail without OCR | No readable text extracted | Out of Scope |

---

## Vector Index Tests

| Test Case | Expected Result | Actual Result | Status |
|---|---|---|---|
| Build Vector Index | Chunks embedded and stored in ChromaDB | Index built successfully | Pass |
| Rebuild Index | Existing collection replaced successfully | Rebuild completed correctly | Pass |
| Metadata Storage | Metadata saved with embeddings | Metadata retrieved successfully | Pass |

---

## Semantic Retrieval Tests

| Query | Expected Topic/Section | Actual Result | Status |
|---|---|---|---|
| What is the purpose of a sample policy? | Introduction/Purpose section | Retrieved partially relevant chunk | Partial Pass |
| Why is communication important? | Communication section | Relevant section retrieved | Pass |
| What are the key terms defined in the policy? | Definitions section | Retrieved nearby content | Partial Pass |
| What are the review requirements? | Review/update section | Retrieved related chunk | Partial Pass |
| Summarize the document | General overview | Broad but weak retrieval quality | Needs Improvement |

---

## Current Limitations

| Limitation | Notes |
|---|---|
| Retrieval quality is still improving | Semantic ranking is basic |
| System retrieves chunks only | No summarization or QA layer yet |
| Scanned PDFs unsupported | OCR not implemented |
| Chunk consistency varies | Depends on PDF formatting quality |

---

## OCR Note

Scanned PDFs require OCR support and are currently outside the active Week 3 scope.

---

