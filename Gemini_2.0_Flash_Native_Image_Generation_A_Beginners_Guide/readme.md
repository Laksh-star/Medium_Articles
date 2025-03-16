# Gemini 2.0 Flash Native Image Generation: Accessibility Design Test

This repository contains a Python implementation demonstrating how to use Google's Gemini 2.0 Flash model for accessibility design testing. The code shows how to upload images of spaces and have the AI generate modified versions with highlighted accessibility features and potential obstacles.

## Overview

This notebook demonstrates a practical application of Google's Gemini 2.0 Flash native image generation capabilities. It focuses on the accessibility design test use case, where the AI can:

- Add wheelchair ramps to entrances in images
- Highlight obstacles that might impede accessibility (steps, narrow doorways, etc.)
- Visualize how spaces could be modified to improve accessibility

This is useful for architects, urban planners, and accessibility consultants to quickly visualize and test design modifications for inclusive spaces.

## Requirements

- Python 3.6+
- Google Gemini API key
- Required libraries:
  - `google-generativeai`
  - `IPython`
  - Access to `gemini-2.0-flash-exp-image-generation` model

## Installation

```bash
pip install google-generativeai ipython
```

## Usage

1. Set your Gemini API key
2. Upload an image of a space you want to analyze (e.g., subway_station.png)
3. Define your accessibility modification requirements
4. Run the code to generate a modified image with highlighted accessibility features

## Code Explanation

The code performs the following steps:

1. Imports necessary libraries and sets up the Gemini API client
2. Uploads an image (e.g., subway_station.png) to be modified
3. Creates a request with specific accessibility modification instructions
4. Configures the generation parameters
5. Processes the response stream, saving and displaying the modified image

## Example Prompt

The example uses this accessibility-focused prompt:
```
Add wheelchair ramps to the entrances and highlight any obstacles that might impede accessibility, such as steps or narrow doorways.
```

## Other Potential Use Cases

This code can be easily modified for other use cases including:

1. **Medical Training and Simulation** - Modify medical images to show different conditions
2. **Disaster Preparedness** - Show landscapes with simulated disaster effects
3. **Forensic Reconstruction** - Enhance or age faces in images
4. **Agricultural Monitoring** - Show fields with different pest damage or drought conditions
5. **Manufacturing Quality Control** - Visualize potential product defects

## Disclaimer

The images used in this repository are for test purposes only and are not meant to infringe any copyrights. All input images are used for educational and research purpose only and no copyright infringement is intended. Same applies to the generated images of the AI model using these. The API key included in the code is a placeholder and should be replaced with your own valid Gemini API key.

This implementation is for demonstration purposes and may require additional modifications for production use cases. Always ensure compliance with Google's usage policies when using the Gemini API.

## References

- [Google Gemini API Documentation](https://ai.google.dev/api?lang=python)
- [Gemini 2.0 Flash Blog Post](https://developers.googleblog.com/en/experiment-with-gemini-20-flash-native-image-generation/)

