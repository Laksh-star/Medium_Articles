
# Automated Essay Grading with Haystack

This project demonstrates an automated essay grading system built using Haystack, a powerful framework for building natural language processing (NLP) pipelines. The system uses a self-reflecting mechanism to provide comprehensive and refined feedback on essays.

## Features

- Automated grading and feedback generation for essays
- Self-reflecting pipeline that iteratively refines feedback
- Integration with Chroma for document storage and retrieval
- Utilizes OpenAI's GPT model for natural language processing

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- An OpenAI API key

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/essays-grading.git
cd essays-grading
Copy
2. Install the required packages:
pip install haystack-ai colorama chroma-haystack
Copy
3. Set up your OpenAI API key as an environment variable:
export OPENAI_API_KEY='your-api-key-here'
Copy
## Usage

1. Place your essay files (in .txt format) in a folder named `essays` in the project directory.

2. Run the notebook


## How It Works

The system uses a pipeline with the following components:

1. **ChromaQueryTextRetriever**: Retrieves essays from the Chroma document store.
2. **PromptBuilder**: Constructs prompts for the language model.
3. **OpenAIGenerator**: Generates initial feedback and refined versions.
4. **EssayFeedbackRefiner**: A custom component that manages the feedback refinement process.

The pipeline iteratively refines the feedback for each essay, ensuring comprehensive and high-quality grading.

## Customization

You can customize the grading criteria and feedback style by modifying the prompt template in the .ipynb file.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [Haystack](https://github.com/deepset-ai/haystack) framework by deepset.
- The language model is powered by OpenAI's GPT.

## Contact

If you have any questions or feedback, please open an issue in this repository.
