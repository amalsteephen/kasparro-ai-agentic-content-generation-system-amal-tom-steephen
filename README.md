# Multi-Agent Content Generation System

This project implements an event-driven, autonomous multi-agent system that converts structured product data into machine-readable content pages. The goal is to demonstrate agent autonomy, dynamic coordination, and clean system design rather than static or sequential control flow.

---

## What the Project Does

Given a structured product dataset, the system automatically generates:

- A FAQ page
- A Product information page

All outputs are generated programmatically in JSON format without manual content writing.

---

## How the System Works

The system is composed of multiple independent agents, each responsible for a single task such as parsing data, generating questions, building reusable content blocks, or assembling final pages.

Agents communicate indirectly through a shared event bus. Each agent observes shared state, decides when it is ready to act, and publishes its output as an event. A lightweight orchestrator coordinates execution without enforcing a fixed order, allowing agent interactions and execution flow to emerge dynamically.

---

## How to Run the Project

1. (Optional) Activate the virtual environment:
```bash
venv\Scripts\activate
