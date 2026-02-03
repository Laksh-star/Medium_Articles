import argparse
import base64
import os
from pathlib import Path
from openai import OpenAI
from config import Config


def analyze_video(video_path: Path, output_dir: Path, prompt: str) -> str:
    api_key = os.environ.get("MOONSHOT_API_KEY")
    if not api_key:
        raise ValueError("MOONSHOT_API_KEY is not set in the environment.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.moonshot.ai/v1",
    )

    video_data = video_path.read_bytes()
    ext = video_path.suffix.lstrip(".") or "mp4"
    video_url = (
        f"data:video/{ext};base64,"
        f"{base64.b64encode(video_data).decode('utf-8')}"
    )

    completion = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[
            {"role": "system", "content": "You are Kimi."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "video_url",
                        "video_url": {"url": video_url},
                    },
                    {
                        "type": "text",
                        "text": prompt,
                    },
                ],
            },
        ],
    )

    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "video_analysis.txt"
    output_path.write_text(completion.choices[0].message.content or "", encoding="utf-8")
    return str(output_path)


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze a video directly with Kimi K2.5.")
    parser.add_argument("--video", required=True, help="Path to the video file.")
    parser.add_argument(
        "--prompt",
        default="Please describe the content of the video.",
        help="Instruction prompt sent with the video.",
    )
    parser.add_argument(
        "--output-dir",
        default="output_video_openrouter",
        help="Output directory for the analysis.",
    )
    return parser


def main() -> None:
    parser = _build_arg_parser()
    args = parser.parse_args()

    video_path = Path(args.video)
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    output_dir = Path(args.output_dir)
    output_path = analyze_video(video_path, output_dir, args.prompt)
    print(f"✅ Video analysis written to: {output_path}")


if __name__ == "__main__":
    main()
