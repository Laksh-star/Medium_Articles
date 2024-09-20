# Eleven Labs Podcast Generator

This repository contains a Python script for generating podcasts using the Eleven Labs Text-to-Speech API. With this tool, you can create multi-speaker podcasts with synthesized voices and even add intro and outro music.

## Features

- Generate speech for multiple speakers using Eleven Labs API
- Process a complete podcast script
- Merge individual audio files into a single podcast
- Add intro and outro music with fade effects

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An Eleven Labs API key
- The following Python libraries:
  - `requests`
  - `pydub`

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Laksh-star/Medium_Articles.git
   ```

2. Navigate to the project directory:
   ```
   cd Medium_Articles/How_to_Generate_AI_Podcasts_with_Eleven_Labs_A_Beginner's_Guide
   ```

3. Install the required Python libraries:
   ```
   pip install requests pydub
   ```

## Usage

1. Replace `'your_eleven_labs_api_key'` in the script with your actual Eleven Labs API key.

2. Modify the `podcast_script` list to include your desired content. Each tuple in the list should contain the speaker's name and their line.

3. Replace the placeholder voice IDs (`EXAMPLE_SARAH_VOICE_ID` and `EXAMPLE_DAVE_VOICE_ID`) with actual voice IDs from your Eleven Labs account.

4. If you want to add intro and outro music, place your audio files (in .wav format) in the project directory and name them `intro_music.wav` and `outro_music.wav`.

5. Run the script:
   ```
   python podcast_generator.py
   ```

## Example

Here's a simple example of how to structure your podcast script:

```python
podcast_script = [
    ("Sarah", "Welcome to the Leadership Legends podcast. I'm Sarah, and joining me is Dave."),
    ("Dave", "Hey Sarah! I'm excited about today's discussion. We're diving into leadership lessons from one of the most iconic characters in literature and film—Don Vito Corleone from The Godfather."),
    # Add more lines here...
]
```

## Contributing

Contributions to this project are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Eleven Labs](https://elevenlabs.io/) for providing the Text-to-Speech API
- [Pydub](http://pydub.com/) for audio processing capabilities
