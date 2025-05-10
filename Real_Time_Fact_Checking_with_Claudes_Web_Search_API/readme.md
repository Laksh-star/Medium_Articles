# Real-time Fact Checking Tools

A comprehensive suite of fact-checking tools powered by Anthropic's Claude AI, designed for journalists, researchers, and newsrooms to verify claims and combat misinformation in real-time.

## Project Structure

This repository contains two main components:

### 1. Basic Fact Checker (`basic_fact_checker/`)
A straightforward implementation for general-purpose fact checking. Features include:
- Real-time claim verification using Claude's web search capabilities
- Confidence scoring and evidence collection
- Color-coded console output for quick visual assessment
- HTML dashboard for professional presentation
- Support for single and batch claim processing

**Use case**: General fact-checking for news articles, social media posts, public statements, etc.

### 2. Conflict Monitoring Simulation (`simulation/`)
A specialized system for monitoring and fact-checking claims in conflict zones, demonstrated with an India-Pakistan border situation scenario. Features include:
- Advanced claim extraction from breaking news
- Multi-source verification (Indian, Pakistani, and neutral sources)
- Priority-based claim processing
- Real-time dashboard with broadcast advisories
- Historical pattern analysis
- Comprehensive reporting for newsrooms

**Use case**: Real-time monitoring of conflict situations, breaking news verification, broadcast journalism support.

## Key Features

- **AI-Powered Verification**: Leverages Claude 3.7 Sonnet's advanced reasoning capabilities
- **Web Search Integration**: Real-time access to current information for verification
- **Multi-Source Validation**: Cross-references multiple sources for accuracy
- **Visual Indicators**: Color-coded results for quick decision-making
- **Professional Reporting**: Export-ready results for broadcast and publication

## Getting Started

Each subfolder contains its own detailed documentation. Choose based on your needs:

- For general fact-checking: See [`basic_fact_checker/README.md`](basic_fact_checker/README.md)
- For conflict monitoring: See [`simulation/README.md`](simulation/README.md)

## Prerequisites

- Python 3.8+
- Anthropic API key
- Required Python packages (see individual project requirements)

## Quick Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/fact-checking-tools.git
cd fact-checking-tools

# Navigate to your chosen tool
cd basic_fact_checker  # or cd simulation

# Install dependencies
pip install -r requirements.txt
```

## Applications

- **Newsrooms**: Real-time verification for breaking news
- **Social Media**: Combat misinformation and verify viral claims
- **Research**: Academic fact-checking and data validation
- **Conflict Monitoring**: Track and verify claims in sensitive situations
- **Public Relations**: Verify statements and press releases


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Anthropic for providing the Claude API
- The journalism and fact-checking community for inspiration
- Open-source contributors

---

**Note**: These tools are designed to assist in fact-checking but should complement, not replace, professional journalistic judgment and additional verification processes.
