## Multi-Agent Content Generation System

---

## Problem Statement

In many companies, product information is already available in structured form, but creating content such as FAQs, product description pages, and comparison pages is still done manually. This process is slow, repetitive, and difficult to scale as the number of products grows. The goal of this project is to design an automated system that can take structured product data and consistently generate multiple content pages without manual effort.

---

## Solution Overview

To address this problem, I built an event-driven multi-agent content generation system where each agent operates autonomously. Instead of following a fixed execution order, agents observe shared system state, decide independently when to act, and publish results as events that other agents can react to. A lightweight orchestrator coordinates execution without enforcing control flow, allowing agent interactions and data flow to emerge dynamically.


---

## Scope & Assumptions

- The system works strictly with the product data provided in the assignment and does not rely on any external sources.
- The comparison page includes a fictional competitor product that is structured but not based on real-world research.
- The focus of this project is backend automation and system design, not frontend or UI development.
- All generated outputs are produced in machine-readable JSON format.

---

## System Design

Agents operate autonomously by observing shared state via an event bus and publishing events when their internal decision conditions are met. The orchestrator does not dictate execution order and serves only as a coordination loop, allowing agent interactions to emerge dynamically.

### Agent Responsibilities

- **ProductParserAgent**  
  This agent takes the raw product data and converts it into a clean, normalized internal format that can be used by the rest of the system.

- **QuestionGenerationAgent**  
  This agent generates a set of categorized user questions based on the product details, covering areas such as usage, safety, purchase, and comparison.

- **ContentLogicAgent**  
  This agent creates reusable content blocks such as benefits, usage instructions, safety information, ingredients, and pricing. These blocks are designed to be reused across multiple pages.

- **TemplateAssemblyAgent**  
  This agent assembles complete pages by combining content blocks with predefined templates for FAQ and product pages.

- **ComparisonAgent**  
  This agent generates a structured comparison between the main product and a fictional competitor product.

- - **OrchestratorAgent**  
  The orchestrator acts as a coordination loop rather than a controller. It does not dictate execution order or directly invoke agent logic. Instead, it continuously evaluates agent readiness and allows agents to act autonomously based on shared state and published events.


---

### Agent Interaction & Coordination

The system operates through a shared event bus that enables indirect agent-to-agent communication. Agents continuously observe shared state, evaluate whether their internal conditions are met, and act by publishing new events. Execution order is not predefined and emerges dynamically based on data availability and agent decisions.

For example:
- The ProductParserAgent publishes parsed product data when raw input becomes available.
- The QuestionGenerationAgent reacts to parsed product data and publishes generated questions.
- The ContentLogicAgent independently generates reusable logic blocks when sufficient product context exists.
- The TemplateAssemblyAgent assembles final pages only after required inputs are available.

This design ensures agent autonomy, loose coupling, and dynamic coordination rather than static control flow.


---

### Design Rationale

This architecture prioritizes agent autonomy and dynamic coordination over rigid pipelines. By decoupling agents through shared state and event-based communication, the system allows agents to evolve independently while remaining composable. The orchestrator’s minimal role ensures that no single component enforces execution order, aligning the design with real-world agentic systems used in scalable automation platforms.


---



