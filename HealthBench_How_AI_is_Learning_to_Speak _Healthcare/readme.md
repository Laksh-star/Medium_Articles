# HealthBench Starter Implementation

This repository provides a simplified implementation of the HealthBench methodology for evaluating AI models on healthcare conversations. HealthBench is a benchmark developed by OpenAI to measure the performance and safety of large language models in healthcare contexts.

## About HealthBench

HealthBench consists of 5,000 multi-turn conversations between a model and a user (either an individual or healthcare professional). Responses are evaluated using conversation-specific rubrics created by physicians. The full benchmark measures 48,562 unique aspects of model behavior across several health contexts and behavioral dimensions.

For more information, see the [original HealthBench paper](https://github.com/openai/simple-evals).

## This Implementation

While the full HealthBench dataset isn't publicly available, this starter implementation demonstrates the core evaluation methodology:

1. Creating sample HealthBench-style examples with conversations and rubric criteria
2. Evaluating model responses to medical queries
3. Grading responses against specific rubric criteria
4. Calculating scores based on criteria met vs. maximum possible points

## Features

- Sample HealthBench-style examples across different healthcare themes
- Evaluation pipeline using the OpenAI API
- Support for testing multiple models (GPT-3.5, GPT-4, etc.)
- Functions for both pre-defined examples and custom evaluations
- Score calculation and analysis tools

## Getting Started

### Prerequisites

- Python 3.6+
- OpenAI API key


### Usage

```python
# Set up your OpenAI API key
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key'

# Run evaluation on a sample example
from healthbench_starter import evaluate_healthbench_sample
result = evaluate_healthbench_sample(example_index=0, model="gpt-4")

# Create and run your own custom evaluation
from healthbench_starter import create_custom_evaluation
my_evaluation = create_custom_evaluation(model="gpt-4")
```

## Sample Examples

The implementation includes several sample healthcare conversations covering themes like:
- Emergency referrals
- Responding under uncertainty
- Context seeking
- Global health considerations

Each example comes with rubric criteria modeled after the physician-created criteria in the original HealthBench.

## Limitations

This implementation is a simplified version of the full HealthBench methodology:
- It uses a small set of sample examples rather than the full 5,000 conversations
- The rubric criteria are inspired by but not identical to the physician-created criteria
- It uses general model-based grading rather than the specialized grader validated against physician judgment

## Citation

If you use this implementation in your research or applications, please cite the original HealthBench paper:

```
@article{arora2025healthbench,
  title={HealthBench: Evaluating Large Language Models Towards Improved Human Health},
  author={Arora, Rahul K. and Wei, Jason and Soskin Hicks, Rebecca and Bowman, Preston and Quiñonero-Candela, Joaquin and Tsimpourlas, Foivos and Sharman, Michael and Shah, Meghan and Vallone, Andrea and Beutel, Alex and Heidecke, Johannes and Singhal, Karan},
  journal={arXiv preprint},
  year={2025}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenAI for developing the original HealthBench methodology
- The 262 physicians who contributed to creating the full HealthBench benchmark
