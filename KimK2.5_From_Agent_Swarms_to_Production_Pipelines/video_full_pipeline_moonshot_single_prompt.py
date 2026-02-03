import argparse
import base64
import os
from pathlib import Path
from openai import OpenAI


def _client() -> OpenAI:
    api_key = os.environ.get("MOONSHOT_API_KEY")
    if not api_key:
        raise ValueError("MOONSHOT_API_KEY is not set in the environment.")
    return OpenAI(api_key=api_key, base_url="https://api.moonshot.ai/v1")


def _video_to_data_url(video_path: Path) -> str:
    video_data = video_path.read_bytes()
    ext = video_path.suffix.lstrip(".") or "mp4"
    return f"data:video/{ext};base64,{base64.b64encode(video_data).decode('utf-8')}"


def _build_context_probe(repeats: int, marker: str) -> str:
    if repeats <= 0:
        return ""
    chunk = "CONTEXT_PROBE_" * 200
    probe = ("\n" + chunk) * repeats
    return (
        f"\n\n[CONTEXT_PROBE_START]\n{probe}\n[CONTEXT_PROBE_END]\n"
        f"Return this marker verbatim at the end of your response: {marker}\n"
    )


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Single-prompt pipeline using Moonshot (video + docs in one response)."
    )
    parser.add_argument("--video", required=True, help="Path to the video file.")
    parser.add_argument(
        "--context",
        default="",
        help="Optional context about the tutorial.",
    )
    parser.add_argument(
        "--output-dir",
        default="output_video_moonshot_single",
        help="Output directory for the response.",
    )
    parser.add_argument(
        "--context-probe-repeats",
        type=int,
        default=0,
        help="Add a large repeated block to probe context handling.",
    )
    parser.add_argument(
        "--context-probe-marker",
        default="PROBE_OK_12345",
        help="Marker to verify the model saw the end of the prompt.",
    )
    return parser


def main() -> None:
    args = _build_arg_parser().parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)

    video_path = Path(args.video)
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    prompt = (
        "You are given a tutorial video. Perform ALL tasks in one response.\n\n"
        f"Context: {args.context}\n\n"
        "Tasks:\n"
        "1) Provide a step-by-step workflow (10-15 steps).\n"
        "2) Provide a concise summary (8-12 bullets).\n"
        "3) Generate 5-7 Q&A pairs (questions + answers).\n"
        "4) Provide 3-5 short HTML code samples related to the steps.\n"
        "5) Output a complete, single-page HTML documentation file at the end.\n\n"
        "Output Rules:\n"
        "- Use clear section headers: WORKFLOW, SUMMARY, QA, CODE_SAMPLES, HTML_DOC\n"
        "- The HTML_DOC section must contain a full HTML document only.\n"
        "- Do not use markdown code fences.\n"
    )

    prompt += _build_context_probe(args.context_probe_repeats, args.context_probe_marker)

    client = _client()
    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[
            {"role": "system", "content": "You are Kimi."},
            {
                "role": "user",
                "content": [
                    {"type": "video_url", "video_url": {"url": _video_to_data_url(video_path)}},
                    {"type": "text", "text": prompt},
                ],
            },
        ],
        temperature=0.3,
        max_tokens=8000,
    )

    output_path = output_dir / "single_prompt_response.txt"
    output_path.write_text(completion.choices[0].message.content or "", encoding="utf-8")
    print(f"✅ Response saved to: {output_path}")


if __name__ == "__main__":
    main()
