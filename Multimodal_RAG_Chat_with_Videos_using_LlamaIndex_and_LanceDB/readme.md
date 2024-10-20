# Multimodal RAG Video Analysis

## Overview

This project implements a Multimodal Retrieval-Augmented Generation (RAG) system for video analysis, focusing on YouTube Community Guidelines compliance checking and movie review extraction. It leverages OpenAI's GPT-4V for multimodal embeddings and LanceDB for efficient vector storage.

## Features

- Video processing: Extracts frames and audio from uploaded videos
- Multimodal indexing: Creates a searchable index of video content
- Content analysis:
  - YouTube Community Guidelines compliance check
  - Age-restricted content detection
  - Movie review extraction
- Report generation: Produces structured reports based on the analysis
- Action recommendation: Suggests actions based on the analysis results

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Laksh-star/Medium_Articles/Multimodal_RAG_Chat_with_Videos_using_LlamaIndex_and_LanceDB.git
   cd multimodal-rag-video-analysis
   ```

2. Install the required packages:
   ```
   pip install llama-index-vector-stores-lancedb
   pip install llama-index-multi-modal-llms-openai
   pip install llama-index-embeddings-clip
   pip install llama_index ftfy regex tqdm
   pip install openai-whisper
   pip install git+https://github.com/openai/CLIP.git
   pip install torch torchvision
   pip install matplotlib scikit-image
   pip install lancedb
   pip install moviepy
   pip install pydub
   pip install SpeechRecognition
   pip install ffmpeg-python
   pip install soundfile
   ```

3. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

1. Place your video file in the project directory.

2. Upload and Execute the .ipynb file in Google Colab or locllay.
   ```
   Medium_Multimodal_RAG_Chat_with_Videos_using_ _LlamaIndex_and_LanceDB.ipynb
   ```

3. The script will process the video, perform the analysis, and generate a report with suggested actions.

## Configuration

You can modify the following parameters in the `main.py` file:

- `output_folder`: Directory for processed video data
- `filepath`: Path to the input video file

## Output

The script generates a JSON report containing:

- Timestamp of the analysis
- Results of the Community Guidelines compliance check
- Results of the age restriction check
- Extracted movie review

It also provides a list of suggested actions based on the analysis.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for GPT-4V
- LlamaIndex for Multimodal RAG platform/pipeline
- LanceDB for vector storage
- The creators and maintainers of the various Python libraries used in this project

## Disclaimer

This tool is for educational and research purposes only. Always respect YouTube's terms of service and community guidelines when using this tool.
