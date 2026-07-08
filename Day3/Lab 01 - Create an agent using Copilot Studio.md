# Lab 01: Build an Enterprise Procurement Assistant in Copilot Studio

## Scenario

ABC Manufacturing wants an internal agent that helps employees with procurement questions and purchase request guidance.

The agent should:

* Answer procurement policy questions
* Guide users through purchase request creation
* Escalate high-value requests for approval
* Use uploaded policy documents as grounding knowledge
* Demonstrate topics, knowledge, actions, generative orchestration, testing, and publishing

Copilot Studio is Microsoft’s low-code platform for building agents, adding knowledge, using tools, and publishing to channels. Microsoft’s current documentation also confirms support for generative orchestration, where the agent can choose topics, tools, agents, and knowledge sources based on user intent. ([Microsoft Learn][1]) ([Microsoft Learn][2])

---

# Lab Objective

By the end of this lab, participants will create:

**Procurement Policy Assistant**

The agent can answer:

* “What is the approval limit for laptop purchase?”
* “I want to buy 20 laptops.”
* “Can I purchase software from a new vendor?”
* “What documents are required for supplier onboarding?”

---

# Prerequisites

Participants need:

* Copilot Studio access
* Microsoft Power Platform environment
* Permission to create agents
* A small procurement policy PDF or Word document
* Optional: SharePoint site for enterprise knowledge source

---

# Sample Policy Content

Use this as a Word/PDF file and upload it as knowledge.

```text
ABC Manufacturing Procurement Policy

1. Purchases below ₹50,000 can be approved by the department manager.
2. Purchases between ₹50,000 and ₹5,00,000 require finance approval.
3. Purchases above ₹5,00,000 require procurement head and finance director approval.
4. New vendor onboarding requires GST details, PAN, bank details, compliance declaration, and signed NDA.
5. Software purchase requires security review before procurement approval.
6. Emergency purchases must be justified with a business reason.
7. Purchase requests must include item description, quantity, estimated cost, vendor details, and business justification.
```

---

# Part 1 — Create the Agent

## Step 1: Open Copilot Studio

1. Go to **Copilot Studio**.
2. Select the required environment from the top-right environment selector.
3. From the home page, select **Create**.
4. Select **New agent**.

In the new experience, Microsoft allows creating an agent by describing what the agent should do in natural language. ([Microsoft Learn][3])

---

## Step 2: Describe the Agent

Enter this description:

```text
Create an internal Procurement Policy Assistant for ABC Manufacturing. 
The agent helps employees understand procurement rules, approval limits, supplier onboarding requirements, software purchase rules, and purchase request guidance. 
The agent must answer using company policy knowledge and should ask clarifying questions when purchase details are missing.
```

Select **Create**.

---

## Step 3: Configure Basic Details

Open the agent configuration page and update:

**Name**

```text
ABC Procurement Assistant
```

**Description**

```text
Helps employees understand procurement policy, purchase approval rules, supplier onboarding requirements, and software purchase governance.
```

**Instructions**

```text
You are an internal procurement assistant for ABC Manufacturing.

Follow these rules:
1. Answer only procurement-related questions.
2. Use company procurement policy knowledge wherever available.
3. Ask clarifying questions when purchase amount, item type, vendor status, or business justification is missing.
4. Do not approve purchases yourself.
5. For high-value purchases, explain the approval path.
6. For software purchases, always mention security review.
7. If the answer is not available in knowledge, say that the user should contact the procurement team.
```

---

# Part 2 — Enable Generative Orchestration

## Step 1: Open Settings

1. Open the agent.
2. Go to **Settings**.
3. Open **Generative AI**.
4. Under **Orchestration**, set:

```text
Use generative AI orchestration for your agent's responses = Yes
```

5. Save the change.

Generative orchestration allows the agent to select relevant topics, tools, agents, and knowledge sources dynamically, instead of relying only on fixed trigger phrases. ([Microsoft Learn][2])

---

# Part 3 — Add Knowledge Source

## Step 1: Add Procurement Policy File

1. Open the agent.
2. Go to **Knowledge**.
3. Select **Add knowledge**.
4. Choose **Upload file**.
5. Upload the procurement policy file created earlier.
6. Name it:

```text
ABC Procurement Policy
```

7. Add description:

```text
Contains ABC Manufacturing procurement approval limits, vendor onboarding rules, software purchase rules, and purchase request requirements.
```

8. Save.

Copilot Studio supports knowledge sources so agents can use internal or external information for generative answers. ([Microsoft Learn][4])

---

## Step 2: Test Knowledge

Open the test panel and ask:

```text
What approval is required for a purchase of ₹2,00,000?
```

Expected answer:

```text
A purchase between ₹50,000 and ₹5,00,000 requires finance approval.
```

Ask:

```text
What is needed for new vendor onboarding?
```

Expected answer:

```text
GST details, PAN, bank details, compliance declaration, signed NDA.
```

---

# Part 4 — Create Topic: Purchase Request Guidance

## Step 1: Create Topic

1. Go to **Topics**.
2. Select **Add a topic**.
3. Select **Create from blank**.

Topic name:

```text
Purchase Request Guidance
```

Topic description:

