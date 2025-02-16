# Claude.ai Chat Analysis Dashboard

A comprehensive Python tool for analyzing chat conversations with AI assistants, providing insights into interaction patterns, task categories, and usage statistics.

## Approach

This tool uses a pattern-based approach with regular expressions instead of complex NLP models for several reasons:

1. **Speed and Efficiency**: Pattern matching is significantly faster than loading and running NLP models.
2. **Domain-Specific Accuracy**: The patterns are specifically tuned for AI assistant interactions, capturing common dialogue patterns in Claude conversations.
3. **Transparency**: The classification rules are human-readable and easily modifiable, making it clear why conversations are classified in certain ways.
4. **Lightweight Dependencies**: No need for large model files or complex ML libraries.

While NLP could potentially provide deeper semantic understanding, our approach provides reliable classification for most common AI chat scenarios while remaining fast and maintainable.

## Features

- Task categorization and distribution analysis
- Interaction type classification (Automation, Augmentation, Collaboration)
- Activity patterns visualization (daily, hourly, weekly)
- Message length analysis
- Conversation statistics
- Interactive visualizations using matplotlib and seaborn

## Requirements

```
python >= 3.6
pandas
numpy
matplotlib
seaborn
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/chat-analysis-dashboard.git
cd chat-analysis-dashboard
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Using Sample Data
For testing or demonstration purposes, you can generate anonymized sample data:

```python
# Generate anonymized sample data
sample_df = anonymize_sample_data(df)
sample_df.to_json('sample_conversations.json', orient='records')
```

### Using Your Own Data
The tool expects two JSON files:
- `users.json`: Contains user information
- `conversations.json`: Contains the chat conversations

### Validation Samples
The tool includes functionality to save sample conversations for validation:

```python
# Save example conversations for each category
save_validation_samples(df, 'validation_samples.json')
```

This creates a JSON file with sample conversations for each task category and interaction type, useful for:
- Verifying classification accuracy
- Debugging classification rules
- Understanding how different conversations are categorized

## Data Format

### users.json
```json
[
  {
    "uuid": "user-id",
    "full_name": "User Name",
    "email_address": "user@example.com"
  }
]
```

### conversations.json
```json
[
  {
    "uuid": "conversation-id",
    "name": "Conversation Name",
    "account": {
      "uuid": "user-id"
    },
    "chat_messages": [
      {
        "uuid": "message-id",
        "sender": "human|assistant",
        "text": "Message content",
        "created_at": "timestamp",
        "files": []
      }
    ]
  }
]
```

## Analysis Components

### Task Categories
The analyzer classifies each conversation into one of these categories:

1. **Programming/Technical**: Code, debugging, APIs, development tasks
2. **Writing/Content**: Text creation, editing, summarization
3. **Analysis/Data**: Data processing, statistics, visualization
4. **Learning/Understanding**: Explanations, concepts, tutorials
5. **Business/Strategy**: Market analysis, business plans, ROI
6. **Creative/Design**: UI/UX, graphics, visual design
7. **Personal/Professional**: Career advice, resumes, skills
8. **Math/Science**: Equations, scientific concepts, proofs

### Interaction Types
Conversations are also classified by how users interact with the AI:

1. **Automation**: Direct task requests and straightforward operations
2. **Augmentation**: Learning and assistance requests ("help me", "explain")
3. **Collaboration**: Interactive problem-solving ("let's", "together")

2. **Interaction Types**: Classifies interactions as:
   - Automation: Direct task requests
   - Augmentation: Learning and assistance requests
   - Collaboration: Interactive problem-solving

3. **Activity Patterns**: Visualizes usage patterns across different time periods

4. **Message Analysis**: Provides insights into message lengths and response patterns

## Visualization Dashboard

The tool generates a comprehensive dashboard with six main visualizations:
1. Task Distribution Bar Chart
2. Interaction Types Pie Chart
3. Activity Heatmap (Hour/Day)
4. Message Length by Task Type
5. Daily Activity Timeline
6. Message Length Comparison (Human vs Assistant)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with Python's data science stack (pandas, numpy, matplotlib, seaborn)
- Inspired by the need for better understanding of human-AI interactions
