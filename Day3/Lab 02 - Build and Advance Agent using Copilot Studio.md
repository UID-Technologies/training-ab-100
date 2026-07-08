# Lab 2: Build an Advanced Enterprise IT Support Agent in Copilot Studio

## Scenario

ABC Manufacturing has 15,000 employees. The IT service desk receives many repetitive requests:

* Software installation
* VPN access
* Laptop request
* Password reset guidance
* Ticket status inquiry
* Escalation to human support

The CIO wants a Copilot Studio agent that can:

* Answer from IT policy documents
* Collect request details
* Classify support issues using a prompt action
* Trigger an automation using Power Automate / agent flow
* Call an external ticket API conceptually
* Escalate urgent issues
* Use activity map and analytics for monitoring

---

# Lab Objectives

By the end of this lab, participants will build:

**ABC IT Support Agent**

The agent can handle:

```text
I need Visual Studio installed.
```

```text
My VPN is not working.
```

```text
Check ticket INC12345.
```

```text
My laptop is damaged and this is urgent.
```

```text
Summarize this issue: Outlook crashes every morning after login.
```

---


Generative orchestration allows an agent to choose topics, tools, agents, and knowledge sources at runtime based on user intent. Microsoft also recommends giving high-quality descriptions to topics, tools, and knowledge sources so the orchestrator can select the right capability.

---

# Prerequisites

Participants need:

* Copilot Studio access
* Power Platform environment
* Permission to create agents
* Permission to create agent flows or Power Automate flows
* Optional: Teams channel enabled for publishing
* Optional: HTTP connector access for API action demo

---

# Sample IT Policy Knowledge File

Create a Word or PDF file named:

```text
ABC_IT_Support_Policy.pdf
```

Use this content:

```text
ABC Manufacturing IT Support Policy

1. Standard software such as Microsoft Office, Teams, Edge, and Power BI Desktop is pre-approved.
2. Developer tools such as Visual Studio, VS Code, Docker Desktop, SQL Server Developer Edition, and Postman require manager approval.
3. Any paid software, SaaS application, or cloud subscription requires IT security review and procurement approval.
4. VPN access is available only to full-time employees and approved contractors.
5. VPN issues should first be resolved by checking MFA status, password expiry, device compliance, and internet connectivity.
6. Laptop replacement is allowed if the device is older than 4 years, physically damaged, or approved by IT asset management.
7. Urgent issues include device failure, security incident, data loss, production access issue, or business-critical outage.
8. Password reset should be performed through the official self-service password reset portal.
9. The IT service desk operates Monday to Friday, 9 AM to 6 PM.
10. Ticket status can be checked using the ITSM ticket number.
```

---

# Part 1 — Create the Advanced IT Support Agent

## Step 1: Open Copilot Studio

1. Open **Copilot Studio**.
2. Select the correct environment.
3. Select **Create**.
4. Select **New agent**.

Microsoft’s current Copilot Studio experience supports creating agents by describing what the agent should do in natural language. 

---

## Step 2: Describe the Agent

Enter:

```text
Create an Enterprise IT Support Agent for ABC Manufacturing.

The agent helps employees with software installation, VPN access, laptop requests, password reset guidance, ticket status, and urgent IT escalation.

The agent should answer from IT policy knowledge, ask clarifying questions when information is missing, classify issues, and guide users to the correct support path.
```

Select **Create**.

---

## Step 3: Configure Agent Name

Set the name:

```text
ABC IT Support Agent
```

Set description:

```text
Helps employees resolve IT support questions, software requests, VPN access issues, laptop replacement requests, password reset guidance, ticket status checks, and escalation.
```

---

## Step 4: Add Agent Instructions

Open the agent’s **Instructions** section and add:

```text
You are an internal IT Support Agent for ABC Manufacturing.

Rules:
1. Answer only IT support-related questions.
2. Use IT support policy knowledge wherever available.
3. Ask clarifying questions when employee name, department, device type, software name, business reason, or urgency is missing.
4. Never claim that a ticket has been created unless an action or flow confirms it.
5. Never approve software, access, or laptop requests yourself.
6. Paid software and SaaS requests require IT security review and procurement approval.
7. Developer tools require manager approval.
8. Urgent issues must be escalated to human IT support.
9. Password reset must be guided through the official self-service password reset portal.
10. If the answer is not available, ask the user to contact the IT service desk.
```

