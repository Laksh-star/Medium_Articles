# Advanced Movie Set Optimization System

## Overview

This system analyzes historical settings for film production to determine the optimal balance between physical set construction and CGI elements. It generates visualizations showing what should be physically built versus digitally created, helping production teams make informed budgeting decisions.

**⚠️ NOTE: This code has not been tested yet and is provided as a conceptual implementation only.**

## Components

- `movie_set_optimization.py`: Main implementation
- `gladiator_colosseum_config.json`: Example configuration file
- `example_usage.py`: Simple script to run the system
- `requirements.txt`: Dependencies

## Requirements

- Python 3.8+
- OpenAI API key with access to GPT-4o and GPT Image models
- Reference images of the historical setting
- Dependencies listed in requirements.txt

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```

3. Prepare reference images and place them in a `references` folder

4. Configure your project by creating a JSON configuration file following the example in `gladiator_colosseum_config.json`

## Usage

Run the system with your configuration file:

```python
from movie_set_optimization import optimize_movie_set

# Run the optimization process
results = optimize_movie_set("your_config.json")

# Access results
print(f"Report available at: {results['report_path']}")
```

## Configuration

The configuration file requires:
- Project details (name, historical setting, period)
- Reference image paths
- Budget constraints
- Script scenes with descriptions

See `gladiator_colosseum_config.json` for a complete example.

## Outputs

The system generates:
- Full archaeological reconstruction
- Physical set visualizations for each scene
- Final composite visualizations with CGI
- Side-by-side comparisons
- Budget analysis
- Comprehensive HTML report

All outputs are saved to an `output` directory.

## Limitations

- **UNTESTED CODE**: This implementation has not been tested and may require debugging.
- Results quality depends on the quality of reference images provided.
- Budget estimates are approximations and should be reviewed by professionals.
- Processing time may be significant due to multiple API calls.
- API costs will vary based on number of scenes and quality settings.

## Future Improvements

- Testing and bug fixing
- UI for more interactive configuration
- Integration with 3D modeling software
- Support for video output
- More detailed construction cost breakdowns


