# Video Frame Analysis with GPT-4.1

This script extracts and analyzes frames from a video file (specifically Charlie Chaplin's "The Tramp" silent film) to answer multiple-choice questions about the content using OpenAI's GPT-4.1 model.

## Prerequisites

- Python 3.6+
- Google Colab (for easy execution)
- An OpenAI API key with access to GPT-4.1

## Required Libraries

```
pip install openai opencv-python tqdm matplotlib numpy
```

## Features

- Extracts frames from specific ranges in a video file
- Enhances frames for better visibility and analysis
- Analyzes frames using OpenAI's GPT-4.1 model to answer questions
- Handles batching and retries for robust API interactions
- Preserves aspect ratio and improves image quality

## Usage

1. Upload your video file to Google Colab or provide a path
2. The script will extract frames from predefined ranges
3. These frames will be analyzed to answer the provided questions
4. Results will be displayed with a comparison to expected answers

## Configuration

- Modify the `MCQS` list to change the questions and frame ranges
- Adjust `FRAME_RATE` to control the sampling rate of frames
- Frame enhancement parameters can be tweaked for different video sources

## Sample Output

Analysis Results:
- Q1: b) 1915
- Q2: b) He sees two other men attacking her and trying to take her money/purse.
- Q3: b) A place to sleep
- Q4: c) Milking a cow
- Q5: b) He finds and reads a note written by the young woman.

Expected Answers:
- Q1: b) 1915
- Q2: b) He sees two other men attacking her and trying to take her money/purse.
- Q3: c) A job working on the farm
- Q4: c) Milking a cow
- Q5: b) He finds and reads a note written by the young woman.

Accuracy: 4/5 correct (80%)

## Notes

- The script automatically cleans up temporary frames after analysis
- Frames are enhanced for better visibility of black and white film content
- The code uses prompt variations to improve analysis accuracy
- The current version achieves 80% accuracy on the sample questions
