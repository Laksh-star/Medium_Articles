
# Indian Spirituality Guide - Rasa Pro Assistant

A conversational AI assistant built with Rasa Pro that provides guidance and information about Indian spirituality concepts, meditation practices, sacred texts, and spiritual disciplines.

## Features

- **Spiritual Concepts**: Learn about dharma, karma, moksha, atman, brahman, and other key concepts
- **Meditation Guidance**: Get personalized meditation instructions based on experience level and available time
- **Sacred Texts**: Explore the teachings of the Bhagavad Gita, Upanishads, Yoga Sutras, and Vedas
- **Spiritual Practices**: Receive guidance on practices like pranayama, mantra recitation, and yoga

## Setup Instructions

1. Install Rasa Pro:
   ```bash
   pip install rasa-pro
   ```

2. Set environment variables:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   export RASA_PRO_LICENSE=your_rasa_pro_license_key
   ```

3. Train the model:
   ```bash
   rasa train
   ```

4. Start the action server:
   ```bash
   rasa run actions
   ```

5. Run the Rasa server:
   ```bash
   rasa run --enable-api --cors "*"
   ```

## Project Structure

- **config.yml**: Configuration for NLU pipeline and policies
- **domain.yml**: Domain specification with intents, responses, slots, and actions
- **data/flows.yml**: Conversation flows for different spiritual topics
- **data/nlu.yml**: Training examples for the assistant's NLU model
- **actions/**: Custom actions for retrieving information from the knowledge base
- **actions/spirituality_data.py**: Knowledge base with spiritual concepts and practices

## Example Conversations

```
User: What is karma?
Bot: Karma refers to the spiritual principle of cause and effect where 
intent and actions of an individual influence their future. Good intent 
and good deeds contribute to good karma, while bad intent and bad deeds 
contribute to bad karma and suffering.

User: I want to learn meditation
Bot: What is your experience level with meditation?
User: Beginner
Bot: How much time do you have for meditation today?
User: 5 minutes
Bot: [Provides a 5-minute beginner meditation practice]
```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Built with Rasa Pro and CALM (Conversational AI with Language Models).
