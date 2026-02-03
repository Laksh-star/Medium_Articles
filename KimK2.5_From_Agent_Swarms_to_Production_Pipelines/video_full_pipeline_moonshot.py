import argparse
import base64
import json
import os
import re
from pathlib import Path

from openai import OpenAI


def _extract_code(content: str) -> str:
    fenced = re.findall(r"```(?:\w+)?\n(.*?)```", content, re.DOTALL)
    if fenced:
        return fenced[0].strip()
    return content.strip()


def _extract_html(content: str) -> str:
    text = content.strip()
    if not text:
        return "<!doctype html>\n<html><body><pre></pre></body></html>"
    fenced = re.findall(r"```(?:html)?\n(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if fenced:
        return fenced[0].strip()
    if text.startswith("```html") or text.startswith("```"):
        text = re.sub(r"^```(?:html)?\n?", "", text, flags=re.IGNORECASE).strip()
    text = re.sub(r"\n?```$", "", text).strip()
    if "<html" in text.lower():
        return text
    return f"<!doctype html>\n<html><body><pre>{text}</pre></body></html>"


def _parse_steps(workflow_text: str) -> list:
    steps = []
    lines = [line.strip() for line in workflow_text.splitlines() if line.strip()]
    numbered_pattern = re.compile(r"^(?:step\s*)?(\d+)[\).\:\-]\s+(.*)$", re.IGNORECASE)
    for line in lines:
        match = numbered_pattern.match(line)
        if match:
            steps.append(match.group(2).strip())
    if steps:
        return steps
    paragraphs = [p.strip() for p in workflow_text.split("\n\n") if p.strip()]
    if paragraphs:
        return paragraphs
    return lines


def _client() -> OpenAI:
    api_key = os.environ.get("MOONSHOT_API_KEY")
    if not api_key:
        raise ValueError("MOONSHOT_API_KEY is not set in the environment.")
    return OpenAI(api_key=api_key, base_url="https://api.moonshot.ai/v1")


def _video_to_data_url(video_path: Path) -> str:
    video_data = video_path.read_bytes()
    ext = video_path.suffix.lstrip(".") or "mp4"
    return f"data:video/{ext};base64,{base64.b64encode(video_data).decode('utf-8')}"


def analyze_video(client: OpenAI, video_path: Path, prompt: str) -> str:
    video_url = _video_to_data_url(video_path)
    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[
            {"role": "system", "content": "You are Kimi."},
            {
                "role": "user",
                "content": [
                    {"type": "video_url", "video_url": {"url": video_url}},
                    {"type": "text", "text": prompt},
                ],
            },
        ],
    )
    return completion.choices[0].message.content or ""


def generate_summary(client: OpenAI, analysis: str, context: str) -> str:
    prompt = (
        "Create a concise, coherent tutorial summary.\n\n"
        f"Context: {context}\n\n"
        f"Workflow analysis:\n{analysis}\n\n"
        "Requirements:\n"
        "- Produce 8-12 bullet points\n"
        "- Keep terminology consistent across the entire tutorial\n"
    )
    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=1200,
    )
    return completion.choices[0].message.content or ""


def generate_questions(client: OpenAI, analysis: str, context: str, max_q: int) -> list:
    prompt = (
        "Generate a short list of useful questions about this tutorial.\n\n"
        f"Context: {context}\n\n"
        f"Workflow analysis:\n{analysis}\n\n"
        "Requirements:\n"
        f"- Write {max_q} questions\n"
        "- Each question should be answerable from the analysis\n"
        "- Favor questions that require global context (early + mid + late steps)\n"
        "- Return only the questions, one per line\n"
    )
    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=800,
    )
    return [line.strip() for line in (completion.choices[0].message.content or "").splitlines() if line.strip()]


def answer_questions(client: OpenAI, analysis: str, questions: list, context: str) -> str:
    question_block = "\n".join([f"- {q}" for q in questions])
    prompt = (
        "Answer the questions using the full tutorial context below.\n\n"
        f"Context: {context}\n\n"
        f"Workflow analysis:\n{analysis}\n\n"
        "Questions:\n"
        f"{question_block}\n\n"
        "Requirements:\n"
        "- Answer each question in 1-3 sentences\n"
        "- Prefer answers that reference early + late steps if relevant\n"
        "- If unsure, say what is missing\n"
    )
    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=1200,
    )
    return completion.choices[0].message.content or ""