Save.

---

# Part 2 — Enable Generative Orchestration

## Step 1: Open Generative AI Settings

1. Open the agent.
2. Go to **Settings**.
3. Select **Generative AI**.
4. Enable:

```text
Generative orchestration
```

5. Save.

With generative orchestration enabled, the agent can choose the right topic, tool, or knowledge source automatically instead of depending only on fixed trigger phrases. 

---

# Part 3 — Add IT Knowledge Source

## Step 1: Upload IT Policy

1. Open **Knowledge**.
2. Select **Add knowledge**.
3. Select **Upload file**.
4. Upload:

```text
ABC_IT_Support_Policy.pdf
```

5. Name the knowledge source:

```text
ABC IT Support Policy
```

6. Description:

```text
Contains ABC Manufacturing IT support rules for software installation, VPN access, laptop replacement, password reset, ticket status, escalation, and service desk hours.
```

7. Save.

---

## Step 2: Test Knowledge

Open the test panel and ask:

```text
Can I install Docker Desktop?
```

Expected result:

```text
Docker Desktop is a developer tool and requires manager approval.
```

Ask:

```text
What should I check if VPN is not working?
```

Expected result:

```text
Check MFA status, password expiry, device compliance, and internet connectivity.
```

---

# Part 4 — Create Topic: Software Installation Request

## Step 1: Create Topic

1. Go to **Topics**.
2. Select **Add a topic**.
3. Select **Create from blank**.

Topic name:

```text
Software Installation Request
```

Topic description:

```text
Use this topic when the employee wants to install, request, or get approval for software, developer tools, SaaS tools, or cloud subscriptions.
```

---

## Step 2: Configure Trigger Description

In the trigger node, describe:

```text
This topic is selected when the user asks to install software, request developer tools, request paid software, request SaaS tools, or ask about software approval.
```

Example phrases:

```text
I need software installed
Install Visual Studio
Can I get Docker Desktop?
I need Power BI Desktop
Request new SaaS tool
```

---

## Step 3: Ask Software Name

Add a **Question** node:

```text
Which software do you want to install?
```

Save response as:

```text
varSoftwareName
```

---

## Step 4: Ask Business Reason

Add another **Question** node:

```text
What is the business reason for this software?
```

Save response as:

```text
varBusinessReason
```

---

## Step 5: Ask Software Type

Add a **Question** node:

```text
What type of software is this?
```

Options:

```text
Standard software
Developer tool
Paid software or SaaS
Not sure
```

Save response as:

```text
varSoftwareType
```

---

## Step 6: Add Approval Logic

Add a **Condition** node.

Condition 1:

```text
If varSoftwareType equals Standard software
```

Message:

```text
Standard software may be pre-approved based on ABC IT policy. Please confirm availability in the company software center.
```

Condition 2:

```text
If varSoftwareType equals Developer tool
```

Message:

```text
Developer tools require manager approval. Please include your manager name and business justification before submitting the request.
```

Condition 3:

```text
If varSoftwareType equals Paid software or SaaS
```

Message:

```text
Paid software, SaaS applications, and cloud subscriptions require IT security review and procurement approval.
```

Condition 4:

```text
If varSoftwareType equals Not sure
```

Message:

```text
I recommend submitting this for IT review because the software category is unclear.
```

---

## Step 7: Ask Manager Name

Add a **Question** node:

```text
Who is your manager?
```

Save as:

```text
varManagerName
```

---

## Step 8: Final Summary Message

Add a **Message** node:

```text
Software request summary:

Software: {varSoftwareName}
Business reason: {varBusinessReason}
Software type: {varSoftwareType}
Manager: {varManagerName}

Next step: submit this request for IT review. I can collect request details, but I cannot approve the software directly.
```

---

# Part 5 — Create Topic: VPN Troubleshooting

## Step 1: Create Topic

Go to **Topics** → **Add a topic** → **Create from blank**.

Topic name:

```text
VPN Troubleshooting
```

Topic description:

```text
Use this topic when users report VPN login issues, remote access issues, MFA problems, device compliance issues, or connectivity problems.
```

