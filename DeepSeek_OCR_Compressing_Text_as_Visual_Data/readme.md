# DeepSeek-OCR Colab Notebook

This repository contains a Google Colab notebook demonstrating how to use the DeepSeek-OCR model for various tasks, including document conversion to markdown, free OCR, image description, figure parsing, and locating specific elements within images.

## Setup

1.  Open the notebook in Google Colab.
2.  Run the first cell to install the necessary libraries with the specified versions. **Note: You may need to restart the runtime after this step.**
3.  Run the second cell to load the DeepSeek-OCR model and tokenizer.
4.  Run the third cell to load the extended prompt support functions.

## Usage

The notebook provides several functions for performing OCR tasks:

*   `perform_ocr(image_path, prompt_type, base_size)`: Performs OCR with preset prompt types ("markdown", "free_ocr", "ocr", "describe", "figure").
*   `perform_ocr_custom(image_path, prompt, prompt_type, ref_text, base_size)`: Provides extended support for custom prompts and locating specific elements.
*   `locate_in_image(image_path, reference_text, base_size)`: A helper function to locate specific text or elements in an image using bounding boxes.
*   `download_image(url, save_path)`: Downloads an image from a given URL.
*   `upload_and_process(prompt_type, base_size)`: Uploads an image from your local machine and processes it with the specified prompt type and base size.

Examples of how to use these functions are provided in the notebook.

## Examples

See the code cells in the notebook for detailed examples of how to use the `perform_ocr_custom` and `locate_in_image` functions with different prompts and image sizes.

## Output

The results of the OCR processing, including the extracted text and images with bounding boxes (if applicable), are saved in the `./output` directory.