def generate_code_samples(client: OpenAI, analysis: str, max_steps: int) -> list:
    steps = _parse_steps(analysis)
    code_samples = []
    for i, step in enumerate(steps[:max_steps], 1):
        prompt = (
            "Based on this tutorial step, generate complete, working code:\n\n"
            f"Step Description: {step}\n\n"
            f"Previous Code Context: {code_samples[-1]['code'] if code_samples else ''}\n\n"
            "Output Format: html\n\n"
            "Requirements:\n"
            "- Generate production-ready code\n"
            "- Include comments explaining each section\n"
            "- Ensure code is fully functional and can run standalone\n"
            "- Use modern best practices\n"
            "- Add proper error handling\n\n"
            "Generate only the code with inline comments."
        )
        completion = client.chat.completions.create(
            model="kimi-k2.5",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=2000,
        )
        code_samples.append(
            {
                "step": i,
                "description": step,
                "code": _extract_code(completion.choices[0].message.content or ""),
            }
        )
    return code_samples


def generate_html_doc(client: OpenAI, analysis: str, code_samples: list) -> str:
    prompt = (
        "Create a complete, interactive HTML documentation page for this tutorial.\n\n"
        f"Workflow Steps:\n{analysis}\n\n"
        f"Code Samples:\n{json.dumps(code_samples, indent=2)}\n\n"
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
    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=6000,
    )
    return completion.choices[0].message.content or ""


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="End-to-end pipeline using Moonshot API for video analysis and docs."
    )
    parser.add_argument("--video", required=True, help="Path to the video file.")
    parser.add_argument(
        "--prompt",
        default="Please describe the content of the video with a step-by-step workflow and key UI changes.",
        help="Instruction prompt sent with the video.",
    )
    parser.add_argument(
        "--context",
        default="",
        help="Optional context about the tutorial.",
    )
    parser.add_argument(
        "--output-dir",
        default="output_video_moonshot_full",
        help="Output directory for generated artifacts.",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=5,
        help="Max number of steps to generate code samples for.",
    )
    parser.add_argument(
        "--max-questions",
        type=int,
        default=6,
        help="Number of auto-generated questions.",
    )
    return parser


def main() -> None:
    args = _build_arg_parser().parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    video_path = Path(args.video)
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    client = _client()

    print("🎬 Step 1: Moonshot video analysis...")
    analysis = analyze_video(client, video_path, args.prompt)
    analysis_path = output_dir / "video_analysis.txt"
    analysis_path.write_text(analysis, encoding="utf-8")

    print("🧭 Step 2: Summary...")
    summary = generate_summary(client, analysis, args.context)
    (output_dir / "summary.txt").write_text(summary, encoding="utf-8")

    print("❓ Step 3: Auto Q&A...")
    questions = generate_questions(client, analysis, args.context, args.max_questions)
    (output_dir / "qa_questions.txt").write_text("\n".join(questions), encoding="utf-8")
    answers = answer_questions(client, analysis, questions, args.context)
    (output_dir / "qa_answers.txt").write_text(answers, encoding="utf-8")

    print("💻 Step 4: Code samples...")
    code_samples = generate_code_samples(client, analysis, args.max_steps)
    (output_dir / "code_samples.json").write_text(
        json.dumps(code_samples, indent=2), encoding="utf-8"
    )

    print("📚 Step 5: Interactive documentation...")
    html = generate_html_doc(client, analysis, code_samples)
    (output_dir / "interactive_tutorial_raw.txt").write_text(html, encoding="utf-8")
    (output_dir / "interactive_tutorial.html").write_text(_extract_html(html), encoding="utf-8")

    print("✅ Done")
    print(f"   • {analysis_path}")
    print(f"   • {output_dir / 'summary.txt'}")
    print(f"   • {output_dir / 'qa_questions.txt'}")
    print(f"   • {output_dir / 'qa_answers.txt'}")
    print(f"   • {output_dir / 'code_samples.json'}")
    print(f"   • {output_dir / 'interactive_tutorial.html'}")


if __name__ == "__main__":
    main()