---

## Step 2: Add First Message

```text
I can help troubleshoot VPN access. Let me collect a few details.
```

---

## Step 3: Ask Employee Type

Question:

```text
Are you a full-time employee or approved contractor?
```

Options:

```text
Full-time employee
Approved contractor
Other
```

Save as:

```text
varEmployeeType
```

---

## Step 4: Ask MFA Status

Question:

```text
Is your MFA working successfully?
```

Options:

```text
Yes
No
Not sure
```

Save as:

```text
varMFAStatus
```

---

## Step 5: Ask Device Compliance

Question:

```text
Is your device marked compliant in Company Portal?
```

Options:

```text
Yes
No
Not sure
```

Save as:

```text
varDeviceCompliance
```

---

## Step 6: Add Conditions

If employee type is **Other**:

```text
VPN access is available only to full-time employees and approved contractors. Please contact IT service desk for access eligibility.
```

If MFA is **No**:

```text
Please resolve MFA first. VPN access can fail when MFA is not working.
```

If device compliance is **No**:

```text
Please fix device compliance in Company Portal. VPN access may be blocked for non-compliant devices.
```

Else:

```text
If MFA, password, device compliance, and internet connectivity are all working, please raise an IT ticket for VPN investigation.
```

---

# Part 6 — Create Prompt Action: Issue Classifier

This part demonstrates advanced prompt usage.

Copilot Studio supports prompt actions that use generative AI models from AI Builder and can be used as natural-language actions for agents. ([Microsoft Learn][4])

## Step 1: Open Tools or Actions

1. Open the agent.
2. Go to **Tools** or **Actions**.
3. Select **Add a tool**.
4. Choose **Prompt** or **Create prompt**.

The exact label may vary slightly by tenant, but in the new experience look for **Tools**, **Actions**, or **Prompts**.

---

## Step 2: Create Prompt

Prompt name:

```text
Classify IT Support Issue
```

Description:

```text
Classifies an employee IT issue into category, priority, suggested next team, and recommended next action.
```

Input:

```text
employeeIssue
```

Prompt instruction:

```text
You are an IT service desk triage assistant.

Classify the following employee issue.

Return the response in this format only:

Category:
Priority:
Suggested Team:
Recommended Next Action:
Escalation Required: Yes/No

Rules:
- Security incident, data loss, device failure, production access issue, or business-critical outage = High priority.
- Password reset = Low priority unless executive or production blocker.
- VPN issue = Medium priority unless business-critical outage.
- Software request = Medium priority.
- Laptop physical damage = High priority if the user cannot work.

Employee issue:
{employeeIssue}
```

---

## Step 3: Test Prompt

Sample input:

```text
My laptop is damaged and I cannot work.
```

Expected output:

```text
Category: Laptop / Device Issue
Priority: High
Suggested Team: IT Asset Management
Recommended Next Action: Escalate to IT support and start laptop replacement process.
Escalation Required: Yes
```

Save the prompt.

---

# Part 7 — Create Topic: Issue Triage Using Prompt Action

## Step 1: Create Topic

Topic name:

```text
IT Issue Triage
```

Description:

```text
Use this topic when the user describes an IT problem and wants help identifying category, priority, next team, or escalation path.
```

---

## Step 2: Ask User for Issue

Question:

```text
Please describe the IT issue you are facing.
```

Save as:

```text
varEmployeeIssue
```

---

## Step 3: Call Prompt Action

Add a node:

```text
Call an action
```

Select:

```text
Classify IT Support Issue
```

Map input:

```text
employeeIssue = varEmployeeIssue
```

Save output as:

```text
varIssueClassification
```

---

## Step 4: Show Classification

Message:

```text
Here is the issue triage result:

{varIssueClassification}
```

---

## Step 5: Add Escalation Guidance

Add a condition:

```text
If varIssueClassification contains "Escalation Required: Yes"
```

Message:

```text
This issue should be escalated to human IT support. Please create an urgent ticket or contact the IT service desk immediately.
```

Else:

```text
You can follow the recommended next action. If the issue continues, raise a standard IT ticket.
```

---

# Part 8 — Create Agent Flow / Power Automate Action: Submit Software Request

This demonstrates tool calling and enterprise automation.

