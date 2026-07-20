# Week 4 Test Log

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

All following tests have been done in Mock Mode. The answer quality may be limited due to the usage of mock mode and chunk boundaries.
## Test 1: TXT Document Question

### Objective
Verify that a factual question can be answered from an indexed TXT document.

### Steps
1. Upload and index a TXT document.
2. Ask a question whose answer appears in the document.
3. Review answer and source information.

### Question
What is the document about?

### Status: 
Pass

### Result
-# SAMPLE POLICY DOCUMENT # # Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

### Observation
- Answer was generated successfully.
- Retrieved chunks contained the expected information.
- Source file was displayed correctly.
- Page value was displayed as N/A for the TXT document.
- Chunk ID was displayed.
- Answer was grounded in the retrieved context.

---

## Test 2: PDF Document Question

### Objective
Verify that a factual question can be answered from an indexed PDF document.

### Steps
1. Upload and index a PDF document.
2. Ask a question whose answer appears in the document.
3. Review answer and source information.

### Question
What are roles and responsibilities?

### Status: 
Pass


### Result
Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority.

### Observation
- Answer was generated successfully, but is slightly messy due to the chunking.
- Relevant PDF chunks were retrieved.
- Source file was displayed correctly.
- Page metadata was displayed correctly.
- Chunk ID was displayed.
- Retrieved context supported the generated answer.

---

## Test 3: Semantic Retrieval

### Objective
Verify that semantic retrieval works when question wording differs from document wording.

### Steps
1. Use an indexed document.
2. Ask a question using wording different from the document text.
3. Review retrieved chunks and answer.

### Question
What defines the scope of a policy?

### Status: 
Pass

### Result
-# SAMPLE POLICY DOCUMENT ## Introduction A sample policy serves as a foundational document that outlines the rules, principles, and expectations governing a particular organization, system, or activity. It is designed to provide clarity, ensure consistency in decision-making, and establish a framework within which individuals can operate effectively.

### Observation
- Since the Answer prints only the first few lines of the relevant chunk, it seems irrelevant at first glance. However, on checking the relevant chunk, the actual answer is found in the remainder text. 
- Relevant chunks were retrieved.
- Semantic search identified related content.
- Answer remained grounded in the retrieved context, but can be messy due to chunking.
- Sources matched the originating document.

---

## Test 4: Insufficient Context Handling

### Objective
Verify behavior when the answer is not present in indexed documents.

### Steps
1. Ask a question unrelated to any indexed document.
2. Review the generated response.

### Question
Who won the 2023 Cricket World Cup?

### Status: 
Pass


### Result
The available document context is insufficient to answer this question.

### Observation
- No relevant document context was available.
- System returned an insufficient-context response.
- No unsupported information was generated.
- Source display remained consistent.

---

## Test 5: Multiple Document Retrieval

### Objective
Verify retrieval behavior when multiple documents are indexed.

### Steps
1. Upload and index multiple documents. In this case, to verify if the exact document is being retrieved, the legacy/sample.txt file about neural networks was also added to the context along with the sample policy and sample report.
2. Ask a question specific to one document.
3. Review source information.

### Question
What are neural networks?

### Status: 
Pass


### Result
Neural networks are a fundamental concept in the field of artificial intelligence, inspired by the structure and functioning of the human brain. They consist of interconnected units called neurons that work together to process information and solve complex problems.

### Observation
- Source file identified the originating document.
- Retrieved chunks matched the expected source.
- Source metadata was displayed correctly.

---

## Test 6: Vector Store Persistence

### Objective
Verify that indexed documents remain searchable after restarting the application.

### Steps
1. Index one or more documents.
2. Close the Streamlit application.
3. Restart the application.
4. Ask a question about a previously indexed document.

### Question
What are the roles and responsibilities?

### Status: 
Pass


### Result
Roles and Responsibilities A sample policy often includes roles and responsibilities to clarify who is responsible for what. This section ensures that tasks are appropriately assigned and that there is no overlap or confusion regarding authority.

### Observation
- Previously indexed chunks remained available.
- Retrieval worked without rebuilding the index.
- Persistent Chroma storage functioned correctly.
- Previously indexed documents remained searchable.

---

## Test 7: Mock Mode

### Objective
Verify answer generation using mock mode.

### Status: 
Pass

### Observation
- All previous answers were generated without API credentials; we can say mock mode is working successfully.
- Sources were displayed correctly.
- Retrieved context was available for review.
- Full demonstration workflow functioned successfully.

---

## Test 8: LLM API Mode

### Objective
Verify answer generation using configured LLM credentials.

### Status: 
Not Executed


### Result
NOT EXECUTED

### Observation
- API credentials were not configured during testing.
- Mock mode was used for demonstration purposes.
- API mode has not been tested yet.




