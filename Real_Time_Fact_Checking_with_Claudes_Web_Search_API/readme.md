# Real-time Fact Checker with Claude

A Python-based real-time fact-checking system that leverages Anthropic's Claude AI with web search capabilities to verify claims and statements. This tool is especially useful for journalists, researchers, and newsrooms who need quick, reliable fact verification.


## Features

- **Real-time fact checking**: Verify claims instantly using Claude's web search capabilities
- **Confidence scoring**: Get confidence levels for each verification result
- **Evidence collection**: Retrieve sources and citations for each claim
- **Color-coded results**: Visual indicators for verified, false, and unverified claims
- **HTML dashboard display**: Professional presentation of fact-checking results
- **Asynchronous processing**: Check multiple claims efficiently

## Prerequisites

- Python 3.8 or higher
- Anthropic API key
- Internet connection for web search functionality

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/realtime-fact-checker.git
cd realtime-fact-checker
```

2. Install required dependencies:
```bash
pip install anthropic asyncio nest_asyncio IPython
```

3. Set up your Anthropic API key:
```python
ANTHROPIC_API_KEY = "your-api-key-here"
```

## Usage

### Basic Usage

```python
from fact_checker import quick_check_with_citations
import asyncio

# Check a single claim
claim = "The Earth is flat"
result = asyncio.run(quick_check_with_citations(claim))
```

### Advanced Usage with Dashboard

```python
from fact_checker import FactCheckDashboard, display_html_results
import asyncio

# Initialize dashboard
dashboard = FactCheckDashboard(ANTHROPIC_API_KEY)

# Check multiple claims
claims = [
    "The Great Wall of China is visible from space",
    "Vaccines cause autism",
    "Lightning never strikes the same place twice"
]

async def check_multiple_claims():
    for claim in claims:
        await dashboard.check_claim(claim)
    display_html_results(dashboard)

asyncio.run(check_multiple_claims())
```

## Core Components

### 1. RealTimeFactChecker
The main fact-checking engine that:
- Interfaces with Claude's web search API
- Parses and validates responses
- Handles error cases gracefully

### 2. FactCheckDashboard
A wrapper that:
- Manages multiple fact-checking operations
- Stores results for display
- Provides a clean interface for batch processing

### 3. Data Classes
- `Claim`: Represents a claim to be verified
- `VerificationResult`: Contains verification results, evidence, and metadata

## Output Format

The system provides results in three formats:

1. **Console Output**: Color-coded text with verdict and confidence
2. **JSON Format**: Structured data for programmatic use
3. **HTML Dashboard**: Rich visual display for web interfaces

### Example Output

```
======================================================================
Claim: The Earth is flat
Verdict: FALSE
Confidence: 100%

Evidence with sources:

1. The Earth is not flat; it is a sphere (oblate spheroid)
   Source: NASA
   🔗 URL: https://www.nasa.gov/earth

2. Scientific evidence from multiple sources confirms Earth's spherical shape
   Source: Scientific American
   🔗 URL: https://www.scientificamerican.com/earth-shape
======================================================================
```

## Customization

### Modify Verification Behavior

```python
class CustomFactChecker(RealTimeFactChecker):
    def __init__(self, api_key: str, max_searches: int = 5):
        super().__init__(api_key)
        self.max_searches = max_searches
    
    # Override methods as needed
```

### Custom Display Formats

```python
def custom_display(result):
    # Implement your own display logic
    print(f"Custom format: {result.verdict}")
```

## Limitations

- Requires active internet connection
- API rate limits apply based on your Anthropic plan
- Results depend on available web sources
- May not work for highly specialized or technical claims without proper context

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Anthropic for providing the Claude API
- The open-source community for inspiration and support

## Disclaimer

This tool is designed to assist in fact-checking but should not be the sole source of truth. Always verify critical information through multiple sources and expert consultation when necessary.

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

---

**Note**: This tool uses Anthropic's Claude AI model (version 3.7 Sonnet) with web search capabilities. Ensure you comply with Anthropic's usage policies and terms of service.
