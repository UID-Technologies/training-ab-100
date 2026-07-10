# Copilot Studio Knowledge
**knowledge management is the heart of any enterprise AI solution**. Many people assume Copilot Studio "reads the entire document," but that's not how it works.

Below is how it actually works internally.

---

# Architecture

```text
                  SharePoint
                 Dataverse
                  Websites
                Uploaded Files
              Azure SQL (Connector)
              Salesforce
             ServiceNow
                    │
                    ▼
        Microsoft Indexing Service
                    │
                    ▼
      Document Processing Pipeline
                    │
        ┌───────────┴────────────┐
        │                        │
  Text Extraction           Metadata Extraction
        │                        │
        └───────────┬────────────┘
                    │
              Chunk Generation
                    │
            Vector Embeddings
                    │
            Microsoft Search Index
                    │
             Semantic Retrieval
                    │
              Top Relevant Chunks
                    │
                 GPT Model
                    │
                Final Response
```

Unlike Azure AI Foundry, Microsoft hides most of this pipeline from the developer. ([Microsoft Learn][1])

---

# Step 1 — How Knowledge is Stored

Copilot Studio **does not store the original documents inside the LLM**.

Instead it creates a searchable index.

For example:

```
HR Policy.pdf
```

contains

```
150 pages
```

Internally it becomes

```
Chunk 1

Chunk 2

Chunk 3

Chunk 4

....

Chunk 800
```

Each chunk receives

* vector embedding
* metadata
* document id
* source location
* permissions

The GPT model only sees the retrieved chunks, not the whole document. ([Microsoft][2])

---

# Step 2 — How Chunking Works

Microsoft doesn't publish the exact algorithm or chunk size.

Internally it performs automatic semantic chunking.

Example

Original document

```
Leave Policy

Section 1

Annual Leave

Employees receive 25 days...

Section 2

Medical Leave

Employees receive 15 days...
```

becomes something similar to

```
Chunk 1

Annual Leave
25 Days

-------------------

Chunk 2

Medical Leave
15 Days

-------------------

Chunk 3

Carry Forward Rules
```

Microsoft automatically determines

* chunk boundaries
* overlap
* embedding generation
* indexing

Developers **cannot configure**:

* Chunk size
* Chunk overlap
* Token count per chunk
* Splitting strategy
* Heading-aware chunking
* Semantic chunking algorithm

This is a major limitation compared to Azure AI Foundry, where you control all of these parameters. ([Microsoft][2])

---

# Step 3 — How Retrieval Works

Suppose the user asks:

```
How many annual leaves do I get?
```

Copilot Studio does **not** send the entire 500-page policy.

Instead it performs:

```
Question

↓

Embedding

↓

Similarity Search

↓

Top Matching Chunks

↓

GPT

↓

Answer
```

If only three chunks are relevant, GPT receives only those three chunks.

This makes responses much faster.

---

# Step 4 — How Knowledge is Updated

This depends on the source.

## Uploaded Files

```
Upload PDF

↓

Indexed

↓

Available
```

If you replace the PDF

```
Policy_v1.pdf

↓

Policy_v2.pdf
```

you normally need to remove the old file and upload the new one so it is re-indexed.

---

## SharePoint

This is much better.

```
SharePoint

↓

Modify Document

↓

Microsoft Graph

↓

Re-index

↓

Copilot Uses New Version
```

Synchronization is automatic, but **not immediate**. Microsoft documents that synchronization typically occurs every **4–6 hours** after ingestion completes for SharePoint-based knowledge. ([Microsoft Learn][1])

---

## Dataverse

Whenever records change

```
Dataverse

↓

Search Index

↓

Updated Retrieval
```

Updates are handled through Microsoft's indexing process.

---

# Does GPT Memorize My Data?

No.

Many people misunderstand this.

GPT never "learns"

```
Employee Salary

Invoice

Customer

Policies
```

Instead

```
Question

↓

Retrieve

↓

Ground

↓

Answer
```

Every request performs retrieval again.

Nothing is permanently learned from your documents.

---

# Maximum Knowledge Size

There isn't one simple number because it depends on the knowledge source.

## Uploaded Files

Microsoft states that uploaded files are effectively **unlimited** from a knowledge-source perspective, although storage quotas and supported file limits still apply. ([Microsoft Learn][1])

---

## SharePoint

Key documented limits include:

