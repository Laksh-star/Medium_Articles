# 🎤 LiveKit Voice Agent with RAG

*Production-ready AI voice assistant that only answers from your custom knowledge base.*

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laksh-star/Medium_Articles/blob/main/From_Speech_to_Action_Building_Production-Ready_AI_Voice_Agents_in_2025/livekit_rag_voice_agent.ipynb)

## ✨ Features

- 🎙️ **Real-time voice interaction** with LiveKit
- 📚 **Custom knowledge base** from your text files  
- 🚫 **Knowledge-only responses** - no hallucination
- 🔊 **High-quality TTS** with ElevenLabs/OpenAI

## 🚀 Quick Start

### 1. Get API Keys
- [OpenAI API Key](https://platform.openai.com/api-keys)
- [LiveKit Account](https://cloud.livekit.io/) (URL, API Key, Secret)
- [ElevenLabs Key](https://elevenlabs.io/) (optional)

### 2. Run in Colab
1. Click the Colab badge above
2. Add your API keys to the configuration section
3. Upload your `.txt` files (optional - uses samples if none provided)
4. Run the code cell

### 3. Talk to Your Agent
- Unmute the microphone in the interface
- Ask questions about your uploaded content
- Agent only answers from your knowledge base

## 📝 Usage Examples

**✅ Will Answer** (if in your files):
- "What is our company policy?"
- "How do I reset my password?"

**❌ Will Refuse** (not in knowledge base):
- "What's the weather today?"
- "Tell me about quantum computing"

## 🔧 Custom Knowledge Files

```python
# Upload your .txt files to Colab, then:
!cp /content/*.txt /content/rag_data/
```

The agent will automatically use your files instead of samples.

## ⚡ How It Works

1. **Upload** your text files → **Index** with LlamaIndex → **Search** on questions → **Voice response**
2. Agent **must** search knowledge base for every question
3. If no relevant info found → "I don't have that information"

## 🎛️ Customization

**Change Voice:**
```python
tts = elevenlabs.TTS(voice_id="CwhRBWXzGAHq8TQ4Fs17")  # Roger
```

**Available Voices:** Roger, Sarah, Laura, George (see code for IDs)

## 🐛 Troubleshooting

**Microphone not working?**
- Allow mic permissions for colab.research.google.com
- Try Chrome/Firefox (Safari has issues)
- Check address bar for mic icon

**Agent not responding?**
- Verify all API keys are set correctly
- Check console for "RAG ready" message
- Ensure knowledge files are uploaded

## 🤝 Contributing

Issues and PRs welcome at [Medium_Articles repo](https://github.com/Laksh-star/Medium_Articles).

## 📰 Article

Read the full tutorial: ["From Speech to Action: Building Production-Ready AI Voice Agents in 2025"](https://medium.com/@your-medium-handle)

---

⭐ [Star the repo](https://github.com/Laksh-star/Medium_Articles) if this helped you!
