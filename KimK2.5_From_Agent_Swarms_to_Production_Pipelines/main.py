import argparse
import json
import re
from pathlib import Path
from typing import Dict, List
from video_processor import VideoFrameExtractor
from openrouter_client import KimiK25OpenRouterClient
from config import Config


class VideoToDocsConverter:
    def __init__(self, video_path: str, context: str = ""):
        self.video_path = video_path
        self.context = context
        self.kimi = KimiK25OpenRouterClient()
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        self.cost_tracker = {"input_tokens": 0, "output_tokens": 0, "estimated_cost": 0.0}

    def process(self) -> Dict:
        print("=" * 60)
        print("🚀 Video to Interactive Documentation Converter")
        print("   Powered by Kimi K2.5 via OpenRouter")
        print("=" * 60)

        print("\n📹 Step 1: Extracting video frames...")
        extractor = VideoFrameExtractor(self.video_path)
        frames = extractor.extract_key_frames()

        if not frames:
            raise ValueError("No frames extracted from video")

        print("\n🔍 Step 2: Analyzing workflow with Kimi K2.5 (Vision)...")
        analysis_result = self.kimi.analyze_frame_sequence(
            frames,
            self.context,
            max_frames=10,
        )
        workflow_analysis = analysis_result["content"]
        self._track_usage(analysis_result["usage"])

        analysis_path = self.output_dir / "workflow_analysis.txt"
        with open(analysis_path, "w", encoding="utf-8") as file:
            file.write(f"Context: {self.context}\n\n")
            file.write(workflow_analysis or "")
            if "reasoning" in analysis_result:
                file.write(f"\n\n--- Reasoning ---\n{analysis_result['reasoning']}")

        print("✅ Workflow analysis complete")
        print(f"   Tokens used: {analysis_result['usage']['total_tokens']}")

        print("\n💻 Step 3: Generating code samples...")
        steps = self._parse_steps(workflow_analysis or "")
        code_samples = []

        for i, step in enumerate(steps[:5], 1):
            print(f"   📝 Generating code for step {i}/{min(len(steps), 5)}...")
            prev_code = code_samples[-1]["code"] if code_samples else ""

            code_result = self.kimi.generate_code_from_description(
                step,
                previous_code=prev_code,
                output_format="html",
            )
            code_samples.append(
                {
                    "step": i,
                    "description": step,
                    "code": self._extract_code(code_result["content"] or ""),
                }
            )
            self._track_usage(code_result["usage"])

        print("✅ Code generation complete")

        code_path = self.output_dir / "code_samples.json"
        with open(code_path, "w", encoding="utf-8") as file:
            json.dump(code_samples, file, indent=2)

        print("\n🧭 Step 3b: Creating timestamped summary...")
        summary_result = self.kimi.generate_timestamped_summary(
            frames,
            workflow_analysis or "",
            context=self.context,
        )
        self._track_usage(summary_result["usage"])
        summary_path = self.output_dir / "summary_with_timestamps.txt"
        with open(summary_path, "w", encoding="utf-8") as file:
            file.write(summary_result["content"] or "")
        print("✅ Timestamped summary created")

        print("\n📚 Step 4: Creating interactive documentation...")
        doc_result = self.kimi.create_interactive_documentation(
            workflow_analysis or "",
            json.dumps(code_samples, indent=2),
        )
        self._track_usage(doc_result["usage"])

        doc_path = self.output_dir / "interactive_tutorial.html"
        raw_doc_path = self.output_dir / "interactive_tutorial_raw.txt"
        raw_content = doc_result["content"] or ""
        if raw_content.strip():
            html_content = self._extract_html(raw_content)
        else:
            html_content = (
                "<!doctype html>\n"
                "<html><body><pre>"
                "Documentation generation returned an empty response. "
                "See output/interactive_tutorial_raw.txt for details."
                "</pre></body></html>"
            )
        with open(doc_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        with open(raw_doc_path, "w", encoding="utf-8") as file:
            file.write(raw_content)

        if raw_content.strip():
            print("✅ Documentation created")
        else:
            print("⚠️ Documentation response was empty; wrote a placeholder HTML.")

        print("\n" + "=" * 60)
        print("🎉 Conversion Complete!")
        print("=" * 60)
        print("\n📊 Token Usage Summary:")
        print(f"   Input tokens:  {self.cost_tracker['input_tokens']:,}")
        print(f"   Output tokens: {self.cost_tracker['output_tokens']:,}")
        print(
            f"   Total tokens:  {self.cost_tracker['input_tokens'] + self.cost_tracker['output_tokens']:,}"
        )
        print(f"   Est. cost:     ${self.cost_tracker['estimated_cost']:.4f}")
        print("\n📁 Output files:")
        print(f"   • {analysis_path}")
        print(f"   • {code_path}")
        print(f"   • {summary_path}")
        print(f"   • {doc_path}")

        return {
            "frames": frames,
            "workflow": workflow_analysis,
            "code_samples": code_samples,
            "summary_path": str(summary_path),
            "documentation_path": str(doc_path),
            "cost_tracker": self.cost_tracker,
        }

    def _parse_steps(self, workflow_text: str) -> List[str]:
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

    def _extract_code(self, content: str) -> str:
        fenced = re.findall(r"```(?:\w+)?\n(.*?)```", content, re.DOTALL)
        if fenced:
            return fenced[0].strip()
        return content.strip()

    def _extract_html(self, content: str) -> str:
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

    def _track_usage(self, usage: Dict) -> None:
        prompt_tokens = int(usage.get("prompt_tokens", 0) or 0)
        completion_tokens = int(usage.get("completion_tokens", 0) or 0)
        self.cost_tracker["input_tokens"] += prompt_tokens
        self.cost_tracker["output_tokens"] += completion_tokens
        self.cost_tracker["estimated_cost"] += (
            (prompt_tokens / 1_000_000) * Config.COST_PER_M_INPUT
            + (completion_tokens / 1_000_000) * Config.COST_PER_M_OUTPUT
        )


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert tutorial videos into interactive docs.")
    parser.add_argument("--video", required=True, help="Path to the tutorial video file.")
    parser.add_argument("--context", default="", help="Optional context about the tutorial.")
    parser.add_argument(
        "--qa-file",
        default="",
        help="Optional path to a text file with one question per line.",
    )
    parser.add_argument(
        "--qa-auto",
        action="store_true",
        help="Auto-generate questions from the workflow analysis and answer them.",
    )
    return parser


def main() -> None:
    parser = _build_arg_parser()
    args = parser.parse_args()

    video_path = Path(args.video)
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")

    converter = VideoToDocsConverter(str(video_path), context=args.context)
    result = converter.process()

    questions = []
    if args.qa_file:
        qa_path = Path(args.qa_file)
        if not qa_path.exists():
            raise FileNotFoundError(f"QA file not found: {qa_path}")
        questions = [
            line.strip()
            for line in qa_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if not questions:
            raise ValueError("QA file is empty.")
    elif args.qa_auto:
        print("\n❓ Step 5: Auto-generating questions...")
        gen_result = converter.kimi.generate_questions_from_workflow(
            result["frames"],
            result["workflow"] or "",
            context=args.context,
        )
        converter._track_usage(gen_result["usage"])
        questions = [
            line.strip()
            for line in (gen_result["content"] or "").splitlines()
            if line.strip()
        ]
        gen_out_path = Path("output") / "qa_questions.txt"
        gen_out_path.write_text("\n".join(questions), encoding="utf-8")
        print("✅ Questions generated")
        print(f"   • {gen_out_path}")

    if questions:
        print("\n❓ Step 6: Answering workflow questions...")
        qa_result = converter.kimi.answer_workflow_questions(
            result["frames"],
            result["workflow"] or "",
            json.dumps(result["code_samples"], indent=2),
            questions,
            context=args.context,
        )
        converter._track_usage(qa_result["usage"])
        qa_out_path = Path("output") / "qa_answers.txt"
        qa_raw_path = Path("output") / "qa_answers_raw.txt"
        qa_raw_path.write_text(qa_result["content"] or "", encoding="utf-8")
        if qa_result["content"]:
            qa_out_path.write_text(qa_result["content"], encoding="utf-8")
            print("✅ Q&A answers created")
            print(f"   • {qa_out_path}")
        else:
            print("⚠️ Q&A response was empty; retrying once with shorter context...")
            qa_retry = converter.kimi.answer_workflow_questions(
                result["frames"],
                result["workflow"] or "",
                "",
                questions,
                context=args.context,
            )
            converter._track_usage(qa_retry["usage"])
            qa_raw_path.write_text(qa_retry["content"] or "", encoding="utf-8")
            qa_out_path.write_text(qa_retry["content"] or "", encoding="utf-8")
            if qa_retry["content"]:
                print("✅ Q&A answers created (retry)")
                print(f"   • {qa_out_path}")
            else:
                print("❌ Q&A response still empty; see qa_answers_raw.txt")
        print(f"   • {qa_raw_path}")


if __name__ == "__main__":
    main()
