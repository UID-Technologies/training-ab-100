# Day 2 AB100 Practice-First Mini-Project

**Python + Azure AI Foundry | Standalone Lab (no Day 1 dependency)**

Azure AI Foundry supports model access through Foundry project/model endpoints. This lab uses `azure-ai-inference` with `ChatCompletionsClient` for direct chat completion against deployed models.

---

# Day 2 Project

## Project Name

```text
enterprise-agentic-ai-day2
```

## Business Scenario

A global manufacturing enterprise wants a **Supplier Onboarding Agent** that can process new vendor applications and provide:

```text
1. Automated onboarding workflow execution
2. External API due diligence (credit, sanctions, ERP)
3. Policy-grounded compliance decisions (RAG)
4. Human approval for high-risk suppliers
5. Operational observability for audit and SRE teams
```

Each Day 2 topic is demonstrated as one runnable module.

---

# Topic-to-Mini-Project Mapping

| Topic | Mini Project | What Participants Learn |
| ----- | ------------ | ----------------------- |
| Workflow Automation | Supplier Onboarding Workflow Engine | State transitions, orchestration, audit history |
| Tool Calling & APIs | Due Diligence Agent with Enterprise APIs | Function schemas, tool loops, API evidence capture |
| RAG Architecture | Policy-Grounded Compliance Agent | Chunking, retrieval, citations, grounded answers |
| Human-in-the-Loop Workflows | Approval Gate Workflow | Risk thresholds, approval queue, accountable decisions |
| AI Observability | Trace, Cost, and Metrics Report | Execution trace, token cost, operational telemetry |

---

# Final Folder Structure

```text
enterprise-agentic-ai-day2/
│
├── .env
├── requirements.txt
├── README.md
│
├── data/
│   ├── procurement_policy.txt
│   ├── anti_bribery_policy.txt
│   ├── supplier_data_classification.txt
│   └── onboarding_sla.txt
│
├── prompts/
│   ├── workflow_orchestrator.txt
│   ├── due_diligence_agent.txt
│   ├── compliance_rag_agent.txt
│   ├── human_reviewer.txt
│   └── observability_agent.txt
│
├── src/
│   ├── config.py
│   ├── foundry_client.py
│   ├── cost_tracker.py
│   ├── trace_logger.py
│   ├── document_loader.py
│   ├── simple_retriever.py
│   ├── context_builder.py
│   ├── workflow_engine.py
│   ├── enterprise_tools.py
│   ├── approval_store.py
│   └── observability_report.py
│
├── modules/
│   ├── 01_workflow_automation.py
│   ├── 02_tool_calling_apis.py
│   ├── 03_rag_architecture.py
│   ├── 04_human_in_the_loop.py
│   └── 05_ai_observability.py
│
└── reports/
    ├── execution_trace.csv
    ├── cost_report.csv
    └── observability_metrics.csv
```

---

# Step 1: Create Project

```bash
mkdir enterprise-agentic-ai-day2
cd enterprise-agentic-ai-day2

python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

# Step 2: Install Packages

## `requirements.txt`

```txt
azure-ai-inference
azure-core
python-dotenv
pandas
scikit-learn
```

Install:

```bash
pip install -r requirements.txt
```

---

# Step 3: Azure Foundry Configuration

## `.env`

```env
AZURE_AI_ENDPOINT=https://<your-resource>.services.ai.azure.com/models
AZURE_AI_KEY=<your-key>

PRIMARY_MODEL=gpt-4o-mini
REASONING_MODEL=gpt-4o
FAST_MODEL=gpt-4o-mini

