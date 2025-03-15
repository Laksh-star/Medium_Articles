# Beyond Assistants: Developing Autonomous Workflows with OpenAI's Agents SDK

This repository contains code examples and demonstrations for building autonomous agent-based systems using OpenAI's new Agents SDK (formerly Swarm).

## Overview

The `Medium_OpenAI_AgentsSDK_SmallBusinessAdvisor.ipynb` notebook demonstrates a practical implementation of a multi-agent system that serves as a small business advisor. This system uses OpenAI's Agents SDK to create specialized agents that can handle different aspects of business consulting:

- **Triage Agent**: Routes user inquiries to the appropriate specialized agent
- **Business FAQ Agent**: Answers common questions about business formation, taxes, and regulations
- **Startup Guide Agent**: Assists with business plan creation and initial business setup
- **Marketing Agent**: Provides marketing strategy recommendations based on business type and budget
- **Funding Agent**: Helps calculate funding needs and suggests appropriate funding options

## Features

- **Multi-agent orchestration**: Demonstrates how to create a system of specialized agents that work together
- **Seamless handoffs**: Shows how conversations can be transferred between agents while maintaining context
- **Function tools**: Uses Python functions as agent tools with automatic schema generation
- **Context management**: Implements a shared context object to maintain state across agent interactions
- **Tracing and monitoring**: Includes integration with OpenAI's tracing system for debugging and monitoring

## Requirements

- Python 3.8+
- OpenAI API key with access to GPT-4 or newer models
- Required packages:
  - `openai-agents` (OpenAI's official Agents SDK)
  - `python-dotenv` (for environment variable management)
  - `gradio` (for the web interface)
  - `pydantic` (for data modeling)
  - `nest-asyncio` (for running async code in notebook environments)

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/Laksh-star/Medium_Articles.git
   cd Medium_Articles/Beyond_Assistants_Developing_Autonomous\ Workflows_with_OpenAIs_Agents_SDK
   ```

2. Install the required packages:
   ```
   pip install openai-agents python-dotenv gradio pydantic nest-asyncio
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the same directory as the notebook
   - Add your API key to the file: `OPENAI_API_KEY=your-api-key-here`

4. Run the notebook:
   - Open the notebook in Jupyter or Google Colab
   - Execute all cells to start the Gradio interface
   - Interact with the business advisor through the provided chat interface

## Implementation Details

The notebook implementation follows these key components:

1. **Agent Creation**: Defines specialized agents with specific instructions and tools
2. **Tool Implementation**: Creates Python functions that serve as agent tools
3. **Context Management**: Implements a Pydantic model to store and manage conversation state
4. **Handoffs**: Configures agents to transfer control to other agents when appropriate
5. **User Interface**: Sets up a Gradio chat interface for user interaction

## Resources

- [OpenAI Agents SDK Documentation](https://github.com/openai/openai-agents-python)
- Article: "Beyond Assistants: Developing Autonomous Workflows with OpenAI's Agents SDK"

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

*Note: This implementation is based on OpenAI's Agents SDK and Responses API released in March 2025.*
