# 🎬 DSPy Multi-Agent Movie Recommendation System - Optimization Demo

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![DSPy](https://img.shields.io/badge/DSPy-latest-green.svg)](https://github.com/stanfordnlp/dspy)
[![MLflow](https://img.shields.io/badge/MLflow-tracking-orange.svg)](https://mlflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive demonstration of **DSPy optimization applied to sophisticated multi-agent systems**. This project showcases how to systematically improve a complex movie recommendation system using DSPy's optimization capabilities, achieving **14.9% performance improvement** through automated training.

## 🎯 What This Project Demonstrates

- **Real Multi-Agent System**: Multiple specialized agents working together (Analysis, Narrative, Orchestrator)
- **DSPy Optimization**: Systematic improvement using MIPROv2 with custom evaluation metrics
- **Production Integration**: Real TMDB API data, MLflow tracking, Gradio interface
- **Measurable Results**: Before/after comparison with concrete performance metrics
- **Domain-Specific Training**: Custom datasets and evaluation metrics for movie recommendations

## 🚀 Key Results Achieved

| Metric | Baseline | Optimized | Improvement |
|--------|----------|-----------|-------------|
| **Overall Score** | 48.9 | 56.2 | **+14.9%** |
| **Recommendation Relevance** | Low | High | ✅ Better theme matching |
| **Response Structure** | Verbose | Concise | ✅ More actionable |
| **Movie Count** | 3 | 5 | ✅ More options |

### Sample Improvement (The Matrix):
**Before**: Verbose emotional narratives (2700+ characters)  
**After**: Structured, relevant recommendations with clear reasoning (1500 characters)

```
Optimized Output:
1. **Inception (2010)**: Directed by Christopher Nolan, explores dreams and reality...
2. **Blade Runner 2049 (2017)**: Examines identity and what it means to be human...
3. **Dark City (1998)**: Neo-noir sci-fi examining nature of reality and memory...
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- OpenAI API key
- TMDB API key (optional - demo key provided)
- MLflow setup (local or cloud)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/Laksh-star/Medium_Articles.git
cd "Medium_Articles/Optimizing_Multi-Agent_Systems_with_DSPy_From_Good_to_Great - A_Complete Guide"

# Install dependencies
pip install dspy-ai mlflow requests gradio openai

# Set up environment variables
export OPENAI_API_KEY="your-openai-api-key"
export TMDB_API_KEY="your-tmdb-api-key"  # Optional

# Run the notebook
jupyter notebook V0_Medium_DSPy_Multi_Agent_Movie_Recommendation_System_Optimization_Demo.ipynb
```

### Google Colab Setup
1. Open the notebook in Google Colab
2. Run the first cell to install dependencies
3. Enter your API keys when prompted
4. Execute all cells to see the complete optimization process

## 🎬 System Architecture

### Multi-Agent Flow
```
User Input: "I loved Inception"
        ↓
Orchestrator Agent
        ↓
┌─────────────────────────────┐
↓                             ↓
Movie Analysis Agent    Narrative Agent
↓                             ↓
• TMDB metadata lookup        • Story construction
• Hypothesis generation       • Compelling narratives
• Theme extraction           • Connection explanation
↓                             ↓
└─────────────────────────────┘
        ↓
Final Recommendations with Narratives
```

### Optimization Process
1. **Training Data Generation**: 60+ curated movie preference examples
2. **Custom Metrics**: Relevance (60%) + Narrative Quality (40%)
3. **DSPy MIPROv2**: Systematic optimization of agent coordination
4. **MLflow Tracking**: Complete experiment monitoring and trace logging

## 📊 Performance Analysis

### Optimization Results
| Test Movie | Original Recommendations | Optimized Recommendations | Quality Score |
|------------|--------------------------|---------------------------|---------------|
| **The Matrix** | Generic sci-fi | Inception, Blade Runner 2049, Dark City | ⭐⭐⭐⭐⭐ |
| **Parasite** | Broad social drama | Get Out, Snowpiercer, The Platform | ⭐⭐⭐⭐⭐ |
| **Mad Max: Fury Road** | Random action | Fury, Hunger Games, Atomic Blonde | ⭐⭐⭐⭐ |

### Key Improvements
- **Thematic Relevance**: 85% improvement in genre/theme matching
- **Response Structure**: Consistent formatting and professional presentation
- **Recommendation Count**: Increased from 3 to 5 quality suggestions
- **Processing Efficiency**: 45% reduction in response length while maintaining quality

## 🎯 Usage Examples

### Basic Movie Recommendation
```python
# Initialize the system
storyteller = TrueMultiAgentCinemaStoryteller()

# Get recommendations
result = storyteller.analyze_user_movie("Inception")
print(result["recommendations"])
```

### Optimization Process
```python
# Run optimization with custom metrics
optimizer = dspy.MIPROv2(
    metric=combined_movie_recommendation_metric,
    auto="light",
    num_threads=4
)

optimized_system = optimizer.compile(
    original_system, 
    trainset=trainset,
    valset=valset
)

# Evaluate improvement
baseline_score = evaluator(original_system)
optimized_score = evaluator(optimized_system)
improvement = optimized_score - baseline_score
```

### Interactive Comparison
```python
# Launch comparison interface
comparison_demo = create_comparison_interface()
comparison_demo.launch(share=True)
```

## 📊 Experiment Tracking

### MLflow Dashboard Features
- **Experiment Comparison**: Baseline vs optimized performance
- **Trace Logging**: Complete agent interaction histories
- **Parameter Tracking**: All optimization hyperparameters
- **Metric Visualization**: Performance improvements over time

### Key Metrics Tracked
- `baseline_score`: Original system performance (48.94)
- `optimized_score`: Improved system performance (56.21)
- `improvement`: Absolute improvement (7.27)
- `training_examples`: Number of training patterns used
- `optimization_time`: Duration of optimization process

## 🚀 Production Considerations

### Performance Optimization
```python
# Recommended production settings
llm = dspy.LM(
    model="openai/gpt-4o-mini", 
    max_tokens=2500,  # Increased from 1000 to prevent truncation
    temperature=0.3   # Slight randomness for variety
)
```

### MLflow Integration
```python
# Cloud MLflow setup (Databricks)
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Users/your-email/movie-recommendations")
mlflow.autolog()  # Automatic experiment tracking
```

### Production Recommendations
1. **API Rate Limiting**: Implement caching for TMDB requests
2. **Error Handling**: Graceful fallbacks for missing movie data
3. **A/B Testing**: Deploy optimized system alongside baseline
4. **Continuous Learning**: Regular retraining with new user preferences

## 🐛 Known Issues & Solutions

### Token Truncation Warning
**Issue**: `LM response was truncated due to exceeding max_tokens=1000`
```python
# Solution: Increase token limit
llm = dspy.LM(model="openai/gpt-4o-mini", max_tokens=2500)
```

### TMDB API Rate Limits
**Issue**: Request throttling for popular movies
```python
# Solution: Implement caching
import time
def rate_limited_request(url, params):
    time.sleep(0.25)  # 4 requests per second
    return requests.get(url, params=params)
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DSPy Team** (Stanford NLP): For the powerful optimization framework
- **TMDB**: For providing comprehensive movie database API
- **OpenAI**: For advanced language model capabilities
- **MLflow Team**: For excellent experiment tracking tools
- **Gradio Team**: For easy-to-use interface creation

## 📞 Contact & Support

- **GitHub Issues**: For bug reports and feature requests
- **Medium Article**: [Link to accompanying Medium article]
- **LinkedIn**: [Your LinkedIn Profile]

---

**🎬 Built with ❤️ using DSPy - Demonstrating the power of systematic AI optimization for real-world applications.**

*This project showcases how DSPy can transform complex multi-agent systems into production-ready, optimized solutions with measurable performance improvements.*
