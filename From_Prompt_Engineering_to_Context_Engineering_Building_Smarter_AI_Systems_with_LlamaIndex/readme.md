# From Prompt Engineering to Context Engineering: Building Smarter AI Systems with LlamaIndex

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-Latest-green)](https://www.llamaindex.ai/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-orange)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A comprehensive demonstration of **Context Engineering** techniques using LlamaIndex - moving beyond simple prompt engineering to build intelligent, multi-source research assistants that can intelligently select, order, and compress contextual information.

## 🎯 What is Context Engineering?

Context Engineering is the practice of intelligently managing the contextual information provided to Large Language Models (LLMs). Unlike prompt engineering which focuses on how to ask questions, context engineering focuses on:

- **What information** to include in the context
- **How to order** information by relevance and importance  
- **How to compress** information to fit within token limits
- **Which sources** to prioritize for different query types
- **How to synthesize** information from multiple sources

## 🚀 Features

### Intelligent Source Selection
- **Query Analysis**: Automatically determines the most relevant source types based on query content
- **Multi-Source Support**: Academic papers (arXiv), news articles, Wikipedia, financial data, and web content
- **Dynamic Source Scoring**: Matches query intent with source capabilities

### Advanced Context Management
- **Context Window Optimization**: Intelligent fitting of information within token limits
- **Document Compression**: Preserves key information while reducing token usage
- **Priority-Based Ordering**: Orders content by relevance, recency, and source authority
- **Multi-Dimensional Scoring**: Combines relevance, recency, priority, and diversity scores

### Real-Time Visualization
- **Context Engineering Metrics**: Visual representation of the entire process
- **Source Distribution Analysis**: See how different sources contribute to your research
- **Performance Comparisons**: Naive vs. engineered approach comparisons
- **Context Utilization Tracking**: Monitor token usage and compression ratios

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (optional - demo mode available without)
- Internet connection for real-time data retrieval

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Laksh-star/Medium_Articles.git
cd Medium_Articles/From_Prompt_Engineering_to_Context_Engineering_Building_Smarter_AI_Systems_with_LlamaIndex
```

2. **Install required packages**:
```bash
pip install llama-index
pip install llama-index-llms-openai
pip install llama-index-embeddings-openai
pip install llama-index-readers-web
pip install llama-index-readers-wikipedia
pip install newspaper3k
pip install arxiv
pip install yfinance
pip install matplotlib seaborn
pip install wikipedia
```

3. **Set up OpenAI API key** (optional):
```python
# In the notebook/script, replace:
OPENAI_API_KEY = "your-openai-api-key-here"
# With your actual OpenAI API key from: https://platform.openai.com/api-keys
```

**Note**: The demo includes a fallback mode that works without an OpenAI API key for educational purposes.

## 📖 Usage

### Option 1: Automated Demo
Run the complete demonstration with 3 predefined queries:

```python
python medium_context_engineering_demo_llamaindex.py
# Choose option 1 when prompted
```

### Option 2: Interactive Demo
Test with your own custom queries:

```python
python medium_context_engineering_demo_llamaindex.py
# Choose option 2 when prompted
# Enter your research questions interactively
```

### Option 3: Jupyter Notebook
Open and run the `.ipynb` file in Jupyter Lab/Notebook for step-by-step exploration.

## 🏗️ Architecture Overview

```
Query Input
     ↓
┌─────────────────────────┐
│  Intelligent Source     │
│  Selection Engine       │
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  Multi-Source           │
│  Data Retrieval         │
│  • Academic (arXiv)     │
│  • News APIs            │
│  • Wikipedia            │
│  • Financial Data       │
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  Context Ordering       │
│  Engine                 │
│  • Relevance Scoring    │
│  • Recency Weighting    │
│  • Priority Assignment  │
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  Context Window         │
│  Management             │
│  • Token Optimization   │
│  • Intelligent         │
│    Compression          │
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│  LLM Response           │
│  Generation             │
└─────────────────────────┘
```

## 📊 Key Components

### 1. ContextualDocument Class
Enhanced document representation with metadata:
- Source type classification
- Priority levels
- Timestamp tracking
- Relevance scoring
- Token count estimation

### 2. IntelligentSourceSelector
Analyzes queries to determine optimal source types:
```python
selector = IntelligentSourceSelector()
sources = selector.analyze_query("renewable energy trends")
# Returns: [SourceType.NEWS, SourceType.ACADEMIC, SourceType.FINANCIAL]
```

### 3. Multi-Source Retrievers
- **AcademicRetriever**: Fetches research papers from arXiv
- **NewsRetriever**: Gets current news articles  
- **WikipediaRetriever**: Provides background context
- **FinancialRetriever**: Adds economic data and market context

### 4. Context Engineering Engines
- **ContextOrderingEngine**: Implements sophisticated document ranking
- **ContextCompressionEngine**: Intelligently reduces content while preserving key information

## 📈 Demo Queries

The automated demo includes these sample queries that showcase different aspects of context engineering:

1. **"renewable energy adoption trends"**
   - Demonstrates multi-source synthesis (news + academic + financial)
   - Shows recency weighting for trend analysis

2. **"artificial intelligence market analysis"**  
   - Highlights intelligent source selection
   - Showcases financial data integration

3. **"climate change economic impact"**
   - Illustrates academic paper prioritization
   - Shows context compression techniques

## 🔍 Understanding the Output

Each demo run provides:

### Context Engineering Metrics
- **Source Selection**: Which source types were chosen and why
- **Document Retrieval**: Number of documents from each source
- **Context Ordering**: Relevance scores and ranking decisions
- **Token Management**: Context window utilization and compression ratios

### Visualizations
- **Source Distribution**: Pie chart of document sources
- **Relevance Scoring**: Bar chart of document rankings
- **Context Utilization**: Token usage optimization
- **Compression Impact**: Before/after comparison

### Performance Comparison
- **Naive Approach**: Single-source (Wikipedia only) baseline
- **Engineered Approach**: Multi-source, optimized context
- **Improvement Metrics**: Quantified benefits of context engineering

## 🎓 Educational Value

This demo teaches:

### Core Concepts
- **Context vs. Prompt Engineering**: Understanding the distinction and when to use each
- **Information Retrieval**: Multi-source data gathering strategies
- **Relevance Scoring**: Algorithmic approaches to content ranking
- **Token Economics**: Managing LLM context window constraints

### Practical Skills
- **LlamaIndex Usage**: Real-world RAG implementation patterns
- **API Integration**: Working with multiple data sources simultaneously
- **Performance Optimization**: Balancing quality vs. efficiency
- **System Design**: Building scalable AI research assistants

### Advanced Techniques
- **Dynamic Source Selection**: Query-dependent retrieval strategies
- **Context Compression**: Lossy compression while preserving key information
- **Multi-dimensional Scoring**: Balancing competing factors (recency, relevance, authority)
- **Visualization**: Making AI decision processes transparent

## 🔧 Customization

### Adding New Sources
Extend the system by implementing new retrievers:

```python
class CustomRetriever:
    def search(self, query: str, max_results: int = 3) -> List[ContextualDocument]:
        # Your custom retrieval logic
        pass

# Register in the assistant
assistant.retrievers[SourceType.CUSTOM] = CustomRetriever()
```

### Modifying Scoring Algorithms
Adjust the context ordering weights:

```python
ordering_engine = ContextOrderingEngine()
ordering_engine.recency_weight = 0.4  # Increase recency importance
ordering_engine.relevance_weight = 0.3  # Decrease relevance weight
```

### Custom Compression Strategies
Implement domain-specific compression:

```python
class DomainSpecificCompressor(ContextCompressionEngine):
    def compress_document(self, doc: ContextualDocument, target_length: int):
        # Your custom compression logic
        pass
```

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- **New Data Sources**: Add support for additional APIs and databases
- **Advanced Compression**: Implement LLM-based summarization techniques  
- **Caching Systems**: Add intelligent caching for repeated queries
- **Evaluation Metrics**: Develop benchmarks for context engineering quality
- **UI Enhancement**: Build web interfaces for easier interaction

## 📚 Related Resources

- **LlamaIndex Documentation**: [https://docs.llamaindex.ai/](https://docs.llamaindex.ai/)
- **Context Engineering Research**: Academic papers on RAG optimization
- **OpenAI API Guide**: [https://platform.openai.com/docs](https://platform.openai.com/docs)
- **Medium Article**: [Link to accompanying blog post]

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LlamaIndex Team**: For the excellent RAG framework
- **OpenAI**: For providing powerful language models
- **arXiv**: For academic paper access
- **Wikipedia**: For reliable background information
- **Open Source Community**: For the amazing tools and libraries used

## 🐛 Issues and Support

If you encounter any issues:

1. Check that all dependencies are installed correctly
2. Verify your OpenAI API key (if using)
3. Ensure internet connectivity for real-time data retrieval
4. Open an issue on GitHub with error details and reproduction steps

## ⭐ Star This Repository

If you found this demo helpful for learning context engineering concepts, please star the repository to help others discover it!

---

**Built with ❤️ for the AI/ML community**

*This demo is part of a comprehensive guide to modern AI system design, moving beyond basic prompt engineering to sophisticated context management techniques.*
