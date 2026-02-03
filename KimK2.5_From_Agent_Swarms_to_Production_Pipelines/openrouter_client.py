import base64
from typing import Dict, List, Optional
from openai import OpenAI
from config import Config


class KimiK25OpenRouterClient:
    """
    Kimi K2.5 client using OpenRouter API.
    """

    def __init__(self):
        if not Config.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY is not set in the environment.")
        self.client = OpenAI(
            api_key=Config.OPENROUTER_API_KEY,
            base_url=Config.OPENROUTER_BASE_URL,
        )
        self.model = Config.MODEL_INSTANT
        self.extra_headers = Config.get_extra_headers()

    def encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def _create_message_with_images(self, text: str, image_paths: List[str]) -> List[Dict]:
        content = [{"type": "text", "text": text}]
        for path in image_paths:
            base64_image = self.encode_image(path)
            content.append(
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                }
            )
        return content

    def _get_extra_body(self, mode: str = "instant") -> Optional[Dict]:
        extra_body = Config.get_provider_config().copy()
        if mode == "thinking":
            extra_body["include_reasoning"] = True
        elif mode == "agent":
            extra_body["enable_agent"] = True
        return extra_body if extra_body else None

    def analyze_frame_sequence(
        self,
        frames: List[Dict],
        context: str = "",
        max_frames: int = 10,
    ) -> Dict:
        prompt = (
            "Analyze this sequence of video frames from a tutorial in ONE coherent pass.\n\n"
            f"Context: {context}\n\n"
            "For each frame, identify:\n"
            "1. What action is being demonstrated\n"
            "2. Key UI elements or code visible\n"
            "3. The step number in the overall workflow\n"
            "4. Any UI interactions (clicks, typing, etc.)\n\n"
            "Requirements:\n"
            "- Produce a single, continuous workflow narrative (no batch stitching).\n"
            "- Maintain consistent terminology from the first frame to the last.\n"
            "- Explicitly reference early, middle, and late steps.\n"
            "- Provide a structured breakdown with numbered steps.\n"
        )

        image_paths = [f["path"] for f in frames[:max_frames]]
        messages = [
            {
                "role": "user",
                "content": self._create_message_with_images(prompt, image_paths),
            }
        ]

        extra_body = self._get_extra_body(mode="thinking")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=Config.ANALYSIS_TEMPERATURE,
            max_tokens=Config.MAX_TOKENS,
            extra_headers=self.extra_headers,
            extra_body=extra_body,
        )

        result = {
            "content": response.choices[0].message.content,
            "model": response.model,
            "usage": {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            },
        }

        if hasattr(response.choices[0].message, "reasoning"):
            result["reasoning"] = response.choices[0].message.reasoning

        return result

    def generate_code_from_description(
        self,
        step_description: str,
        previous_code: str = "",
        output_format: str = "html",
    ) -> Dict:
        prompt = (
            "Based on this tutorial step, generate complete, working code:\n\n"
            f"Step Description: {step_description}\n\n"
            f"Previous Code Context: {previous_code}\n\n"
            f"Output Format: {output_format}\n\n"
            "Requirements:\n"
            "- Generate production-ready code\n"
            "- Include comments explaining each section\n"
            "- Ensure code is fully functional and can run standalone\n"
            "- Use modern best practices\n"
            "- Add proper error handling\n\n"
            "Generate only the code with inline comments."
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=Config.CODE_GENERATION_TEMPERATURE,
            max_tokens=Config.MAX_TOKENS,
            extra_headers=self.extra_headers,
        )

        return {
            "content": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            },
        }

    def create_interactive_documentation(
        self,
        workflow_steps: str,
        code_samples: str,
    ) -> Dict:
        prompt = (
            "Create a complete, interactive HTML documentation page for this tutorial.\n\n"
            f"Workflow Steps:\n{workflow_steps}\n\n"
            f"Code Samples:\n{code_samples}\n\n"
            "Requirements:\n"
            "1. Single-page HTML with embedded CSS and JavaScript\n"
            "2. Navigation sidebar with progress tracker\n"
            "3. Step-by-step instructions with expandable sections\n"
            "4. Syntax-highlighted code blocks with copy buttons\n"
            "5. Interactive demos where applicable\n"
            "6. Responsive design (mobile-friendly)\n"
            "7. Search functionality in the sidebar\n"
            "8. Smooth scrolling between sections\n"
            "9. Code preview panels for HTML/CSS/JS\n\n"
            "Include CDNs:\n"
            "- Tailwind CSS for styling\n"
            "- Prism.js for syntax highlighting\n"
            "- Font Awesome for icons\n\n"
            "Output Rules:\n"
            "- Return ONLY a complete HTML document\n"
            "- Do NOT include code fences, explanations, or markdown\n\n"
            "Generate the complete, standalone HTML file."
        )

        extra_body = self._get_extra_body(mode="agent")

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=Config.DOCUMENTATION_TEMPERATURE,
            max_tokens=Config.DOC_MAX_TOKENS,
            extra_headers=self.extra_headers,
            extra_body=extra_body,
        )

        return {
            "content": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            },
        }

    def generate_timestamped_summary(
        self,
        frames: List[Dict],
        workflow_steps: str,
        context: str = "",
    ) -> Dict:
        timestamps = ", ".join([f"{f['index']}@{f['timestamp']:.1f}s" for f in frames])
        has_timestamps = bool(timestamps)
        prompt = (
            "Create a concise, coherent tutorial summary.\n\n"
            f"Context: {context}\n\n"
            f"{'Available frame timestamps (index@seconds): ' + timestamps + '\\n\\n' if has_timestamps else ''}"
            f"Workflow analysis:\n{workflow_steps}\n\n"
            "Requirements:\n"
            "- Produce 8-12 bullet points\n"
            f"{'- Each bullet must include a timestamp in seconds (e.g., 30s)\\n' if has_timestamps else ''}"
            f"{'- Use the provided timestamps; if uncertain, say \\'approx.\\'\\n' if has_timestamps else ''}"
            f"{'- Cover the full timeline: include at least one early, mid, and late timestamp\\n' if has_timestamps else ''}"
            "- Keep terminology consistent across the entire tutorial\n"
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=Config.SUMMARY_MAX_TOKENS,
            extra_headers=self.extra_headers,
        )

        return {
            "content": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            },
        }

    def answer_workflow_questions(
        self,
        frames: List[Dict],
        workflow_steps: str,
        code_samples: str,
        questions: List[str],
        context: str = "",
    ) -> Dict:
        timestamps = ", ".join([f"{f['index']}@{f['timestamp']:.1f}s" for f in frames])
        has_timestamps = bool(timestamps)
        question_block = "\n".join([f"- {q}" for q in questions])
        prompt = (
            "Answer the questions using the full tutorial context below.\n\n"
            f"Context: {context}\n\n"
            f"{'Available frame timestamps (index@seconds): ' + timestamps + '\\n\\n' if has_timestamps else ''}"
            f"Workflow analysis:\n{workflow_steps}\n\n"
            f"Code samples:\n{code_samples}\n\n"
            "Questions:\n"
            f"{question_block}\n\n"
            "Requirements:\n"
            "- Answer each question in 1-3 sentences\n"
            f"{'- Include a timestamp (seconds) when possible\\n' if has_timestamps else ''}"
            "- Prefer answers that reference early + late steps if relevant\n"
            "- If unsure, say what is missing\n"
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=Config.QA_MAX_TOKENS,
            extra_headers=self.extra_headers,
        )

        return {
            "content": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            },
        }

    def generate_questions_from_workflow(
        self,
        frames: List[Dict],
        workflow_steps: str,
        context: str = "",
        max_questions: int = 6,
    ) -> Dict:
        timestamps = ", ".join([f"{f['index']}@{f['timestamp']:.1f}s" for f in frames])
        has_timestamps = bool(timestamps)
        prompt = (
            "Generate a short list of useful questions about this tutorial.\n\n"
            f"Context: {context}\n\n"
            f"{'Available frame timestamps (index@seconds): ' + timestamps + '\\n\\n' if has_timestamps else ''}"
            f"Workflow analysis:\n{workflow_steps}\n\n"
            "Requirements:\n"
            f"- Write {max_questions} questions\n"
            "- Each question should be answerable from the analysis\n"
            "- Favor questions that require global context (early + mid + late steps)\n"
            f"{'- At least two questions should explicitly reference timing or sequence\\n' if has_timestamps else ''}"
            "- Return only the questions, one per line\n"
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=Config.QA_MAX_TOKENS,
            extra_headers=self.extra_headers,
        )

        return {
            "content": response.choices[0].message.content,
            "usage": {
                "prompt_tokens": getattr(response.usage, "prompt_tokens", 0),
                "completion_tokens": getattr(response.usage, "completion_tokens", 0),
                "total_tokens": getattr(response.usage, "total_tokens", 0),
            },
        }

    def test_connection(self) -> bool:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": "Say 'OpenRouter connection successful' if you can read this.",
                    }
                ],
                max_tokens=20,
                extra_headers=self.extra_headers,
            )
            print("✅ OpenRouter connection successful!")
            print(f"   Model: {response.model}")
            print(f"   Response: {response.choices[0].message.content}")
            return True
        except Exception as exc:
            print(f"❌ OpenRouter connection failed: {exc}")
            return False


if __name__ == "__main__":
    client = KimiK25OpenRouterClient()
    client.test_connection()
