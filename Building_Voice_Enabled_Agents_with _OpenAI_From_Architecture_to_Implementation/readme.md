# 🧑‍⚖️ Legal Voice Assistant (India) — Built with OpenAI Agents & Gradio

> A voice-enabled legal information agent that accepts **anonymous audio or text questions** on Indian law and responds in **text and audio** — with multilingual support.  
> ⚠️ **Disclaimer:** This tool provides general information, not legal advice.

---

## 🔧 Features

- 🎙️ Voice input using **`gpt-4o-mini-transcribe`** (OpenAI’s real-time speech-to-text)
- 🧠 Legal-specific multi-agent routing via OpenAI Agents SDK
- 🗣️ Natural responses using **`tts-1`** text-to-speech model
- 🌐 Multilingual audio output (English, Hindi, Tamil, Bengali, Telugu, Marathi)
- 📦 Gradio interface for anonymous input and feedback
- 🔐 Privacy-focused: no persistent voice data stored

---

## 🖼️ Demo UI Screenshot

![Gradio Interface](./interface_screenshot.jpeg)

---

## 🧪 Try It Yourself (Locally or via Colab)

1. **Install dependencies**
   ```bash
   pip install openai-agents gradio python-dotenv

