# Eleven Labs Podcast Generator

This repository contains a Jupyter notebook that automates the generation of a podcast using various text-to-speech (TTS) APIs and audio processing techniques. You can create a podcast with distinct male and female voices, add intro and outro music, apply fade-in and fade-out effects, and export the final podcast as an MP3 file.

## Features

- **Text-to-Speech (TTS) Generation**: Uses the Eleven Labs API to synthesize different voices for podcast hosts.
- **Audio Processing with pydub**: Supports adding intro and outro music, trimming, adjusting volume, and applying fade-in and fade-out effects.
- **Flexible Input**: Podcast scripts can be passed as text, and the code will generate audio files for each segment.
- **Supports Multiple File Formats**: Processes audio files in `.mp3` and `.wav` formats.
- **Final Podcast Export**: Combines all audio segments into a final podcast file with background music and smooth transitions.

## Setup

### Prerequisites

Before running the notebook, ensure that the following dependencies are installed:

- **Python 3.x**
- **pip** (Python package manager)

Install the required Python libraries:

```bash
pip install requests
pip install pydub
pip install google-cloud-texttospeech  # If using Google Cloud TTS
```

You will also need:

- An Eleven Labs API key (for voice generation).
- Optional: Google Cloud API key (if using Google Cloud Text-to-Speech).

### Additional Software

- **FFmpeg**: Required for `pydub` to process audio. Install FFmpeg using the following instructions:

#### On Linux (Ubuntu):
```bash
sudo apt install ffmpeg
```

#### On macOS (with Homebrew):
```bash
brew install ffmpeg
```

#### On Windows:
- Download and install FFmpeg from [FFmpeg.org](https://ffmpeg.org/download.html).

### Setup API Keys

- **Eleven Labs API**: Sign up at [Eleven Labs](https://beta.elevenlabs.io/), get your API key, and insert it in the notebook where required.
- **Google Cloud API (Optional)**: Follow [this guide](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries) to generate and set up your Google Cloud Text-to-Speech API key if using Google TTS.

## Structure of the Jupyter Notebook

### 1. Podcast Script Definition

In the notebook, you define the podcast script with dialogue between the hosts (e.g., Sarah and Dave). Each part of the conversation is synthesized using Eleven Labs' TTS.

```python
podcast_script = [
    ("Sarah", "Welcome to the Leadership Legends podcast. I’m Sarah, and joining me is Dave."),
    ("Dave", "Hey Sarah! I’m excited about today’s discussion. Let’s dive in!"),
    ...
]
```

### 2. Voice Synthesis with Eleven Labs API

The notebook uses Eleven Labs API to generate speech from the text. Ensure you have your API key and the correct voice IDs for male and female voices.

```python
generate_speech(text, voice_id, output_file)
```

### 3. Adding Intro and Outro Music

You can add music files to your podcast. The music is trimmed to a specific length and adjusted in volume if needed. Fade-in and fade-out effects are applied to create smooth transitions.

```python
# Apply 3-second fade-in to intro and 3-second fade-out to outro
intro_music = intro_music.fade_in(3000)
outro_music = outro_music.fade_out(3000)
```

### 4. Merging Audio Files

Once all the audio segments (hosts' speech and music) are generated, the notebook merges them into a single podcast file using `pydub`.

```python
final_podcast_with_music = intro_music + podcast_audio + outro_music
```

### 5. Exporting the Final Podcast

The final podcast is exported in MP3 or WAV format, depending on your preference.

```python
final_podcast_with_music.export("final_podcast_with_music.mp3", format="mp3")
```

## Usage

1. **Prepare Your Podcast Script**: Define the script in the notebook as dialogue between the hosts.
2. **Run the Notebook**: Follow the instructions in each cell to generate the voices, process the audio, and add music.
3. **Export Your Podcast**: After processing, the final podcast will be available as `final_podcast_with_music.mp3`.

## Example Workflow

- **Generate Speech**: The Eleven Labs API generates speech for both Sarah and Dave based on the text you provide.
- **Add Background Music**: Load an intro and outro music file, adjust volume, and apply fade effects.
- **Combine Audio**: Use `pydub` to concatenate the intro music, podcast dialogue, and outro music.
- **Export as MP3**: Save the final podcast with all the elements combined.

## Customization

- **Voice Customization**: Modify the stability and similarity boost parameters for the voices to better suit your needs.
- **Background Music**: Swap out intro/outro music as desired. The notebook supports `.mp3` and `.wav` formats.
- **Export Formats**: You can export the final podcast in either `.mp3` or `.wav` formats.

## Future Enhancements

- **Dynamic Voice Selection**: Add more voices or allow dynamic selection of voices through additional API calls.
- **Improved Audio Effects**: Explore more advanced audio effects like noise reduction or background ambient sound mixing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

