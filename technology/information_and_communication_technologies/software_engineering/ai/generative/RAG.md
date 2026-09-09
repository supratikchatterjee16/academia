# Retrieval Augmented Generation

**Retrieval-Augmented Generation (RAG)** is an architectural pattern that enhances large language models (LLMs) by grounding their responses in **external knowledge sources** retrieved at query time. Instead of relying solely on the model’s training data, RAG dynamically fetches relevant documents and conditions the model’s output on them.

## What RAG Is

RAG combines two components:

1. **Retriever**
   Searches a knowledge store to find relevant information.

2. **Generator (LLM)**
   Uses the retrieved context to produce accurate, grounded responses.

**Pipeline:**

```
User Query → Embed → Retrieve relevant docs → Augments prompt → LLM generates answer
```

This reduces hallucinations and enables domain-specific intelligence.

---

## What RAG Can Do

### Knowledge Grounding

* Answer questions using proprietary or real-time data
* Cite documents or sources

### Enterprise Search & QA

* Internal documentation assistants
* Policy & compliance lookup

### Domain-Specific Assistants

* Healthcare knowledge retrieval
* Legal document analysis
* Customer support automation

### Context Extension

* Overcomes LLM context window limits
* Enables long-document reasoning

### Personalization & Memory

* Retrieve user-specific knowledge
* Maintain conversational memory

---

## How RAG Works (Step-by-Step)

### Data Ingestion

Documents are collected and chunked.

### Embedding

Chunks are converted into vector embeddings using embedding models.

### Storage

Vectors stored in a vector database or index.

### Query Processing

User query → embedding → similarity search.

### Retrieval

Top-k relevant chunks returned.

### Augmented Prompt

Retrieved context inserted into prompt.

### Generation

LLM generates grounded answer.

---

## How to Use RAG (Implementation Workflow)

### Step 1: Prepare Data

* PDFs, HTML, Markdown, database records
* Chunk into ~200–1000 tokens

### Step 2: Generate Embeddings

Use embedding models (e.g., sentence transformers).

### Step 3: Store Vectors

Choose vector store (in-memory or persistent).

### Step 4: Build Retrieval Pipeline

Perform semantic similarity search.

### Step 5: Prompt Augmentation

Insert retrieved context into prompt template.

### Step 6: Generate Response

Call LLM with context.

---

## Frameworks & Tools for RAG

### RAG Orchestration Frameworks

* LangChain — modular pipelines & integrations
* LlamaIndex — optimized for document retrieval & indexing
* Haystack — production search & QA pipelines

---

## Vector Stores & Retrieval Backends

### In-Memory / Lightweight

* FAISS (fast similarity search)
* Chroma (local persistent option)

**Use when:** prototyping, local apps, small datasets.

---

### Persistent Vector Databases

#### Vector-native DBs

* Qdrant — high-performance semantic search
* Pinecone — managed cloud service
* Weaviate — hybrid search & graph features
* Milvus — scalable distributed vector search

#### Traditional DBs with Vector Support

* MongoDB (Atlas Vector Search)
* PostgreSQL + pgvector
* Elasticsearch (dense vectors)

**Use when:** production apps, large-scale data, durability required.

---

## Retrieval Techniques Used in RAG

* **Dense retrieval** (embedding similarity)
* **Hybrid search** (BM25 + vectors)
* **Re-ranking** with cross-encoders
* **Metadata filtering**
* **Chunk compression & summarization**

---

## When to Use RAG vs Fine-Tuning

| Use Case                  | RAG | Fine-tuning |
| ------------------------- | --- | ----------- |
| Frequently changing data  | ✅   | ❌           |
| Private documents         | ✅   | ❌           |
| Domain style adaptation   | ⚠️  | ✅           |
| Factual accuracy          | ✅   | ⚠️          |
| Low latency offline model | ❌   | ✅           |

Often both are combined.

---

## Common Challenges

* Poor chunking strategy
* Irrelevant retrieval results
* Context overload
* Embedding drift
* Latency from retrieval step

## Example