* Up to **25 SharePoint URLs** as knowledge sources in generative orchestration.
* Individual supported files up to **512 MB** (for supported formats such as PDF, DOCX, PPTX).
* SharePoint synchronization typically every **4–6 hours** after ingestion. ([Microsoft Learn][1])

---

## Websites

Generative orchestration

```
Maximum

25 websites
```

Classic orchestration

```
Maximum

4 websites
```

([Microsoft Learn][1])

---

## Dataverse

Microsoft documents **unlimited** Dataverse knowledge sources in generative orchestration (subject to service limits and licensing), while classic orchestration has lower limits. ([Microsoft Learn][1])

---

# Does Copilot Search Everything?

No.

Suppose you have

```
SharePoint

1000 PDFs
```

and the user asks

```
Show maternity leave.
```

The pipeline is closer to:

```
1000 PDFs

↓

Semantic Search

↓

Top Relevant Chunks

↓

GPT
```

GPT never receives all 1000 PDFs.

---

# What Happens if Documents Change?

Example

Version 1

```
Annual Leave

20 Days
```

Later

Version 2

```
Annual Leave

30 Days
```

After the knowledge source is re-indexed,

the agent starts retrieving

```
30 Days
```

No prompt changes are required.

---

# Why Large Documents Sometimes Give Poor Answers

Suppose

```
Employee Handbook

900 pages
```

User asks

```
Summarize the handbook.
```

The retrieval engine

```
Search

↓

Top Chunks

↓

GPT
```

Only selected chunks are sent to GPT.

This means Copilot Studio is excellent for **fact lookup**, but less effective for summarizing very large documents because it is retrieval-based rather than processing the entire document in one request. This behavior is also frequently reported by practitioners. ([Reddit][3])

---

# Can We Control Chunking?

No.

You cannot specify

```
Chunk Size = 512

Chunk Overlap = 50

Embedding Model

Top K

Similarity Threshold

Metadata Filter

Hybrid Search

Reranking
```

These are managed by Microsoft.

With Azure AI Foundry or Azure AI Search, you can configure these aspects yourself.

---

# Can We Customize Retrieval?

Only to a limited extent.

Copilot Studio allows you to:

* Add descriptions to knowledge sources to help generative orchestration choose relevant sources.
* Enable or disable enhanced search features.
* Configure authentication and permissions.
* Mark some sources as official (in supported scenarios). ([Microsoft Learn][1])

However, you cannot directly configure:

* Top-K retrieval count
* Similarity threshold
* Reranking model
* Embedding model
* Hybrid keyword/vector weighting
* Metadata filters
* Retrieval scoring

---

# Knowledge Source Limitations

| Limitation                   | Explanation                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| No custom chunking           | Microsoft controls document splitting.                       |
| No custom embedding model    | Uses Microsoft's managed embedding pipeline.                 |
| No Top-K configuration       | Number of retrieved chunks isn't user configurable.          |
| No reranking control         | Cannot plug in your own reranker.                            |
| No hybrid search tuning      | Cannot adjust keyword vs. semantic weighting.                |
| No metadata filtering        | Fine-grained retrieval filters aren't exposed.               |
| Limited visibility           | No access to chunk scores or retrieval diagnostics.          |
| Large document summarization | May miss content because only relevant chunks are retrieved. |
| Indexing delay               | SharePoint synchronization is not real time.                 |
| Minimal observability        | Limited insight into why a particular chunk was selected.    |

---

# Enterprise Recommendation

For **departmental copilots** (HR, IT help desk, Finance FAQs, Teams assistants, SharePoint search), Copilot Studio's managed knowledge pipeline is usually sufficient and dramatically reduces development effort.

For **large enterprise RAG systems** (legal research, healthcare, insurance, engineering manuals, procurement, multi-agent AI), many architects use a hybrid approach:

```text
Copilot Studio
      │
      ▼
Conversation Layer
      │
      ▼
Custom Action / Power Automate
      │
      ▼
Azure AI Foundry + Azure AI Search
      │
      ├── Custom Chunking
      ├── Hybrid Search
      ├── Metadata Filters
      ├── Reranking
      ├── Top-K Control
      ├── Evaluation
      └── Observability
```

This pattern combines Copilot Studio's rapid conversational experience with the advanced retrieval, governance, and tuning capabilities required for enterprise-scale AI applications.


