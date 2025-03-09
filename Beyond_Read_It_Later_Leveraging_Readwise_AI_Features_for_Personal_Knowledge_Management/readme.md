# Beyond Read-It-Later: Leveraging Readwise AI Features for Personal Knowledge Management

This project provides tools to export reading content from Readwise and transform it into a professional-looking newsletter. The project consists of two main scripts:

1. `readwise_export.py` - Exports content from Readwise based on a date range
2. `generate_newsletter.py` - Creates a professional HTML newsletter from the exported content

## Requirements

- Python 3.7+
- Readwise API token
- OpenAI API key

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Medium_Articles.git
   cd Medium_Articles/Beyond_Read_It_Later_Leveraging_Readwise_AI_Features_for_Personal_Knowledge_Management
   ```

2. Install required dependencies:
   ```
   pip install requests python-dotenv reportlab jinja2 openai
   ```

3. Create a `.env` file in the project directory with your API keys:
   ```
   READWISE_TOKEN=your_readwise_api_token
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Step 1: Export Readwise Content

```
python readwise_export.py --start-date 2025-01-01 --end-date 2025-01-31 --debug
```

Parameters:
- `--start-date`: Start date in YYYY-MM-DD format
- `--end-date`: End date in YYYY-MM-DD format
- `--date-field`: Which date field to filter by (choices: saved, published, last_opened, last_status)
- `--debug`: Enable detailed debug output
- `--try-all`: Try all date fields and use the one that returns the most results
- `--max-date-range`: Allow very large date ranges without warnings

This will create a JSON file named `readwise_summaries_YYYY-MM-DD_to_YYYY-MM-DD.json` containing all your Readwise content within the specified date range.

### Step 2: Generate Newsletter

```
python generate_newsletter.py --input readwise_summaries_2025-01-01_to_2025-01-31.json --output professional_newsletter.html
```

Parameters:
- `--input`: Input JSON file from Readwise export (default: `readwise_summaries_2025-01-01_to_2025-01-20.json`)
- `--output`: Output HTML file for the newsletter (default: `professional_newsletter.html`)

## Features

### Readwise Export
- Exports articles, tweets, and other content from Readwise
- Filters by date range
- Handles pagination for large exports
- Multiple date field filtering options
- JSON and PDF output formats

### Newsletter Generator
- AI-powered content organization and summarization
- Automatically groups content by themes
- Generates executive summaries and key takeaways
- Professional HTML layout with modern styling
- Smart source attribution based on content type

## How It Works

1. The Readwise export script connects to the Readwise API to fetch your reading content
2. Content is filtered by date range and saved to JSON and PDF formats
3. The newsletter generator reads this JSON data
4. Content is grouped by theme using keyword analysis
5. OpenAI's GPT models generate professional summaries and insights for each theme
6. A Jinja2 template transforms everything into a clean, professional HTML newsletter

## Troubleshooting

- **API Connection Issues**: Ensure your API keys are correct in the `.env` file
- **No Content Found**: Try different date ranges or date fields with the `--try-all` option
- **Date Range Issues**: Readwise may limit results to recent content; use smaller date ranges
- **OpenAI Errors**: If OpenAI API fails, the script will use fallback content

## Newsletter Example

The generated newsletter will look like this:

![Newsletter Example](https://github.com/Laksh-star/Medium_Articles/raw/main/Beyond_Read_It_Later_Leveraging_Readwise_AI_Features_for_Personal_Knowledge_Management/newsletter_example.png)

## About Personal Knowledge Management with Readwise

This project is part of a broader exploration of how to leverage Readwise for personal knowledge management. Readwise isn't just a read-it-later app - it's a powerful tool for capturing, processing, and synthesizing information from various sources.

By automating the creation of themed newsletters from your reading material, you can:

1. Identify patterns in your reading habits
2. Discover connections between seemingly unrelated content
3. Create a valuable archive of curated knowledge
4. Share insights with others in a professional format

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Readwise](https://readwise.io/) for the content aggregation platform
- [OpenAI](https://openai.com/) for the GPT API used for content summarization
- [Jinja2](https://jinja.palletsprojects.com/) for HTML templating
