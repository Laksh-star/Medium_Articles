# 📊 ChatGPT Personal Usage Analyzer

A comprehensive tool to analyze your ChatGPT conversation data and gain insights into your AI usage patterns. Based on research methodology from *"How Do People Use ChatGPT? Analyzing User Behavior and Message Content"* by Zhang et al. (2024).

## 🔍 What This Tool Does

Analyzes your ChatGPT export data to provide insights on:

- **Work vs Personal Usage** - Classify messages as work-related or personal
- **Intent Analysis** - Categorize messages as Asking, Doing, or Expressing
- **Topic Classification** - Identify 15+ topic categories (Writing, Technical Help, etc.)
- **Usage Patterns** - Analyze when and how you use ChatGPT
- **Research Comparison** - Compare your patterns to typical ChatGPT users

## 📈 Sample Results

- Most users have ~27% work-related messages
- ~49% of messages are "Asking" for information
- Common topics: Writing (20%), Technical Help (15%), Practical Guidance (12%)
- Peak usage times vary by user but often evening hours

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)
1. **Get your ChatGPT data**:
   - Go to ChatGPT → Settings → Data Controls → Export
   - Download and extract the ZIP file
   - Locate `conversations.json`

2. **Open the notebook**:
   - Upload `ChatGPT_conversations_Sept17_2025.ipynb` to Google Colab
   - Upload your `conversations.json` file

3. **Set up OpenAI API** (optional but recommended):
   - Get API key from [platform.openai.com](https://platform.openai.com)
   - In Colab: Click 🔑 → Add secret: `OPENAI_API_KEY` = your key

4. **Run all cells** and view your results!

### Option 2: Local Python Environment
```bash
# Clone the repository
git clone <repository-url>
cd chatgpt-usage-analyzer

# Install dependencies
pip install openai pandas matplotlib seaborn numpy python-dateutil

# Set your OpenAI API key (optional)
export OPENAI_API_KEY="your-api-key-here"

# Run the analysis
python fixed_custom_format_analyzer_openai.py
```

## 📊 Analysis Methods

### Basic Analysis (Free)
- Uses keyword-based heuristics
- Good for general trends
- No API costs
- ~70-80% accuracy

### Advanced Analysis (Recommended)
- Uses OpenAI GPT models (GPT-3.5 Turbo by default for cost efficiency)
- Context-aware classification
- Research-grade accuracy
- Cost: ~$3-6 for typical analysis (~3000 messages)

## 💰 Cost Breakdown

For OpenAI API usage (advanced analysis):

| Dataset Size | Estimated Cost | Runtime |
|--------------|----------------|---------|
| < 1,000 messages | $1-2 | 2-5 minutes |
| 1,000-3,000 messages | $3-5 | 5-15 minutes |
| 3,000+ messages | $5-8 | 15-30 minutes |

**Cost calculation**: GPT-3.5 Turbo rates - $0.50 per 1M input tokens + $1.50 per 1M output tokens (as of 2025)

**💡 Cost Optimization**: We intentionally use GPT-3.5 Turbo for cost efficiency. For higher accuracy, you can upgrade to newer models:
- **GPT-4o Mini**: $0.15 per 1M input + $0.60 per 1M output (~60% cheaper than GPT-3.5)
- **GPT-4o**: More expensive but highest accuracy for complex classifications

## 📁 File Structure

```
chatgpt-usage-analyzer/
├── README.md                                    # This file
├── Medium_ChatGPT_conversations_Sept17_2025.ipynb     # Main Jupyter notebook
└── conversations.json                           # Your ChatGPT export (not included)
```

## 🔧 Technical Details

### Input Format
- **Required**: ChatGPT export file (`conversations.json`)
- **Format**: Standard ChatGPT export with `chat_messages` structure
- **Fields used**: `sender`, `content`, `created_at`, conversation metadata

### Output
- **Visualizations**: 6 charts showing usage patterns
- **Statistics**: Detailed breakdown of your usage
- **Comparison**: Your patterns vs research findings
- **Export**: Results can be saved as images or CSV

### Classification Categories

**Intent Classification**:
- **Asking**: Seeking information or advice
- **Doing**: Requesting task completion (writing, coding, etc.)
- **Expressing**: Sharing thoughts/opinions without specific requests

**Topic Categories** (15+ types):
- Writing, Technical Help, Practical Guidance
- Seeking Information, Creative, Self-Expression
- Learning, Planning, Health/Wellness
- Entertainment, Shopping/Products, Travel
- Food/Cooking, Spiritual, Career, Other

## 🛠️ Customization

### Modify Classifications
Edit the keyword lists or OpenAI prompts in the analyzer class:

```python
# Example: Add custom work-related keywords
work_keywords = ['work', 'job', 'office', 'meeting', 'your-custom-terms']

# Example: Modify topic categories
topics = {
    'Your Custom Topic': ['keyword1', 'keyword2'],
    # ... existing topics
}
```

### Adjust Analysis Parameters
```python
# Analyze all messages (default samples 500 for speed)
analyzer.classify_messages(sample_size=None)

# Use different OpenAI models for better accuracy (higher cost)
analyzer = FixedCustomFormatAnalyzer(api_key="your-key", model="gpt-4o-mini")  # Cheaper option
analyzer = FixedCustomFormatAnalyzer(api_key="your-key", model="gpt-4o")       # Highest accuracy

# Note: The default model is gpt-3.5-turbo for cost efficiency
```

## 🔒 Privacy & Security

- **Local Processing**: Your data stays on your machine/Colab instance
- **API Usage**: Only message content sent to OpenAI for classification (if using advanced mode)
- **No Storage**: No conversation data is permanently stored by this tool
- **Optional**: You can use heuristic mode to avoid any external API calls

## 🐛 Troubleshooting

### Common Issues

**"No messages extracted"**
- Check if your `conversations.json` file is from ChatGPT (not Claude, etc.)
- Verify the file isn't corrupted
- Try the debug cell to inspect your data format

**"OpenAI API error"**
- Verify your API key is correct
- Check you have sufficient credits in your OpenAI account
- The tool will fall back to heuristics if API fails

**"Rate limit exceeded"**
- The tool includes automatic retry logic
- For large datasets, consider using `sample_size` parameter
- You can resume interrupted analysis

**Memory issues**
- Use `sample_size` parameter for large datasets
- In Colab: Runtime → Factory reset runtime

## 📚 Research Background

This tool implements the methodology from:

> Zhang, Y., et al. (2024). "How Do People Use ChatGPT? Analyzing User Behavior and Message Content." *Conference on AI and Society*.

**Key findings from the research**:
- 27% of messages are work-related on average
- 49% are "Asking" type interactions
- Writing and Technical Help are most common topics
- Usage patterns vary significantly by profession and use case

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional topic categories
- Support for other AI chat exports (Claude, Bard, etc.)
- Advanced visualization options
- Batch processing for multiple users
- Web interface

## 📄 License

MIT License - feel free to use and modify for personal or research purposes.

## 🙏 Acknowledgments

- Research team behind the original ChatGPT usage study
- OpenAI for providing classification API
- Google Colab for accessible compute environment

---

**Questions?** Open an issue on GitHub or check existing discussions.

**Privacy note**: This tool is designed for personal insight and research purposes. Always review any data you share or publish to ensure it meets your privacy requirements.