```text
Use this topic when the employee wants to create or understand a purchase request, including required details, approval path, or missing information.
```

With generative orchestration enabled, topic descriptions become very important because the agent uses descriptions to decide when to invoke a topic. ([Microsoft Learn][2])

---

## Step 2: Add Trigger Description

In the trigger node, use:

```text
The agent chooses this topic when the user wants to create a purchase request, check purchase approval flow, or understand required purchase request fields.
```

---

## Step 3: Add Questions

Add a question node:

```text
What item do you want to purchase?
```

Save answer as:

```text
varItem
```

Add another question:

```text
What is the estimated purchase amount?
```

Save answer as:

```text
varAmount
```

Add another question:

```text
Is this a new vendor?
```

Options:

```text
Yes
No
Not sure
```

Save answer as:

```text
varNewVendor
```

Add another question:

```text
Is this a software or technology purchase?
```

Options:

```text
Yes
No
```

Save answer as:

```text
varSoftwarePurchase
```

---

## Step 4: Add Conditional Logic

Add condition:

```text
If varAmount is greater than 500000
```

Message:

```text
This purchase requires approval from the Procurement Head and Finance Director. Please prepare business justification, vendor details, estimated cost, and supporting documents.
```

Else if:

```text
varAmount is greater than 50000
```

Message:

```text
This purchase requires Finance approval. Please include item details, quantity, estimated cost, vendor details, and business justification.
```

Else:

```text
This purchase can be approved by your department manager, provided all purchase request details are complete.
```

---

## Step 5: Add Software Purchase Rule

Add condition:

```text
If varSoftwarePurchase equals Yes
```

Message:

```text
Because this is a software or technology purchase, a security review is required before procurement approval.
```

---

## Step 6: Add New Vendor Rule

Add condition:

```text
If varNewVendor equals Yes
```

Message:

```text
For a new vendor, please collect GST details, PAN, bank details, compliance declaration, and signed NDA before onboarding.
```

---

## Step 7: Final Response

Add final message:

```text
Purchase request summary:

Item: {varItem}
Estimated amount: {varAmount}
New vendor: {varNewVendor}
Software purchase: {varSoftwarePurchase}

Please submit the request through the official procurement system. I can guide you on the required documents, but I cannot approve the purchase.
```

---

# Part 5 — Create Topic: Software Purchase Governance

## Step 1: Create Topic

Go to **Topics** → **Add a topic** → **Create from blank**.

Name:

```text
Software Purchase Governance
```

Description:

```text
Use this topic when a user asks about buying software, SaaS tools, IT subscriptions, cloud services, or technology products.
```

---

## Step 2: Add Message

```text
Software purchases require security review before procurement approval.
```

---

## Step 3: Ask Vendor Status

Question:

```text
Is the software vendor already approved?
```

Options:

```text
Yes
No
Not sure
```

---

## Step 4: Add Conditions

If **Yes**:

```text
You can proceed with the purchase request, but security review is still required before approval.
```

If **No**:

```text
The vendor must go through onboarding first. Required documents include GST details, PAN, bank details, compliance declaration, and signed NDA.
```

If **Not sure**:

```text
Please check the approved vendor list or contact the procurement team before submitting the request.
```

---

# Part 6 — Add a Prompt Library Style Instruction

This is not a separate Copilot Studio feature in every tenant, so for the lab we implement it through reusable instructions.

Go to **Settings** → **Generative AI** → agent instructions and add:

```text
Response style:
- Start with the direct answer.
- Then explain the approval rule.
- Then mention required documents or next steps.
- Keep the answer concise.
- Do not make legal, financial, or procurement approval decisions.
```

This demonstrates **prompt governance** and **standardized response behavior**.

---

# Part 7 — Test the Agent

Use the test panel.

## Test 1

User:

```text
I want to buy 20 laptops worth ₹8,00,000.
```

Expected behavior:

```text
The agent should identify that the amount is above ₹5,00,000 and explain that Procurement Head and Finance Director approval is required.
```

---

## Test 2

User:

```text
Can I buy a new SaaS tool for my team?
```

Expected behavior:

```text
The agent should mention software purchase security review and vendor onboarding if the vendor is new.
```

---

## Test 3

User:

```text
What documents are required for supplier onboarding?
```

Expected behavior:

```text
The agent should answer from knowledge: GST details, PAN, bank details, compliance declaration, and signed NDA.
```

---

## Test 4

User:

```text
Create a purchase request for office chairs.
```

Expected behavior:

```text
The agent should ask item, amount, vendor status, and whether it is software/technology purchase.
```

---

# Part 8 — Review Activity Map

While testing:

1. Open the test panel.
2. Ask a question.
3. Open **Activity map**.
4. Review which topic, knowledge source, or action was selected.

The activity map helps understand how the agent responds when generative orchestration is enabled. ([Microsoft Learn][2])

---

# Part 9 — Publish Agent

1. Select **Publish**.
2. Confirm **Publish**.
3. Open the agent menu.
4. Select **Go to demo website**.
5. Test the published agent.

Microsoft documentation notes that publishing depends on available channels and licensing. Trial access may allow testing but may not allow publishing. ([Microsoft Learn][3])

---
