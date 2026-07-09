# Azure Foundary

# What is Microsoft Copilot Studio?
It is low code/no code Ai agent development platform from microsoft that allows organizations to build, customize, deploy and manage intelligent AI agents

- these agents can answer the questions
- automate business process
- intercat with enterprise systems
- perform complex multi-step task using generative AI


# Major components
1. Agent
2. Instructions - system prompt
3. Knowldge - RAG
4. Actions (Tools)
5. Topics - are guided conversation
6. Generative AI Orchestration - instead of manually defining conversation path



# Important features
1. natural language agent creation
2. visual agent builder
3. Knowldge sources
4. enterprise search (RAG)
5. Action execution
6. authenticationm
7. connectors




# Agent type
- Knowldge agent - basic - FAQ, HR, Documentation
- action agent - limited - Automation, workflows
- agentic AI agent - enterprise assistants, business process
- Multi agent solution - complex enterprise orchestration



custom agents = you build an Ai assistant from scratch
declarative agent = you customize the existing copilot


A declartive agent is essentially copilot + your business instructions + your business knowldge + your business action





# When should you use a declartive agent?
- create HR assistant
- create an IT support assistent



# when should you use a custom agent instead?
- choose a custom agent when you need
- complex business workjflow
- human approval processer



# Old UI

topics -> trigger -> questions -> conditions -> messages


# Modern approach

instructions -> knowldge -> action -> generative orchestration



Step 1: create -> agent -> describe the agent


Step 2: configure instruction


You are an internal procurement assistant for ABC Manufacturing.


Responsibilites:

1. Answer only procurement-related questions.
2. Use company procurement policy knowledge wherever available.
3. Ask clarifying questions when purchase amount, item type, vendor status, or business justification is missing.
4. Do not approve purchases yourself.
5. For high-value purchases, explain the approval path.
6. For software purchases, always mention security review.
7. If the answer is not available in knowledge, say that the user should contact the procurement team.
8. For new vendors, explain onboarding documents
9. If information isn't aviable, ask the user contact procument
10. explain approval workflow



Step 3: upload knowledge


Step 4: replace topic 

Step 5: where does conditional logic go

option1 : let LLM + Knowledge handle it

option2: use an action

Amount = 500000 -> Approval action -> return (approved | rejected)


Step 6: messages


Before guiding a purchase request,
collect:

- item
- quantity
- estimated cost
- vendor
- busniess justification

if any information is missing,
ask follow-up question one at a time




# instruction - yes
# knowledge configuration - yes - adding/removing sharepoint, sites, folders, files
# knowldge content - no
# actions/ tools - yes
# activity - no
# monitor - no




# Skills


Instruction - define the agent personality and behavior
Knowldge - provides information the agent can answer from
action - perform a single operationm (API call, power automation flow, sql query, etc)
skills = perform a compete business capability that may involve multiple steps, actions, decision and conversaion




A skill is a resiable business function that an Ai agent can execute when it determines the user request matched that capability


HR Assistant

 - Leave request skill
 - payroll skill
 - employee lookup skill
 - performance review skill



- easier to maintain
- easier to test
- easier to reuse
- easier to scala



# Skill vs actions


Action - no conversation

Skill - can include conversation and reasining



# skill vs knowldge

skill - perform work

knowledge - answer question



# skill vs instruction


instruction - tell the Ai how to behave




Procurement Assistent

- Purchse request skll
- vendor onboarding skill
= Approval lookup skill



item -> quantity -> estimated cosy -> vendor -> bsuiness justification















