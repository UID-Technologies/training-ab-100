## Lab 05 - Azure Foundary vs Copilot Studio

## Simple Analogy

Think of building a house:

* **Azure AI Foundry** is like the **construction company**. It provides the foundation, tools, materials, and flexibility to build a custom house exactly the way you want.
* **Copilot Studio** is like **interior design software**. It helps you quickly create and customize rooms, furniture, and layouts without needing to build the structure from scratch.

So:

> **Azure AI Foundry = Build AI Solutions**
> **Copilot Studio = Build Business Agents**

---

# High-Level Comparison

| Feature           | Azure AI Foundry                             | Copilot Studio                                                         |
| ----------------- | -------------------------------------------- | ---------------------------------------------------------------------- |
| Primary Purpose   | Build custom AI applications                 | Build business agents and copilots                                     |
| Target Users      | Developers, AI Engineers, Architects         | Business Users, Power Platform Developers, Solution Architects         |
| Coding Required   | Yes (Python, C#, JavaScript, etc.)           | Low-code / No-code                                                     |
| Flexibility       | Very High                                    | Moderate                                                               |
| Model Choice      | Any supported Azure AI model                 | Uses configured generative AI capabilities, can integrate with Foundry |
| Agent Development | Full custom multi-agent systems              | Business workflow agents                                               |
| RAG               | Fully customizable                           | Built-in knowledge sources                                             |
| Memory            | Fully customizable                           | Conversation/session memory with platform capabilities                 |
| Deployment        | APIs, web apps, mobile apps, enterprise apps | Teams, Microsoft 365, websites, Power Platform                         |
| Best For          | Enterprise AI platforms                      | Business automation and copilots                                       |

---

# Architecture View

## Azure AI Foundry

```text
Users

↓

Custom Application

↓

AI Foundry

↓

Model Router

↓

GPT-4.1
Phi
Llama
Mistral

↓

Vector Database

↓

Custom Agents

↓

Enterprise APIs

↓

SQL
SAP
Dynamics
ServiceNow
```

Everything is programmable.

---

## Copilot Studio

```text
Employee

↓

Microsoft Teams

↓

Copilot Studio Agent

↓

Knowledge

↓

Topics

↓

Prompt Actions

↓

Power Automate

↓

SharePoint

↓

Dynamics

↓

Microsoft Graph
```

Everything is configuration-driven.

---

# Think Like an Enterprise Architect

Suppose your CEO says:

> "I want an AI assistant for employees."

Ask yourself:

Do we need to build a **custom AI platform**, or do we need a **business assistant**?

That answer determines the platform.

---

# Azure AI Foundry

Imagine building an AI-powered legal document review platform.

Requirements:

* Upload thousands of contracts
* Vector database
* Multiple AI agents
* Model routing
* Reasoning
* Cost optimization
* OCR
* Images
* Charts
* Human approval
* Evaluation
* Custom UI

Could Copilot Studio do all of this?

**Not effectively.**

Azure AI Foundry is designed for this level of customization.

---

# Copilot Studio

Imagine HR wants:

* Leave policy assistant
* Payroll questions
* Employee onboarding
* Microsoft Teams integration
* Approval workflows
* SharePoint documents
* Power Automate
* Outlook integration

Building this entirely in Python would be unnecessary.

Copilot Studio is the right fit.

---

# Core Components

## Azure AI Foundry

Provides:

* AI Models
* Azure OpenAI
* Open-source models
* Agent Service
* Prompt Flow
* Evaluations
* Model Catalog
* Vector Search integration
* AI Safety
* Fine-tuning
* AI Observability
* SDKs
* APIs

Think of it as an **AI engineering platform**.

---

## Copilot Studio

Provides:

* Agent Builder
* Topics
* Knowledge
* Prompt Actions
* Agent Flows
* Power Automate
* Teams Integration
* Microsoft 365 Integration
* Dynamics Integration
* Publishing
* Analytics

Think of it as an **AI business application platform**.

---

# Who Uses Them?

## Azure AI Foundry

Typically used by:

* AI Engineers
* Machine Learning Engineers
* Python Developers
* Solution Architects
* Platform Engineers

Example:

```python
response = client.chat.completions.create(...)
```

Everything is code.

---

## Copilot Studio

Typically used by:

* Business Analysts
* Power Platform Developers
* Citizen Developers
* Functional Consultants
* Solution Architects

Everything is configured through the UI with minimal code.

---

# Typical Development Process

## Azure AI Foundry

1. Select a model
2. Deploy the model
3. Write code
4. Implement RAG
5. Build memory
6. Build tools
7. Build APIs
8. Build agents
9. Deploy application

---

## Copilot Studio

1. Create an agent
2. Describe the agent
3. Upload knowledge
4. Create topics
5. Add prompt actions
6. Add agent flows
7. Publish to Teams or Microsoft 365

---

# Customization

## Azure AI Foundry

You can customize:

* Memory
* RAG
* Model routing
* Prompt chaining
* Multi-agent orchestration
* Retry policies
* Evaluation
* Observability
* Security
* Vector databases
* Tool calling
* Model selection

Almost everything is under your control.

---

## Copilot Studio

You configure:

* Topics
* Knowledge
* Agent instructions
* Prompt actions
* Power Automate flows
* Connectors
* Publishing
* Analytics

The platform manages much of the underlying complexity.

---

# Integration

## Azure AI Foundry

Can integrate with:

* SAP
* Dynamics 365
* Oracle
* SQL Server
* PostgreSQL
* Redis
* Cosmos DB
* Azure AI Search
* Custom APIs
* Any application via SDKs or REST APIs

---

## Copilot Studio

Can integrate with:

* Microsoft Teams
* SharePoint
* Outlook
* Microsoft Graph
* Dynamics 365
* Power Apps
* Power Automate
* Dataverse
* Custom connectors and APIs

---

# Cost

## Azure AI Foundry

You pay for:

* Model inference
* Compute
* Storage
* AI Search
* Vector database
* Network
* Monitoring
* Custom infrastructure

You control optimization.

---

## Copilot Studio

Typically licensed per user, message, or capacity (depending on licensing model), with much of the infrastructure managed for you. It can also incur costs for connected Azure AI services and Power Platform components.

---

# Decision Matrix

| Scenario                                     | Recommended Platform              | Why                                                  |
| -------------------------------------------- | --------------------------------- | ---------------------------------------------------- |
| HR Policy Assistant                          | Copilot Studio                    | Fast, low-code, Teams integration                    |
| Employee Leave Assistant                     | Copilot Studio                    | Microsoft 365 integration                            |
| Dynamics 365 Sales Copilot Extension         | Copilot Studio                    | Native Dynamics integration                          |
| Enterprise Procurement Agent                 | Copilot Studio + Azure AI Foundry | Business workflow + custom AI capabilities           |
| AI Contract Review Platform                  | Azure AI Foundry                  | Complex document processing and custom orchestration |
| Medical Diagnosis Assistant                  | Azure AI Foundry                  | Advanced AI, governance, and model control           |
| Financial Risk Engine                        | Azure AI Foundry                  | Custom models and regulatory requirements            |
| Company-wide Microsoft 365 Copilot Extension | Copilot Studio                    | Extends Microsoft 365 experiences                    |
| Multi-Agent Research Platform                | Azure AI Foundry                  | Full orchestration and custom agent design           |

---

# When to Use Both Together

Many enterprise solutions combine the two:

```text
Employee
      │
      ▼
Microsoft Teams
      │
      ▼
Copilot Studio
      │
      ├── SharePoint Knowledge
      ├── Power Automate
      ├── Microsoft Graph
      │
      ▼
Azure AI Foundry
      │
      ├── Custom Agent Service
      ├── Model Router
      ├── RAG Pipeline
      ├── Azure AI Search
      └── Multiple Foundation Models
```

In this architecture:

* **Copilot Studio** provides the conversational interface, business workflows, and Microsoft ecosystem integration.
* **Azure AI Foundry** performs advanced AI tasks such as custom agent orchestration, model routing, sophisticated RAG, evaluations, and reasoning.

---

# Rule of Thumb

Use **Copilot Studio** when:

* You need a business copilot quickly.
* The solution is centered around Microsoft 365, Teams, Dynamics 365, or Power Platform.
* Low-code development is preferred.
* Business users or functional teams will maintain the solution.

Use **Azure AI Foundry** when:

* You need full control over AI architecture.
* You're building custom AI applications or platforms.
* You require advanced RAG, multiple models, custom agents, evaluations, or fine-tuning.
* Developers and AI engineers will build and maintain the solution.

Use **both together** when you want a business-friendly conversational experience backed by enterprise-grade AI capabilities. This combined approach is increasingly common in large organizations and aligns well with the architecture-focused mindset
