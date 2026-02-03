import argparse
import json
import re
from pathlib import Path
from openrouter_client import KimiK25OpenRouterClient


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
        description="Generate docs from an existing video analysis text."
    )
    parser.add_argument(
        "--analysis-file",
        default="output_video_openrouter/video_analysis.txt",
        help="Path to the video analysis text file.",
    )
    parser.add_argument(
        "--output-dir",
        default="output_video_openrouter_docs",
        help="Output directory for generated artifacts.",
    )
    parser.add_argument(
        "--context",
        default="",
        help="Optional context about the tutorial.",
    )
    return parser


def main() -> None:
    args = _build_arg_parser().parse_args()
    analysis_path = Path(args.analysis_file)
    if not analysis_path.exists():
        raise FileNotFoundError(f"Analysis file not found: {analysis_path}")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    analysis_text = analysis_path.read_text(encoding="utf-8")
    client = KimiK25OpenRouterClient()

    summary_result = client.generate_timestamped_summary(
        frames=[],
        workflow_steps=analysis_text,
        context=args.context,
    )
    summary_path = output_dir / "summary.txt"
    summary_path.write_text(summary_result["content"] or "", encoding="utf-8")

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
    questions_path = output_dir / "qa_questions.txt"
    questions_path.write_text("\n".join(questions), encoding="utf-8")

    a_result = client.answer_workflow_questions(
        frames=[],
        workflow_steps=analysis_text,
        code_samples="",
        questions=questions,
        context=args.context,
    )
    answers_path = output_dir / "qa_answers.txt"
    answers_path.write_text(a_result["content"] or "", encoding="utf-8")

    steps = [
        line.strip()
        for line in analysis_text.splitlines()
        if line.strip().lower().startswith("step ")
    ]
    code_samples = []
    for i, step in enumerate(steps[:5], 1):
        code_result = client.generate_code_from_description(
            step,
            previous_code=code_samples[-1]["code"] if code_samples else "",
            output_format="html",
        )
        code_samples.append(
            {
                "step": i,
                "description": step,
                "code": code_result["content"] or "",
            }
        )
    code_samples_path = output_dir / "code_samples.json"
    code_samples_path.write_text(
        json.dumps(code_samples, indent=2), encoding="utf-8"
    )

    doc_result = client.create_interactive_documentation(
        analysis_text,
        json.dumps(code_samples, indent=2),
    )
    html = _extract_html(doc_result["content"] or "")
    html_path = output_dir / "interactive_tutorial.html"
    html_path.write_text(html, encoding="utf-8")
    raw_path = output_dir / "interactive_tutorial_raw.txt"
    raw_path.write_text(doc_result["content"] or "", encoding="utf-8")

    print("✅ Generated docs from video analysis")
    print(f"   • {summary_path}")
    print(f"   • {questions_path}")
    print(f"   • {answers_path}")
    print(f"   • {code_samples_path}")
    print(f"   • {html_path}")
    print(f"   • {raw_path}")


if __name__ == "__main__":
    main()
