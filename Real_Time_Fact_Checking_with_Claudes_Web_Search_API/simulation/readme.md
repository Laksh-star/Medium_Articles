# Real-Time Fact Checker with Claude AI

A sophisticated fact-checking system that uses Claude AI's web search capabilities to verify claims in real-time. This tool provides evidence-based verification with source citations and confidence scores.


## Features

- 🔍 **Real-time fact checking** using Claude AI's web search
- 📊 **Confidence scoring** for each verification
- 🔗 **Source citations** with URLs when available
- 🎨 **Color-coded results** (True/False/Unverified)
- 📈 **Batch processing** for multiple claims
- 💻 **Both console and HTML output** formats
- 🚀 **Async support** for better performance

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/realtime-fact-checker.git
cd realtime-fact-checker
```

2. Install required packages:
```bash
pip install anthropic asyncio aiohttp pandas plotly nest_asyncio
```

3. Set up your Anthropic API key:
```python
ANTHROPIC_API_KEY = "your-api-key-here"
```

## Quick Start

### Single Claim Check

```python
import asyncio
import nest_asyncio
nest_asyncio.apply()

# Initialize with your API key
ANTHROPIC_API_KEY = "your-api-key-here"

# Check a single claim
test_claim = "The Earth is flat"
result = asyncio.run(quick_check_with_citations(test_claim))
```

### Output Example

```
🔍 Fact-checking: The Earth is flat...
✓ Completed: FALSE (100% confidence)

======================================================================
Claim: The Earth is flat
Verdict: FALSE
Confidence: 100%

Evidence with sources:

1. NASA and space agencies worldwide have provided overwhelming evidence that Earth is a sphere
   Source: NASA
   🔗 URL: https://www.nasa.gov/...

2. Scientific consensus based on centuries of observations confirms Earth's spherical shape
   Source: Scientific American
   🔗 URL: https://www.scientificamerican.com/...
======================================================================
```

## Usage Examples

### Batch Fact Checking

```python
# Check multiple claims
test_claims = [
    "COVID-19 vaccines contain microchips",
    "The Great Wall of China is visible from space",
    "Lightning never strikes the same place twice"
]

# Run batch check
dashboard = FactCheckDashboard(ANTHROPIC_API_KEY)
for claim in test_claims:
    await dashboard.check_claim(claim)

# Display results
display_html_results(dashboard)
```

### Custom Categories

```python
# Fact check with categories
political_claims = [
    "Claim about election results",
    "Statement about policy changes"
]

science_claims = [
    "New medical breakthrough claim",
    "Climate change statistic"
]

# Check different categories
for claim in political_claims:
    await dashboard.check_claim(claim, source="Political")

for claim in science_claims:
    await dashboard.check_claim(claim, source="Science")
```

## Key Components

### 1. RealTimeFactChecker Class
- Handles Claude AI API interactions
- Performs web searches
- Parses and structures results

### 2. FactCheckDashboard Class
- Manages multiple fact checks
- Stores results
- Provides display methods

### 3. Data Classes
- `Claim`: Represents a claim to be checked
- `VerificationResult`: Contains verification results

## Configuration Options

### Advanced Search Configuration

```python
# Configure with specific domains
advanced_config = {
    "max_searches": 10,
    "allowed_domains": ["reuters.com", "apnews.com", "bbc.com"],
    "blocked_domains": ["unreliablesource.com"],
    "user_location": {
        "type": "approximate",
        "city": "New York",
        "country": "US"
    }
}
```

## Output Formats

### Console Output
- Color-coded verdicts
- Structured evidence listing
- Source citations with URLs

### HTML Output
- Interactive web display
- Clickable source links
- Visual verdict indicators

## API Response Structure

```json
{
    "verdict": "true/false/unverified",
    "confidence": 0.0-1.0,
    "evidence": [
        {
            "claim": "Evidence statement",
            "source": "Source name",
            "url": "https://..."
        }
    ],
    "summary": "Brief explanation"
}
```

## Error Handling

The system includes robust error handling for:
- API connection issues
- Malformed responses
- JSON parsing errors
- Missing data fields

## Performance Considerations

- Uses async/await for non-blocking operations
- Limits API calls to prevent overuse
- Implements token management
- Caches results when possible

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Claude AI](https://www.anthropic.com/claude) by Anthropic
- Uses Claude's web search capabilities for real-time verification

## Troubleshooting

### Common Issues

1. **"Invalid API key" error**
   - Ensure your Anthropic API key is valid
   - Check for proper formatting (no extra spaces)

2. **"No results found" for claims**
   - Try rephrasing the claim
   - Check internet connectivity
   - Ensure the claim is specific enough

3. **Incomplete URLs in results**
   - This is normal - not all sources provide public URLs
   - Official sources may not have direct links

## Future Enhancements

- [ ] GUI interface
- [ ] Historical claim tracking
- [ ] Multi-language support
- [ ] Integration with fact-checking databases
- [ ] Export reports to PDF
- [ ] Real-time monitoring of news sources

## Support

For issues or questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the troubleshooting section

---

Built with ❤️ for fighting misinformation
