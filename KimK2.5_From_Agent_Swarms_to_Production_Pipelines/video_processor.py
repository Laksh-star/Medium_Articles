import cv2
from pathlib import Path
from typing import Dict, List
from config import Config


class VideoFrameExtractor:
    def __init__(self, video_path: str, output_dir: str = "frames"):
        self.video_path = video_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def extract_key_frames(
        self,
        interval_seconds: int = None,
        max_frames: int = None,
    ) -> List[Dict]:
        interval_seconds = interval_seconds or Config.FRAME_INTERVAL_SECONDS
        max_frames = max_frames or Config.MAX_FRAMES

        cap = cv2.VideoCapture(str(self.video_path))
        fps = cap.get(cv2.CAP_PROP_FPS)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = total_frames / fps if fps > 0 else 0

        frame_interval = int(fps * interval_seconds) if fps > 0 else 0

        frames = []
        frame_count = 0
        extracted_count = 0

        print(f"🎬 Video info: {duration:.1f}s, {total_frames} frames, {fps:.1f} FPS")

        while cap.isOpened() and extracted_count < max_frames:
            ret, frame = cap.read()
            if not ret:
                break

            should_capture = frame_interval == 0 or frame_count % frame_interval == 0
            if should_capture:
                timestamp = frame_count / fps if fps > 0 else 0
                frame_path = self.output_dir / f"frame_{extracted_count:04d}_{timestamp:.1f}s.jpg"
                cv2.imwrite(str(frame_path), frame)
                frames.append(
                    {
                        "path": str(frame_path),
                        "timestamp": timestamp,
                        "index": extracted_count,
                    }
                )
                extracted_count += 1
                print(f"  📸 Extracted frame {extracted_count}/{max_frames} at {timestamp:.1f}s")

            frame_count += 1

        cap.release()
        print(f"✅ Extracted {len(frames)} frames")
        return frames
