import argparse
import json
import re
from pathlib import Path

from openrouter_client import KimiK25OpenRouterClient
from video_processor_kimi_video import analyze_video


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


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="End-to-end pipeline: Moonshot video analysis + OpenRouter docs."
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
        default="output_video_full",
        help="Output directory for generated artifacts.",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=5,
        help="Max number of steps to generate code samples for.",
    )
    return parser


def main() -> None:
    args = _build_arg_parser().parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    video_path = Path(args.video)
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    print("🎬 Step 1: Moonshot video analysis...")
    analysis_path = Path(
        analyze_video(video_path, output_dir, args.prompt)
    )
    analysis_text = analysis_path.read_text(encoding="utf-8")

    client = KimiK25OpenRouterClient()

    print("🧭 Step 2: Timestamp-free summary...")
    summary_result = client.generate_timestamped_summary(
        frames=[],
        workflow_steps=analysis_text,
        context=args.context,
    )
    (output_dir / "summary.txt").write_text(
        summary_result["content"] or "", encoding="utf-8"
    )

    print("❓ Step 3: Auto Q&A...")
    q_result = client.generate_questions_from_workflow(
        frames=[],
        workflow_steps=analysis_text,
        context=args.context,
    )
    questions = [
        line.strip()
        for line in (q_result["content"] or "").splitlines()
        if line.strip()
    ]
    (output_dir / "qa_questions.txt").write_text(
        "\n".join(questions), encoding="utf-8"
    )

    a_result = client.answer_workflow_questions(
        frames=[],
        workflow_steps=analysis_text,
        code_samples="",
        questions=questions,
        context=args.context,
    )
    (output_dir / "qa_answers.txt").write_text(
        a_result["content"] or "", encoding="utf-8"
    )

    print("💻 Step 4: Code samples...")
    steps = _parse_steps(analysis_text)
    code_samples = []
    for i, step in enumerate(steps[: args.max_steps], 1):
        prev_code = code_samples[-1]["code"] if code_samples else ""
        code_result = client.generate_code_from_description(
            step,
            previous_code=prev_code,
            output_format="html",
        )
        code_samples.append(
            {
                "step": i,
                "description": step,
                "code": _extract_code(code_result["content"] or ""),
            }
        )
    (output_dir / "code_samples.json").write_text(
        json.dumps(code_samples, indent=2), encoding="utf-8"
    )

    print("📚 Step 5: Interactive documentation...")
    doc_result = client.create_interactive_documentation(
        analysis_text,
        json.dumps(code_samples, indent=2),
    )
    html = _extract_html(doc_result["content"] or "")
    (output_dir / "interactive_tutorial.html").write_text(html, encoding="utf-8")
    (output_dir / "interactive_tutorial_raw.txt").write_text(
        doc_result["content"] or "", encoding="utf-8"
    )

    print("✅ Done")
    print(f"   • {analysis_path}")
    print(f"   • {output_dir / 'summary.txt'}")
    print(f"   • {output_dir / 'qa_questions.txt'}")
    print(f"   • {output_dir / 'qa_answers.txt'}")
    print(f"   • {output_dir / 'code_samples.json'}")
    print(f"   • {output_dir / 'interactive_tutorial.html'}")


if __name__ == "__main__":
    main()
