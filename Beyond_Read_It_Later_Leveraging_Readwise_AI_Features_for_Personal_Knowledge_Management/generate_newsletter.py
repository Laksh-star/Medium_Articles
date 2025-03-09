import json
import os
import sys
from datetime import datetime
from collections import defaultdict
import html
from dotenv import load_dotenv
from jinja2 import Template

# Try importing OpenAI with both new and old client options
try:
    from openai import OpenAI  # New client
    USE_NEW_CLIENT = True
    print("Using new OpenAI client")
except ImportError:
    try:
        import openai  # Old client
        USE_NEW_CLIENT = False
        print("Using legacy OpenAI client")
    except ImportError:
        print("ERROR: OpenAI module not found. Please install with: pip install openai")
        sys.exit(1)

load_dotenv()

class NewsletterGenerator:
    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        if not self.openai_api_key:
            raise ValueError("Please set your OPENAI_API_KEY in the .env file")
        
        # Initialize the appropriate client
        if USE_NEW_CLIENT:
            self.client = OpenAI(api_key=self.openai_api_key)
        else:
            openai.api_key = self.openai_api_key
        
        # Test API connection
        print("Testing OpenAI API connection...")
        try:
            if USE_NEW_CLIENT:
                test_response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": "Hello"}],
                    max_tokens=5
                )
            else:
                test_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": "Hello"}],
                    max_tokens=5
                )
            print("✅ OpenAI API connection successful")
        except Exception as e:
            print(f"⚠️ WARNING: OpenAI API connection failed: {str(e)}")
            print("The script will use fallback content instead of AI-generated content.")
            print("Check your API key and network connection.")
    
    def clean_text(self, text):
        """Clean text by decoding HTML entities and handling special characters"""
        if text is None:
            return ""
            
        # First decode HTML entities
        text = html.unescape(text)
        
        # Replace common problematic characters
        replacements = {
            '"': '"',
            '"': '"',
            ''': "'",
            ''': "'",
            '–': '-',
            '—': '-',
            '…': '...',
            '™': '(TM)',
            '®': '(R)',
            '©': '(c)',
            '\u2019': "'",  # Right single quotation mark
            '\u2018': "'",  # Left single quotation mark
            '\u2013': "-",  # En dash
            '\u2014': "-",  # Em dash
            '\u2026': "...", # Horizontal ellipsis
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
            
        # Remove any remaining non-ASCII characters
        text = text.encode('ascii', 'ignore').decode('ascii')
        
        return text.strip()
    
    def read_json_data(self, json_file):
        """Read and parse the Readwise JSON export"""
        print(f"Reading data from {json_file}...")
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"Successfully loaded {len(data)} items from JSON file")
                
                # Clean all text fields
                for item in data:
                    item['title'] = self.clean_text(item.get('title'))
                    item['summary'] = self.clean_text(item.get('summary'))
                    item['author'] = self.clean_text(item.get('author'))
                return data
        except FileNotFoundError:
            print(f"ERROR: JSON file '{json_file}' not found.")
            print(f"Current working directory: {os.getcwd()}")
            print("Please make sure you have run readwise_export.py first")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"ERROR: Could not parse '{json_file}' as JSON. The file may be corrupted.")
            sys.exit(1)
    
    def group_by_theme(self, documents):
        """Group documents into professional themes"""
        themes = {
            'Technology & Innovation': ['ai', 'tech', 'innovation', 'software', 'digital'],
            'Business & Strategy': ['business', 'strategy', 'leadership', 'management'],
            'Industry Insights': ['industry', 'market', 'trends', 'analysis'],
            'Future Trends': ['future', 'trends', 'prediction', 'forecast'],
            'Research & Development': ['research', 'science', 'development', 'study']
        }
        
        categorized = defaultdict(list)
        uncategorized = []
        
        for doc in documents:
            # Get the content to analyze
            content = f"{doc.get('title', '')} {doc.get('summary', '')} {doc.get('category', '')}".lower()
            
            # Find the best matching theme
            max_matches = 0
            best_theme = None
            
            for theme, keywords in themes.items():
                matches = sum(1 for keyword in keywords if keyword in content)
                if matches > max_matches:
                    max_matches = matches
                    best_theme = theme
            
            if max_matches > 0:
                categorized[best_theme].append(doc)
            else:
                uncategorized.append(doc)
        
        # Add uncategorized items to the theme with the least articles
        if uncategorized:
            min_theme = min(categorized.items(), key=lambda x: len(x[1]), default=(None, []))
            if min_theme[0]:
                categorized[min_theme[0]].extend(uncategorized)
            else:
                # If no themes exist yet, create a "Featured Stories" theme
                categorized['Featured Stories'] = uncategorized
        
        # Sort themes by number of articles, descending
        return dict(sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True))
    
    def generate_theme_content(self, theme, articles):
        """Generate professional content for a theme using OpenAI"""
        if theme == 'Other Insights':
            # For Other Insights, create a simple summary without using GPT
            return f"""
            <h3>Additional Notable Articles</h3>
            <p>This section contains additional articles that cover various topics of interest. 
            Browse through these pieces for diverse perspectives and insights across different domains.</p>
            """
        
        articles_text = "\n".join([
            f"Title: {article.get('title', 'Untitled')}\n"
            f"Summary: {article.get('summary', 'No summary available')}\n"
            for article in articles[:5]
        ])
        
        prompt = f"""As a professional newsletter curator, create a compelling section for {theme}. 
        The audience consists of business professionals, industry leaders, and decision-makers.
        
        Required format:
        1. An executive summary (2-3 sentences) highlighting key developments and their business implications
        2. 2-3 key takeaways that professionals should be aware of as bullet points
        3. A forward-looking statement about potential industry impact
        
        IMPORTANT: Format your response using proper HTML tags. Use <p> for paragraphs, <strong> for emphasis, 
        and <ul>/<li> for lists. DO NOT include any markdown formatting, backticks, or the theme name as a header 
        (the theme name will be added automatically in the template).
        
        Tone: Professional, analytical, and focused on business value
        Length: Around 200 words
        
        Source material:
        {articles_text}"""
        
        try:
            print(f"Generating content for theme: {theme}...")
            
            if USE_NEW_CLIENT:
                # Use new OpenAI client
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",  # Updated to correct model name
                    messages=[
                        {"role": "system", "content": "You are a professional business analyst and newsletter curator. Format your responses in clean HTML without markdown syntax, backticks, or code blocks. Do not include the section title in your response as it will be added automatically."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=800
                )
                content = response.choices[0].message.content
            else:
                # Use legacy OpenAI client
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",  # Updated to correct model name
                    messages=[
                        {"role": "system", "content": "You are a professional business analyst and newsletter curator. Format your responses in clean HTML without markdown syntax, backticks, or code blocks. Do not include the section title in your response as it will be added automatically."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=800
                )
                content = response.choices[0].message.content
            
            print(f"Successfully generated content for {theme} ({len(content)} chars)")
            
            # Clean up content by removing code blocks, backticks, and duplicate headings
            content = self.clean_generated_content(content, theme)
                
            return content
            
        except Exception as e:
            # Log the error and use fallback content
            print(f"ERROR generating content for {theme}: {str(e)}")
            print("Using fallback content instead")
            return f"""
            <p>This section features important developments in {theme}. 
            Browse through the articles below for detailed insights and analysis.</p>
            """
    
    def clean_generated_content(self, content, theme):
        """Clean up AI-generated content to remove common formatting issues"""
        # Remove code block markers
        content = content.replace('```html', '')
        content = content.replace('```', '')
        
        # Remove theme name if it appears as a heading
        theme_variations = [
            f"<h1>{theme}</h1>",
            f"<h2>{theme}</h2>",
            f"<h3>{theme}</h3>",
            f"<h4>{theme}</h4>",
            f"<h5>{theme}</h5>",
            f"<h6>{theme}</h6>",
            f"# {theme}",
            f"## {theme}",
            f"### {theme}",
            f"#### {theme}",
            f"##### {theme}",
            f"###### {theme}",
            f"<strong>{theme}</strong>",
            f"**{theme}**"
        ]
        
        for variation in theme_variations:
            content = content.replace(variation, '')
        
        # Convert markdown to HTML if needed
        if '**' in content or '#' in content or '*' in content or '- ' in content or '1. ' in content:
            content = self.markdown_to_html(content)
        
        # Fix any unclosed tags
        if '<ul>' in content and '</ul>' not in content:
            content += '</ul>'
        if '<ol>' in content and '</ol>' not in content:
            content += '</ol>'
        if '<li>' in content and '</li>' not in content:
            content = content.replace('<li>', '<li></li>')
        
        # Ensure content starts with paragraph if not starting with a tag
        if not content.strip().startswith('<'):
            content = f"<p>{content.strip()}</p>"
        
        # Remove excessive whitespace
        content = content.strip()
        
        return content
            
    def markdown_to_html(self, text):
        """Convert common markdown patterns to HTML"""
        # Convert headers
        for i in range(6, 0, -1):
            pattern = '\n' + '#' * i + ' '
            replacement = f'\n<h{i}>'
            text = text.replace(pattern, replacement)
            if f'<h{i}>' in text and not f'</h{i}>' in text:
                text = text.replace('\n', f'</h{i}>\n', 1)
        
        # Convert bold
        text = text.replace('**', '<strong>', 1)
        while '**' in text:
            text = text.replace('**', '</strong>', 1)
            if '**' in text:
                text = text.replace('**', '<strong>', 1)
        
        # Convert italic
        text = text.replace('*', '<em>', 1)
        while '*' in text:
            text = text.replace('*', '</em>', 1)
            if '*' in text:
                text = text.replace('*', '<em>', 1)
        
        # Convert lists
        text = text.replace('\n1. ', '\n<ol>\n<li>')
        text = text.replace('\n2. ', '\n<li>')
        text = text.replace('\n3. ', '\n<li>')
        if '<li>' in text and not '</ol>' in text:
            text = text + '\n</li>\n</ol>'
        
        text = text.replace('\n- ', '\n<ul>\n<li>')
        text = text.replace('\n* ', '\n<ul>\n<li>')
        if '<ul>' in text and not '</ul>' in text:
            text = text + '\n</li>\n</ul>'
        
        # Convert paragraphs
        paragraphs = text.split('\n\n')
        for i, paragraph in enumerate(paragraphs):
            if not paragraph.strip().startswith('<') and paragraph.strip():
                paragraphs[i] = f'<p>{paragraph}</p>'
        
        return '\n\n'.join(paragraphs)
    
    def select_featured_articles(self, articles, count=3):
        """Select the most impactful articles for featuring"""
        # Sort by length of summary as a proxy for article depth
        return sorted(articles, 
                     key=lambda x: len(str(x.get('summary', ''))) if x.get('summary') is not None else 0, 
                     reverse=True)[:count]
    
    def get_source_link_text(self, article):
        """Get appropriate link text based on content type"""
        category = str(article.get('category', '')).lower()
        
        if 'tweet' in category or 'twitter' in category:
            return 'View Tweet'
        elif 'video' in category or 'youtube' in category:
            return 'Watch Video'
        elif 'podcast' in category or 'audio' in category:
            return 'Listen Now'
        elif 'paper' in category or 'research' in category:
            return 'Read Paper'
        elif 'book' in category:
            return 'View Book'
        elif 'discussion' in category or 'forum' in category:
            return 'Join Discussion'
        else:
            return 'Read More'
    
    def generate_newsletter(self, json_file, output_file):
        """Generate the professional newsletter"""
        # Read data
        documents = self.read_json_data(json_file)
        
        # Group by theme
        print("Grouping documents by theme...")
        themed_docs = self.group_by_theme(documents)
        print(f"Organized into {len(themed_docs)} themes")
        
        # Generate content for each theme
        print("Generating content for each theme...")
        newsletter_sections = {}
        for theme, articles in themed_docs.items():
            print(f"Processing theme: {theme} ({len(articles)} articles)")
            newsletter_sections[theme] = {
                'content': self.generate_theme_content(theme, articles),
                'featured_articles': self.select_featured_articles(articles)
            }
        
        # Load newsletter template
        template = Template('''
<!DOCTYPE html>
<html>
<head>
    <title>The Innovation Pulse</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
            color: #2d3748;
            background-color: #f7fafc;
        }
        .header {
            text-align: center;
            padding: 40px 0;
            margin-bottom: 40px;
            border-bottom: 3px solid #2b6cb0;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .header h1 {
            color: #2b6cb0;
            font-size: 2.8em;
            margin: 0;
            font-weight: 800;
        }
        .header .tagline {
            color: #4a5568;
            font-size: 1.4em;
            margin: 15px 0;
            font-style: italic;
        }
        .header .date {
            color: #718096;
            font-size: 1.1em;
            margin: 10px 0;
        }
        .intro {
            background: linear-gradient(135deg, #2b6cb0 0%, #4299e1 100%);
            color: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .intro h2 {
            margin: 0 0 15px 0;
            font-size: 1.6em;
        }
        .intro p {
            margin: 0;
            font-size: 1.1em;
            line-height: 1.6;
        }
        .theme-section {
            background: white;
            margin: 30px 0;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .theme-title {
            color: #2c5282;
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e2e8f0;
        }
        .theme-content {
            margin-bottom: 30px;
            font-size: 1.1em;
            color: #4a5568;
        }
        .featured-articles {
            background: #f8fafc;
            padding: 20px;
            border-radius: 6px;
        }
        .featured-title {
            color: #2b6cb0;
            font-size: 1.3em;
            margin-bottom: 15px;
        }
        .article {
            margin: 15px 0;
            padding: 20px;
            background: white;
            border-radius: 6px;
            border-left: 4px solid #2b6cb0;
        }
        .article h3 {
            margin: 0 0 10px 0;
            color: #2c5282;
            font-size: 1.2em;
        }
        .article-link {
            display: inline-block;
            margin-top: 15px;
            color: #2b6cb0;
            text-decoration: none;
            font-size: 0.95em;
            font-weight: 500;
            transition: color 0.2s;
        }
        .article-link:hover {
            color: #1a4971;
        }
        .article-link::after {
            content: " \\2192";  /* Unicode right arrow */
            font-size: 1.1em;
        }
        .metadata {
            font-size: 0.9em;
            color: #718096;
            margin: 8px 0;
        }
        .summary {
            margin: 10px 0;
            color: #4a5568;
            font-size: 1em;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 30px 20px;
            border-top: 1px solid #e2e8f0;
            color: #718096;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .footer .curator {
            font-size: 1.1em;
            color: #4a5568;
            margin-bottom: 15px;
        }
        .footer .curator strong {
            color: #2b6cb0;
        }
        .footer .powered-by {
            font-size: 0.9em;
            color: #718096;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>The Innovation Pulse</h1>
        <div class="tagline">Where Tomorrow's Ideas Meet Today's Leaders</div>
        <div class="date">{{ date }}</div>
    </div>

    <div class="intro">
        <h2>Welcome to This Week's Innovation Pulse</h2>
        <p>In this curated edition, we dive deep into groundbreaking developments and emerging trends that are reshaping our world. From cutting-edge tech innovations to strategic business insights, we've handpicked the stories that matter most to forward-thinking leaders like you.</p>
    </div>

    {% for theme, data in sections.items() %}
    <div class="theme-section">
        <h2 class="theme-title">{{ theme }}</h2>
        <div class="theme-content">
            {{ data.content | safe }}
        </div>
        
        <div class="featured-articles">
            <h3 class="featured-title">Featured Articles</h3>
            {% for article in data.featured_articles %}
            <div class="article">
                <h3>{{ article.title or "Untitled" }}</h3>
                <div class="metadata">
                    {% if article.author %}By {{ article.author }}{% endif %}
                    {% if article.created_at %} | {{ article.created_at.split('T')[0] }}{% endif %}
                </div>
                {% if article.summary %}
                <div class="summary">
                    {{ article.summary[:200] }}...
                </div>
                {% endif %}
                <a href="{{ article.source_url }}" class="article-link" target="_blank">{{ get_source_link_text(article) }}</a>
            </div>
            {% endfor %}
        </div>
    </div>
    {% endfor %}

    <div class="footer">
        <div class="curator">Curated by <strong>Lakshmi Narayana</strong></div>
        <div class="powered-by">Enhanced with advanced AI analysis to bring you the most relevant insights</div>
        <p> {{ date.split(',')[1] }} The Innovation Pulse</p>
    </div>
</body>
</html>
        ''')
        
        # Generate HTML with the source link text function available to the template
        print("Generating HTML newsletter...")
        html_content = template.render(
            sections=newsletter_sections,
            date=datetime.now().strftime('%B %d, %Y'),
            get_source_link_text=self.get_source_link_text
        )
        
        # Save to file
        print(f"Saving newsletter to {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Newsletter successfully generated: {output_file}")
        return output_file

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate a professional newsletter from Readwise exported data')
    parser.add_argument('--input', default='/content/readwise_summaries_2025-02-01_to_2025-02-10.json', 
                        help='Input JSON file from Readwise export (default: readwise_summaries_2025-01-01_to_2025-01-20.json)')
    parser.add_argument('--output', default='professional_newsletter.html',
                        help='Output HTML file for the newsletter (default: professional_newsletter.html)')
    
    args = parser.parse_args()
    
    print(f"Newsletter Generator v1.1")
    print(f"========================")
    
    # Initialize generator
    try:
        generator = NewsletterGenerator()
        
        # Generate newsletter
        generated_file = generator.generate_newsletter(args.input, args.output)
        print(f"========================")
        print(f"Professional newsletter generated successfully: {generated_file}")
        print(f"Open this file in your browser to view the newsletter.")
    except Exception as e:
        print(f"ERROR: Newsletter generation failed: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()