# AI Ethics Research Assistant (RAG)

A Retrieval-Augmented Generation (RAG) system that answers **AI ethics research questions** using academic papers and citations.

The system retrieves relevant document chunks from a **FAISS vector database** and generates answers using **Llama 3.1 via Groq**, citing the original sources.

---

# Project Overview

This project builds a research assistant that can:

- Retrieve relevant academic text using **vector similarity search**
- Answer questions using **LLM reasoning**
- Cite the **original papers used for the answer**
- Evaluate retrieval quality using **Precision@k**

The goal is to create a **trustworthy AI assistant for AI ethics research**.

---

# System Architecture

Pipeline:

```
User Question
      ↓
Query Embedding
      ↓
FAISS Vector Search
      ↓
Top Document Chunks
      ↓
Prompt Construction
      ↓
Groq Llama 3.1
      ↓
Answer + Citations
```

---

# Project Structure

```
ai-ethics-research-assistant-RAG
│
├── ingestion/
│   └── load_papers.py
│
├── embedding/
│   └── build_index.py
│
├── retrieval/
│   ├── retrieve.py
│   ├── vector_store.py
│   └── test_retrieval.py
│
├── generation/
│   └── answer_questions.py
│
├── evaluation/
│   └── evaluate_retrieval.py
│
├── faiss_index/      (ignored in git)
│
├── requirements.txt
└── README.md
```

---

# Dataset Processing

Document ingestion results:

- Loaded **190 pages** of AI ethics papers
- Created **1429 chunks initially**
- Later expanded to **2098 chunks**

Example chunk metadata:

```
{
 'source_id': '01',
 'title': 'The Ethics of AI Surveillance and Data Privacy',
 'author': 'MaryEllen O’Connell',
 'year': 2025,
 'domain': 'surveillance',
 'type': 'journal'
}
```

Metadata allows filtering by:

- research domain
- publication type
- author
- year

---

# Vector Database

Embedding model used:

```
sentence-transformers/all-MiniLM-L6-v2
```

Each document chunk is converted into a **384-dimensional vector embedding**.

Vector storage:

```
FAISS
```

FAISS enables **fast semantic similarity search** across document chunks.

---

# Retrieval Example

Query:

```
What are ethical risks of AI surveillance?
```

Retrieved documents:

1. **Kakembo Aisha Annet (2025)**  
   *The Ethics of AI: Philosophical Perspectives*

2. **Dorotic & Stagno (2022)**  
   *AI in Public: Technology Bias and Surveillance*

3. **MaryEllen O’Connell (2025)**  
   *The Ethics of AI Surveillance and Data Privacy*

---

# Retrieval Evaluation

Retrieval performance was evaluated using **Precision@5**.

Test queries included:

- AI surveillance ethics
- healthcare bias
- generative AI risks
- philosophical concerns of AI
- AI policy frameworks

Result:

```
Precision@5: 0.72
```

Meaning **72% of retrieved documents belong to the correct domain**.

---

# Example Output

Question:

```
What are ethical risks of AI surveillance?
```

Answer:

```
AI surveillance introduces ethical risks including violations of privacy,
loss of autonomy, and potential algorithmic bias. These systems may
also lead to unintended societal consequences when deployed in public
monitoring scenarios.
```

Sources:

- Kakembo Aisha Annet (2025) — *The Ethics of AI: Philosophical Perspectives*
- Dorotic & Stagno (2022) — *AI in Public: Technology Bias and Surveillance*
- MaryEllen O’Connell (2025) — *The Ethics of AI Surveillance and Data Privacy*

---

# Technologies Used

Core stack:

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Groq (Llama 3.1)
- Streamlit *(planned UI)*

---

# How to Run

Clone the repository:

```
git clone https://github.com/aarushiarora18/ai-ethics-research-assistant-RAG.git
cd ai-ethics-research-assistant-RAG
```

Install dependencies:

```
pip install -r requirements.txt
```

Build the vector index:

```
python -m embedding.build_index
```

Run the research assistant:

```
python -m generation.answer_questions
```

---

# Future Improvements

Planned upgrades:

- Streamlit web interface
- Query rewriting for improved retrieval
- Reranking using cross-encoders
- Hybrid search (BM25 + vector search)
- Interactive paper viewer
- Conversational research assistant

---

# Author

**Aarushi Arora**

Project: *AI Ethics Research Assistant (RAG)*
