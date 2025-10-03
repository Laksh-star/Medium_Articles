# Microsoft Agent Framework: Building Production-Ready AI Agents

Practical implementations demonstrating key features of the Microsoft Agent Framework through three real-world use cases.

📝 **Companion Article:** [Microsoft Agent Framework: Building Production-Ready AI Agents](https://medium.com/@your-username/microsoft-agent-framework-building-production-ready-ai-agents)

## 📚 Overview

This repository contains complete, runnable Jupyter notebooks showcasing the Microsoft Agent Framework's capabilities:

- **Multi-agent orchestration patterns** (Sequential, Concurrent, Fan-out/Fan-in)
- **Human-in-the-Loop workflows** with approval gates and checkpointing
- **MCP (Model Context Protocol)** integration via stdio and HTTP
- **Real-time streaming** and live transcript updates
- **Enterprise-grade patterns** for production deployments

## 🎯 Use Cases

### 1. Human-in-the-Loop Content Approval Workflow
**Notebook:** [`Medium_HTML_Resume_Workflow_MS_Agent_Framework.ipynb`](./Medium_HTML_Resume_Workflow_MS_Agent_Framework.ipynb)

**Features Demonstrated:**
- ✅ Human-in-the-Loop approval gates
- ✅ Checkpointing and state persistence
- ✅ Multi-agent collaboration (Writer + Reviewer agents)
- ✅ Iterative revision loops with human feedback
- ✅ Sequential orchestration
- ✅ Artifact generation and publishing

**Scenario:** Automate corporate communications drafting while maintaining human oversight for quality control and compliance.

---

### 2. Enterprise Orchestration with Concurrent Agents
**Notebook:** [`Medium_Workflow_MS_Agent_Framework.ipynb`](./Medium_Workflow_MS_Agent_Framework.ipynb)

**Features Demonstrated:**
- ✅ Fan-out/Fan-in orchestration patterns
- ✅ Concurrent/parallel agent execution
- ✅ MCP tool integration (calculator via stdio)
- ✅ Fallback mechanisms for unavailable tools
- ✅ Real-time streaming responses
- ✅ Multi-agent coordination and result aggregation

**Scenario:** Orchestrate three specialized agents (Research, Costing, Risk) working in parallel to produce a comprehensive enterprise planning report.

---

### 3. External API Integration via MCP over HTTP
**Notebook:** [`Medium_MCP_TMDB_Workflow_MS_Agent_Framework.ipynb`](./Medium_MCP_TMDB_Workflow_MS_Agent_Framework.ipynb)

**Features Demonstrated:**
- ✅ MCP over HTTP/SSE for remote services
- ✅ External API integration (TMDB movie database)
- ✅ Fan-out/fan-in orchestration
- ✅ Concurrent agent execution
- ✅ Structured data aggregation
- ✅ Graceful error handling for unavailable services

**Scenario:** Query a remote TMDB API server to discover films, check trends, and generate personalized movie recommendations using three collaborative agents.

## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.9+
python --version

# Install Agent Framework
pip install agent-framework --pre

# Install additional dependencies
pip install openai python-dotenv ipykernel
