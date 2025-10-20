# Arch-Router Demo

A minimal Gradio app that uses **[katanemo/Arch-Router-1.5B](https://huggingface.co/katanemo/Arch-Router-1.5B)** as a **router** to analyze user intent and forward it to the most suitable model (e.g., GPT-4o).  
Based on the idea of *preference-aligned routing* from the Arch-Router paper.  
Adapted from [tejasashinde/archRouter_simulator](https://huggingface.co/spaces/tejasashinde/archRouter_simulator/blob/main/app.py).

---

## 🚀 Quickstart

```bash
pip install -U transformers gradio openai torch accelerate
```

**Set your OpenAI key:**

```bash
export OPENAI_API_KEY="sk-..."
```
or in Colab:
```python
from google.colab import userdata
userdata.set('OPENAI_API_KEY', 'sk-...')
```

**Run the app:**
```bash
python app.py
```

Then open the Gradio link shown in your terminal.

---

## ⚙️ What It Does
1. Uses Arch-Router-1.5B to classify your query (e.g., “Write a poem” → `creative_writing`).
2. Maps that route to a backend model via:
   ```python
   ROUTE_TO_MODEL = {
     "code_generation": "gpt-4o",
     "creative_writing": "gpt-4o",
     "casual_conversation": "gpt-4o-mini",
     "math_reasoning": "gpt-4o",
     "other": "gpt-4o-mini"
   }
   ```
3. Sends your prompt to that model and displays the final response.

---

## 💡 Example Prompts
- “Write Python code for a calculator.”  
- “Compose a haiku about the ocean.”  
- “Solve 2x + 5 = 15.”  
- “Explain recursion in simple terms.”

---

## 🧩 References
- [Arch-Router: Aligning LLM Routing with Human Preferences (arXiv 2506.16655)](https://arxiv.org/abs/2506.16655v1)  
- [katanemo/Arch-Router-1.5B on Hugging Face](https://huggingface.co/katanemo/Arch-Router-1.5B)  
- [ArchGW: Smart Gateway for Agents](https://github.com/katanemo/archgw)  
- [ArchRouter Simulator on Hugging Face Spaces](https://huggingface.co/spaces/tejasashinde/archRouter_simulator)

---

📜 Licensed under MIT (feel free to adapt for your experiments).