Microsoft documents that agent flows can be added as tools. When added as a tool, the agent orchestrator can call the flow at runtime to retrieve data or perform actions. ([Microsoft Learn][1])

## Step 1: Create Agent Flow

1. Open **Tools** or **Actions**.
2. Select **Add a tool**.
3. Choose **Agent flow** or **Power Automate flow**.
4. Select **Create new flow**.

Flow name:

```text
Submit Software Request
```

---

## Step 2: Define Flow Inputs

Create inputs:

```text
EmployeeName
SoftwareName
BusinessReason
SoftwareType
ManagerName
```

---

## Step 3: Add Flow Logic

For a simple classroom lab, avoid connecting to real ServiceNow.

Add a **Compose** or response step that returns:

```text
Request submitted successfully.

Request ID: SW-{current timestamp}
Status: Pending IT Review
Next Approval: Manager / IT Security / Procurement based on software type
```

If your tenant supports Dataverse, optionally create a Dataverse row instead.

Suggested table:

```text
IT Software Requests
```

Columns:

```text
RequestId
EmployeeName
SoftwareName
BusinessReason
SoftwareType
ManagerName
Status
CreatedOn
```

---

## Step 4: Return Output to Agent

Return these fields:

```text
RequestId
Status
NextApproval
Message
```

Save and add the flow as a tool.

---

# Part 9 — Connect Software Topic to Flow

Go back to topic:

```text
Software Installation Request
```

After the summary message, add a question:

```text
Do you want me to submit this software request for review?
```

Options:

```text
Yes
No
```

Save as:

```text
varSubmitRequest
```

Add condition:

```text
If varSubmitRequest equals Yes
```

Call action:

```text
Submit Software Request
```

Map:

```text
EmployeeName = user name or ask the user
SoftwareName = varSoftwareName
BusinessReason = varBusinessReason
SoftwareType = varSoftwareType
ManagerName = varManagerName
```

Show response:

```text
Your software request has been submitted.

Request ID: {RequestId}
Status: {Status}
Next approval: {NextApproval}
```

Else:

```text
No problem. You can submit it later through the IT service portal.
```

---

# Part 10 — Create Topic: Ticket Status Check

This part can be done as a conceptual REST/API integration.

Copilot Studio supports adding tools to custom agents so the agent can use them with generative orchestration or call them explicitly from topics. ([Microsoft Learn][5])

## Step 1: Create Topic

Topic name:

```text
Ticket Status Check
```

Description:

```text
Use this topic when users ask to check ITSM ticket status, incident status, request status, or provide a ticket number such as INC12345 or REQ12345.
```

---

## Step 2: Ask Ticket Number

Question:

```text
Please enter your ticket number.
```

Save as:

```text
varTicketNumber
```

---

## Step 3: Mock Ticket Response

For classroom demo without API connector, add condition-based mock responses.

If ticket number contains:

```text
INC
```

Message:

```text
Ticket {varTicketNumber} status:

Status: In Progress
Assigned team: IT Service Desk
Priority: Medium
Estimated update: Within 4 business hours
```

If ticket number contains:

```text
REQ
```

Message:

```text
Request {varTicketNumber} status:

Status: Pending Approval
Assigned team: IT Operations
Next step: Manager approval
```

Else:

```text
I could not identify this ticket format. Please provide a ticket number starting with INC or REQ.
```

---

## Optional API Version

If the environment allows HTTP/custom connectors:

1. Create a custom connector or HTTP action.
2. Endpoint example:

```text
GET https://your-api-domain/api/tickets/{ticketNumber}
```

3. Response example:

```json
{
  "ticketNumber": "INC12345",
  "status": "In Progress",
  "priority": "Medium",
  "assignedTeam": "IT Service Desk",
  "eta": "4 business hours"
}
```

4. Add it as a tool.
5. Call it from the topic.

---

# Part 11 — Create Topic: Urgent Escalation

## Step 1: Create Topic

Topic name:

```text
Urgent IT Escalation
```

Description:

```text
Use this topic when users mention urgent IT issues, business-critical outage, device failure, security incident, data loss, laptop damage, or production access issue.
```

---

## Step 2: Ask Impact

Question:

