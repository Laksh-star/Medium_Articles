# 🎤 LiveKit Voice Agent with RAG Integration

*From the Medium Article: "From Speech to Action: Building Production-Ready AI Voice Agents in 2025"*

A powerful voice-activated AI assistant that runs in Google Colab and only answers questions from your custom knowledge base using Retrieval-Augmented Generation (RAG).

## ✨ Features

- 🎙️ **Real-time voice interaction** using LiveKit agents
- 🧠 **Custom knowledge base** - upload your own text files
- 🚫 **Knowledge-only responses** - agent ONLY answers from your uploaded documents
- 🔊 **High-quality voice synthesis** with ElevenLabs or OpenAI TTS
- 📱 **Browser-based interface** - works directly in Google Colab
- 🔍 **Intelligent search** using LlamaIndex for document retrieval

## 🛠️ Requirements

### API Keys (Required)
- **OpenAI API Key** - for LLM and STT/TTS
- **LiveKit Account** - for real-time voice communication
  - LiveKit URL
  - LiveKit API Key  
  - LiveKit API Secret
- **ElevenLabs API Key** (Optional) - for premium voice synthesis

### Dependencies
All dependencies are automatically installed in the Colab environment:
- `livekit-agents`
- `llama-index`
- `openai`
- `elevenlabs` (optional)

## 🚀 Quick Start

### 1. Open in Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Laksh-star/Medium_Articles/blob/main/From_Speech_to_Action_Building_Production-Ready_AI_Voice_Agents_in_2025/livekit_rag_voice_agent.ipynb)

### 2. Set Up API Keys
Replace the placeholder values in the code:

```python
os.environ['OPENAI_API_KEY'] = 'your-openai-api-key-here'
os.environ['ELEVENLABS_API_KEY'] = 'your-elevenlabs-api-key-here'  # Optional
os.environ['LIVEKIT_URL'] = 'wss://your-project.livekit.cloud'
os.environ['LIVEKIT_API_KEY'] = 'your-livekit-api-key'
os.environ['LIVEKIT_API_SECRET'] = 'your-livekit-api-secret'
```

### 3. Upload Your Knowledge Files (Optional)
- Click the folder icon in Colab's left sidebar
- Upload your `.txt` files containing the knowledge you want the agent to have
- Run this command to move them to the RAG directory:
```python
!cp /content/*.txt /content/rag_data/
```

### 4. Run the Agent
Execute the main code cell. You'll see:
```
🚀 Starting your working notebook + RAG...
🧠 Now with knowledge about your uploaded documents!
```

### 5. Start Talking
- **Unmute** the microphone icon in the interface
- Start with a long phrase like "Hello, how are you today?"
- Ask questions about your uploaded documents

## 📚 How It Works

1. **Document Processing**: Your text files are processed and indexed using LlamaIndex
2. **Voice Input**: Your speech is converted to text using OpenAI's Whisper
3. **Knowledge Search**: The agent searches your documents for relevant information
4. **Response Generation**: Only information from your documents is used to generate responses
5. **Voice Output**: The response is converted back to speech using ElevenLabs or OpenAI TTS

## 🎯 Usage Examples

### ✅ Questions That Should Work
(If you have relevant content in your uploaded files)
- "What is our company policy on remote work?"
- "How do I reset my password?"
- "What are the key features of our product?"
- "Who should I contact for technical support?"

### ❌ Questions That Will Be Refused
(Information not in your knowledge base)
- "What's the weather today?"
- "Tell me about quantum computing" (unless in your files)
- "What's the latest news?"

## 🔧 Customization

### Change Voice
Modify the voice by updating the TTS configuration:
```python
tts = elevenlabs.TTS(voice_id="CwhRBWXzGAHq8TQ4Fs17")  # Roger
```

Available ElevenLabs voices:
- Roger: `CwhRBWXzGAHq8TQ4Fs17`
- Sarah: `EXAVITQu4vr4xnSDxMaL`
- Laura: `FGY2WhTYpPnrIDTdsKH5`
- George: `JBFqnCBsd6RMkjVDRZzb`

### Modify Instructions
Update the agent's behavior by editing the instructions:
```python
instructions="""
    Your custom instructions here...
    You MUST use search_knowledge for every question.
    Only answer from the knowledge base.
"""
```

## 🔍 Troubleshooting

### Microphone Not Working
1. **Check browser permissions** - allow microphone access for colab.research.google.com
2. **Try a different browser** - Chrome and Firefox work best
3. **Check the address bar** for microphone icon and click "Allow"

### Agent Not Responding
1. **Verify API keys** are correctly set
2. **Check LiveKit connection** - you should see "livekit-rtc connected"
3. **Ensure knowledge base loaded** - look for "RAG ready with X documents"

### No Knowledge Found
1. **Upload text files** to `/content/rag_data/` directory
2. **Check file format** - only `.txt` files are supported
3. **Verify content** - files should contain readable text

## 🏗️ Architecture

```
User Speech → OpenAI Whisper → RAG Search → OpenAI GPT-4 → ElevenLabs → Voice Output
                                    ↓
                            LlamaIndex Vector Store
                                    ↓
                            Your Uploaded Documents
```

## 📁 File Structure

### Repository Structure
```
From_Speech_to_Action_Building_Production-Ready_AI_Voice_Agents_in_2025/
├── livekit_rag_voice_agent.ipynb # Main notebook  
├── README.md                      # This file
├── requirements.txt               # Dependencies
└── sample_knowledge/              # Example knowledge files
    ├── ai_basics.txt
    └── python_info.txt
```

### Runtime Structure (in Google Colab)
```
/content/
├── rag_data/                      # Your uploaded knowledge files
│   ├── document1.txt
│   ├── document2.txt
│   └── ...
└── (notebook files...)
```

## 🤝 Contributing

1. Fork this repository: [Medium_Articles](https://github.com/Laksh-star/Medium_Articles)
2. Navigate to the voice agent folder: `From_Speech_to_Action_Building_Production-Ready_AI_Voice_Agents_in_2025/`
3. Create a feature branch (`git checkout -b feature/amazing-feature`)
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📰 Related Medium Article

Read the full tutorial: **["From Speech to Action: Building Production-Ready AI Voice Agents in 2025"](https://medium.com/@your-medium-handle)**

*This repository contains the complete working code from the article.*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LiveKit](https://livekit.io/) for the real-time communication framework
- [LlamaIndex](https://www.llamaindex.ai/) for the RAG implementation
- [OpenAI](https://openai.com/) for language models and speech processing
- [ElevenLabs](https://elevenlabs.io/) for high-quality voice synthesis

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Open an issue on the [Medium_Articles repository](https://github.com/Laksh-star/Medium_Articles/issues)
3. Make sure all API keys are valid and have sufficient credits

## 🔗 More Projects

Check out other articles and projects in the [Medium_Articles repository](https://github.com/Laksh-star/Medium_Articles):
- AI and Machine Learning tutorials
- Production-ready code examples
- Latest tech implementations

---

⭐ **Star the [main repo](https://github.com/Laksh-star/Medium_Articles)** if you found this helpful!

🔗 **Share** with others who might benefit from a voice-activated knowledge assistant!
