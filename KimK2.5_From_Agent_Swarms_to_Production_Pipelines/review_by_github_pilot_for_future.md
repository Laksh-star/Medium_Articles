# Review by GitHub Pilot (for future maintainers)

This file documents the changes made to the repo and recommendations for future work. Keep this file updated whenever significant changes are made to prompts, client wrappers, or pipeline flows.

## Summary of changes applied by automation
- README updated: clarified prerequisites, outputs, script-to-output mapping, known issues, cost and troubleshooting guidance. Mermaid diagram and comparison table preserved.
- Added this review file to capture recommendations, TODOs, and rationale.

## Recommended immediate next steps (TODOs)
1. Implement missing convenience methods in openrouter_client.py used across scripts:
   - generate_timestamped_summary(frames, workflow_steps, context)
   - generate_code_from_description(description, previous_code, output_format)
   - generate_questions_from_workflow(frames, workflow_steps, context)
   - answer_workflow_questions(frames, workflow_steps, code_samples, questions, context)
   Each should:
   - Use a small, well-documented prompt
   - Return a dict with keys: content, usage, model

2. Add file-size checks before base64-encoding videos. For example, refuse to encode files > 10 MB by default and instruct users to trim or upload.
3. Improve VideoFrameExtractor to seek by timestamp (CAP_PROP_POS_MSEC) to avoid reading every frame for long videos. Add an ffmpeg helper to extract frames more efficiently.
4. Add tests:
   - unit tests for _extract_html, _extract_code helpers
   - smoke test that runs VideoFrameExtractor on a very short generated video (or mocked capture)
5. Add CI (GitHub Actions): run flake8/black, run lint, and a smoke test that executes imports and frame extraction on a tiny test artifact.
6. Consider swapping prints for logging (python logging) and a --verbose flag.

## Longer-term enhancements
- Support uploading large videos to cloud storage (S3) and pass a URL to Moonshot instead of base64-encoding.
- Add rate-limit and retry behavior around API calls (exponential backoff).
- Add prompts versioning and a simple test-suite to ensure prompt changes don't break expected outputs.
- Provide a small sample video under /tests/ (CC0 or generated) for CI smoke runs.

## Checklist for reviewers
- Ensure any added client methods follow the same usage dict format.
- Verify that prompts used for code generation and summaries are robust and contain explicit output constraints (e.g., HTML_DOC must be full HTML).
- Check environment variable handling: prefer reading envs at call-time for flexibility during containerized runs.

## How to update this review file
- Edit this file with the PR that changes prompts or client methods and add a short rationale explaining why the change was made.

---

Maintainer: @Laksh-star
Date: 2026-02-03