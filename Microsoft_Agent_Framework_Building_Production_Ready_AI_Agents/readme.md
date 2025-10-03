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
```

### Environment Setup

Create a `.env` file in the repository root:

```bash
# Required for all notebooks
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_CHAT_MODEL_ID=gpt-4o-mini

# Optional: For Azure OpenAI (if you prefer)
# AZURE_OPENAI_ENDPOINT=your_endpoint
# AZURE_OPENAI_API_KEY=your_key
# AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment
```

### Running the Notebooks

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Laksh-star/Medium_Articles.git
   cd Medium_Articles/Microsoft_Agent_Framework_Building_Production_Ready_AI_Agents
   ```

2. **Install Jupyter:**
   ```bash
   pip install jupyter notebook
   ```

3. **Launch Jupyter:**
   ```bash
   jupyter notebook
   ```

4. **Open any notebook and run cells sequentially**

## 📋 Detailed Setup Instructions

### Use Case 1: HITL Workflow
No additional setup required. The notebook creates checkpoint files automatically.

**Expected outputs:**
- `af_hitl_ckpt.json` - State checkpoint file
- `approved_post.md` - Published artifact

### Use Case 2: Enterprise Workflow (MCP Calculator)

**Option A - With MCP Calculator (Recommended):**
```bash
# Install MCP calculator server
pip install mcp-server-calculator

# The notebook will automatically connect via stdio
```

**Option B - Without MCP (Fallback):**
The notebook includes a built-in local calculator that activates automatically if MCP is unavailable.

### Use Case 3: MCP TMDB Workflow

This notebook connects to a remote TMDB MCP server over HTTP. 

**Default Configuration:**
```python
MCP_URL = "https://steadfast-prosperity-production.up.railway.app/sse"
```

**To use your own TMDB MCP server:**
1. Deploy your own MCP TMDB server (instructions [here](https://github.com/modelcontextprotocol/servers/tree/main/src/tmdb))
2. Update the `MCP_URL` in the notebook
3. Add authentication headers if required

## 🏗️ Architecture Patterns

### Sequential + HITL Pattern (Use Case 1)
```
Start → Draft → Review → [Human Gate] → Approve/Revise → Publish
                              ↓
                          Revision Loop
```

### Concurrent Fan-Out/Fan-In Pattern (Use Case 2)
```
              ┌─→ Research Agent ─┐
Dispatcher ───┼─→ Costing Agent  ─┼─→ Aggregator → Report
              └─→ Risk Agent ─────┘
```

### MCP External Integration Pattern (Use Case 3)
```
              ┌─→ Discovery Agent (search_movies) ────┐
Dispatcher ───┼─→ Trends Agent (get_trending) ────────┼─→ Aggregator
              └─→ Recommendations Agent (get_recs) ────┘
                             ↓
                      TMDB API via MCP
```

## 🎓 Learning Path

**Recommended Order:**
1. **Start with Use Case 1** - Understand basic agent setup and HITL patterns
2. **Move to Use Case 2** - Learn concurrent orchestration and MCP tools
3. **Finish with Use Case 3** - Explore external API integration via MCP HTTP

## 🔧 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'agent_framework'`
```bash
pip install agent-framework --pre
```

**Issue:** `OpenAI API key not found`
- Ensure `.env` file exists in the notebook directory
- Verify `OPENAI_API_KEY` is set correctly
- Restart the Jupyter kernel after adding environment variables

**Issue:** MCP calculator connection fails (Use Case 2)
- The notebook will automatically fall back to local calculator
- To enable MCP: `pip install mcp-server-calculator`

**Issue:** TMDB MCP server unreachable (Use Case 3)
- Check your internet connection
- Verify `MCP_URL` is correct
- The notebook will show helpful error messages if connection fails

## 📖 Additional Resources

- **Microsoft Agent Framework Documentation:** [learn.microsoft.com/agent-framework](https://learn.microsoft.com/agent-framework)
- **GitHub Repository:** [github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **Model Context Protocol:** [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Azure AI Foundry Discord:** [aka.ms/foundry/discord](https://aka.ms/foundry/discord)

### Related Articles by Author

- [Developing Business Thinking AI Plugins using Semantic Kernel](https://medium.com/...)
- [Design Patterns for AI Agents: Using Autogen for Effective Multi-Agent Collaboration](https://medium.com/...)

## 🤝 Contributing

Found an issue or have an improvement? Feel free to:
- Open an issue
- Submit a pull request
- Share your adaptations and extensions

## 📄 License

MIT License - feel free to use these examples in your own projects!

## 👤 Author

**Lakshmi Narayanan**
- Medium: [@your-medium-username](https://medium.com/@your-username)
- GitHub: [@Laksh-star](https://github.com/Laksh-star)
- LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/your-profile)

## ⭐ Support

If you find these examples helpful, please:
- ⭐ Star this repository
- 📝 Share the companion article
- 💬 Join the discussion in the Azure AI Foundry Discord

---

**Last Updated:** October 2025  
**Framework Version:** agent-framework (preview)  
**Python Version:** 3.9+