```text
What is the business impact of this issue?
```

Options:

```text
I cannot work
Production system is impacted
Security incident or data loss
Minor issue
```

Save as:

```text
varImpact
```

---

## Step 3: Ask Contact Number

Question:

```text
Please provide your contact number or Teams alias for IT support follow-up.
```

Save as:

```text
varContact
```

---

## Step 4: Add Escalation Message

If impact is:

```text
I cannot work
Production system is impacted
Security incident or data loss
```

Message:

```text
This qualifies as an urgent IT issue. Please contact the IT service desk immediately.

Escalation summary:
Impact: {varImpact}
Contact: {varContact}

I recommend creating an urgent ticket and notifying the IT support team.
```

If impact is:

```text
Minor issue
```

Message:

```text
This appears to be a standard issue. Please create a normal IT ticket through the service portal.
```

---

# Part 12 — Improve Generative Orchestration Descriptions

Review descriptions for:

* Topics
* Knowledge source
* Prompt action
* Agent flow
* Ticket status action

Use clear descriptions because Copilot Studio uses these descriptions to select the right capability when generative orchestration is enabled. ([Microsoft Learn][2])

Recommended descriptions:

## Software Topic

```text
Handles software installation, developer tools, SaaS requests, paid software, manager approval, and software request submission.
```

## VPN Topic

```text
Handles VPN access problems, MFA issues, password expiry, device compliance, and remote connectivity troubleshooting.
```

## Issue Classifier Prompt

```text
Classifies raw IT issues into category, priority, suggested team, recommended action, and escalation requirement.
```

## Submit Software Request Flow

```text
Submits a software request for IT review and returns request ID, status, and next approval step.
```

---

# Part 13 — Test Full Agent

Use the test panel.

## Test 1: Software Request

User:

```text
I need Visual Studio installed.
```

Expected behavior:

* Agent chooses software request topic
* Asks software name if missing
* Asks business reason
* Identifies developer tool
* Mentions manager approval
* Offers request submission

---

## Test 2: Paid SaaS

User:

```text
Can I buy a new SaaS tool for marketing automation?
```

Expected behavior:

* Mentions IT security review
* Mentions procurement approval
* Collects business reason
* Does not approve directly

---

## Test 3: VPN Issue

User:

```text
My VPN is not working.
```

Expected behavior:

* Agent invokes VPN troubleshooting
* Asks employee type
* Checks MFA
* Checks device compliance
* Gives next step

---

## Test 4: Issue Triage

User:

```text
Summarize this issue: My laptop is damaged and I cannot work.
```

Expected behavior:

```text
Category: Laptop / Device Issue
Priority: High
Suggested Team: IT Asset Management
Escalation Required: Yes
```

---

## Test 5: Ticket Status

User:

```text
Check ticket INC12345.
```

Expected behavior:

```text
Status: In Progress
Assigned team: IT Service Desk
Priority: Medium
Estimated update: Within 4 business hours
```

---

## Test 6: Urgent Escalation

User:

```text
My laptop is broken and this is urgent.
```

Expected behavior:

* Agent chooses urgent escalation
* Asks business impact
* Asks contact
* Recommends urgent IT escalation

---

# Part 14 — Review Activity Map

1. Ask one full test question.
2. Open the activity map or activity review.
3. Review:

   * Which topic was selected
   * Whether knowledge was used
   * Whether a prompt action was called
   * Whether a flow/tool was called
   * Any errors or missing inputs

Microsoft describes activity review as a way to see interactions and decisions made by the agent, diagnose behavior that does not match goals, and find error details.

---

# Part 15 — Review Analytics

1. Open **Analytics**.
2. Review available metrics:

   * Conversations
   * Engagement
   * Resolution
   * Escalation
   * Topic usage
   * Errors

Copilot Studio analytics provides usage and performance data for agents and their components.

---

# Part 16 — Publish the Agent

1. Select **Publish**.
2. Confirm publish.
3. Open **Channels**.
4. Choose one:

   * Demo website
   * Microsoft Teams
   * Microsoft 365 Copilot, if available
   * Custom website

Copilot Studio supports publishing agents to multiple platforms such as websites, mobile apps, Microsoft 365 Copilot, Teams, and other messaging platforms. 

---