RISK_APPROVAL_THRESHOLD=65
```

Deploy at least one chat model in Azure AI Foundry (recommended: `gpt-4o-mini`).

---

# Step 4: Shared Source Code

## `src/config.py`

Central configuration for Foundry endpoint, model names, and human approval threshold.

## `src/foundry_client.py`

- `ask_ai()` for standard chat completions
- `ask_ai_with_tools()` for tool-calling loops against enterprise APIs

## `src/cost_tracker.py`

Logs token usage and estimated model cost to `reports/cost_report.csv`.

## `src/trace_logger.py`

Logs workflow and tool events to `reports/execution_trace.csv` and metrics to `reports/observability_metrics.csv`.

## `src/document_loader.py`

Loads enterprise policy files from `data/`.

## `src/simple_retriever.py`

Chunking + TF-IDF retrieval for RAG (training-friendly; production typically uses vector DB + embeddings).

## `src/context_builder.py`

Builds structured enterprise prompt context (role, task, constraints, examples, retrieved docs).

## `src/workflow_engine.py`

Deterministic supplier onboarding state machine.

## `src/enterprise_tools.py`

Mock enterprise APIs and tool schemas:
- Credit bureau API
- Sanctions screening API
- ERP registration API
- Risk score calculator

## `src/approval_store.py`

SQLite-backed approval queue for human-in-the-loop decisions.

## `src/observability_report.py`

Aggregates trace and metric files into an architect-friendly report.

---

# Step 5: Data Files

Policy corpus in `data/`:

- `procurement_policy.txt` — onboarding rules and auto-approval criteria
- `anti_bribery_policy.txt` — third-party risk and human accountability
- `supplier_data_classification.txt` — confidential data handling and residency
- `onboarding_sla.txt` — workflow stages and SLA targets

---

# Step 6: Prompt Files

- `workflow_orchestrator.txt` — workflow coordination guidance
- `due_diligence_agent.txt` — tool-using due diligence agent
- `compliance_rag_agent.txt` — policy-grounded compliance reviewer
- `human_reviewer.txt` — accountable procurement approver
- `observability_agent.txt` — telemetry interpretation for architects

---

# Mini Project 1: Workflow Automation

## Purpose

Demonstrate deterministic workflow orchestration before LLM autonomy is applied.

An agentic system in enterprise must separate:

```text
Known business process (workflow engine)
from
Model reasoning (policy interpretation and recommendations)
```

## Business Use Case

Procurement operations need a repeatable onboarding pipeline with auditable state transitions.

## Run File

From project root:

```bash
# Windows PowerShell
$env:PYTHONPATH="."
python modules/01_workflow_automation.py
```

## Expected Output

- Supplier metadata
- Workflow state history
- Stage artifacts (KYC status, policy scope, preliminary risk)

---

# Mini Project 2: Tool Calling & APIs

## Purpose

Demonstrate how agents call external enterprise APIs through controlled tool schemas.

## Real Enterprise Lesson

Tool calling must be:

```text
Schema-defined
Allow-listed
Auditable
Evidence-backed
```

## Business Use Case

Due diligence requires credit checks, sanctions screening, and ERP registration.

## Run File

```bash
$env:PYTHONPATH="."
python modules/02_tool_calling_apis.py
```

## Expected Behavior

1. Model calls `check_credit_score`
2. Model calls `screen_sanctions_list`
3. Model calls `calculate_risk_score`
4. Model returns recommendation with tool evidence

---

# Mini Project 3: RAG Architecture

## Purpose

Demonstrate retrieval-augmented generation for compliance decisions.

RAG is not just search + prompt. Architects must design:

```text
Chunking strategy
Retrieval quality
Citation-backed answers
Fallback behavior when confidence is low
```

## Business Use Case

Compliance decisions must be grounded in procurement, anti-bribery, and data classification policies.

## Run File

```bash
$env:PYTHONPATH="."
python modules/03_rag_architecture.py
```

## Expected Output

- Retrieved chunk IDs and scores
- Grounded compliance recommendation with policy basis

---

# Mini Project 4: Human-in-the-Loop Workflows

## Purpose

Demonstrate accountable human approval for high-risk agent recommendations.

## Real Enterprise Lesson

High-impact decisions require:

```text
Risk threshold
Approval queue
Human rationale
Audit trail
```

## Business Use Case

High spend + elevated risk score suppliers cannot be auto-approved.

## Run File

```bash
$env:PYTHONPATH="."
python modules/04_human_in_the_loop.py
```

## Expected Output

- Full workflow history
- Human reviewer decision (high-risk path)
- Final status: APPROVED / REJECTED / AUTO_APPROVED

---

# Mini Project 5: AI Observability

## Purpose

Demonstrate operational visibility for agentic systems.

## Real Enterprise Lesson

Before production rollout, teams need:

```text
Step success/failure rates
Tool call volume and errors
Token usage and cost
Traceability for audits
```

## Business Use Case

Platform and procurement leaders need evidence that the onboarding agent is reliable and governable.

## Run File

```bash
# Run after modules 01-04
$env:PYTHONPATH="."
python modules/05_ai_observability.py
```

## Expected Output

- Observability summary report
- Recent trace events
- AI interpretation of telemetry signals

---

# Execution Order for Classroom Demo

```bash
$env:PYTHONPATH="."
python modules/01_workflow_automation.py
python modules/02_tool_calling_apis.py
python modules/03_rag_architecture.py
python modules/04_human_in_the_loop.py
python modules/05_ai_observability.py
```

---

# How to Explain to Participants

## 1. Workflow Automation

Explain:

```text
Enterprise agents must follow governed process stages.
Workflow engines provide predictability, SLAs, and audit history.
AI reasoning should operate inside bounded workflow stages.
```

Real example:

```text
Supplier onboarding moves from Intake -> Due Diligence -> Policy Check -> Risk Scoring.
```

---

## 2. Tool Calling & APIs

Explain:

```text
Agents act on systems through tools, not free-form text.
Each tool has schema, purpose, and trace evidence.
Architects control which tools the agent can invoke.
```

Real example:

```text
Before approving a supplier, call credit and sanctions APIs and store the evidence.
```

---

## 3. RAG Architecture

Explain:

```text
Compliance answers must be grounded in enterprise policy documents.
RAG combines retrieval and generation with citations.
Better retrieval quality produces safer enterprise decisions.
```

Real example:

```text
Can we auto-approve this supplier and where can we store their bank details?
Answer must cite procurement and data classification policy.
```

---

## 4. Human-in-the-Loop Workflows

Explain:

```text
Not every decision should be fully automated.
High-risk cases escalate to human approvers with full AI summary.
Human decision and rationale must be auditable.
```

Real example:

```text
Risk score 72 and spend USD 750k -> route to Regional Procurement Manager.
```

---

## 5. AI Observability

Explain:

```text
Agent systems are production workloads and need SRE-grade visibility.
Trace logs support audit; metrics support reliability and cost control.
Design observability before scaling agent workloads.
```

Real example:

```text
Track tool call failures, model latency, and estimated token cost per onboarding case.
```

---

# Recommended Day 2 Flow

| Time | Activity |
| ---- | -------- |
| 30 min | Workflow automation concepts |
| 45 min | Mini Project 1 |
| 45 min | Tool calling and APIs |
| 60 min | Mini Project 2 |
| 30 min | RAG architecture concepts |
| 45 min | Mini Project 3 |
| 45 min | Human-in-the-loop design |
| 60 min | Mini Project 4 |
| 30 min | AI observability patterns |
| 45 min | Mini Project 5 + AB-100 scenario Q&A |

---

# AB-100 Architect Discussion (Final 30 Minutes)

Ask participants to design production upgrades for:

1. Replace TF-IDF with Azure AI Search + embeddings
2. Persist workflow state in Durable Functions or Cosmos DB
3. Route approvals to Teams or ServiceNow
4. Export telemetry to Application Insights and Foundry eval
5. Define SLOs: onboarding completion time, approval accuracy, tool failure rate

---

# Final Trainer Message

By the end of Day 2, participants will have built a standalone enterprise-style agentic workflow system with:

```text
Workflow automation
Tool/API integration
RAG-based compliance grounding
Human approval gates
Execution trace
Cost tracking
Operational observability
```

This completes the practice path from Day 1 agent foundations to Day 2 production-oriented agent architecture patterns required for AB-100 solution design discussions.

---

# Troubleshooting

| Issue | Fix |
| ----- | --- |
| `ModuleNotFoundError: No module named 'src'` | Run from project root with `$env:PYTHONPATH="."` |
| Authentication error | Verify `.env` endpoint and key from Foundry project |
| Model not found | Set `PRIMARY_MODEL` to your deployed model name |
| Empty observability report | Run modules 01–04 before module 05 |
