

from smolagents import tool, CodeAgent, HfApiModel
import arxiv
from typing import List, Dict, Any
from collections import Counter
import re
from datetime import datetime

@tool
def search_papers(query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """
    Searches for academic papers on ArXiv with business relevance

    Args:
        query: Search query string
        max_results: Maximum number of papers to retrieve

    Returns:
        List of relevant papers with metadata
    """
    papers = []
    client = arxiv.Client()
    # Enhance query with business-related terms
    business_query = f"{query} AND (industry OR commercial OR business OR market OR application)"
    search = arxiv.Search(
        query=business_query,
        max_results=max_results
    )

    for result in client.results(search):
        papers.append({
            'title': result.title,
            'authors': [str(author) for author in result.authors],
            'year': result.published.year,
            'abstract': result.summary,
            'id': result.entry_id,
            'categories': result.categories
        })

    return papers

@tool
def analyze_market_potential(papers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyzes market potential and business implications

    Args:
        papers: List of research papers

    Returns:
        Comprehensive market analysis
    """
    analysis = {
        'market_segments': [],
        'business_models': [],
        'revenue_streams': [],
        'key_players': [],
        'competitive_advantages': [],
        'market_drivers': [],
        'market_barriers': [],
        'maturity_assessment': {
            'research_stage': [],
            'prototype_stage': [],
            'market_ready': []
        }
    }

    # Market analysis keywords
    market_keywords = {
        'segments': ['segment', 'sector', 'industry', 'vertical', 'market'],
        'business_models': ['business model', 'monetization', 'revenue', 'commercial'],
        'advantages': ['advantage', 'unique', 'superior', 'better', 'improve'],
        'drivers': ['driver', 'trend', 'growth', 'demand', 'need'],
        'barriers': ['barrier', 'challenge', 'limitation', 'constraint', 'problem']
    }

    for paper in papers:
        text = f"{paper['title']} {paper['abstract']}"

        # Extract market segments
        for keyword in market_keywords['segments']:
            matches = re.findall(f"{keyword}.*?(?=[.!?])", text.lower())
            analysis['market_segments'].extend(matches)

        # Identify business models
        for keyword in market_keywords['business_models']:
            matches = re.findall(f"{keyword}.*?(?=[.!?])", text.lower())
            analysis['business_models'].extend(matches)

        # Extract competitive advantages
        for keyword in market_keywords['advantages']:
            matches = re.findall(f"{keyword}.*?(?=[.!?])", text.lower())
            analysis['competitive_advantages'].extend(matches)

        # Identify market drivers
        for keyword in market_keywords['drivers']:
            matches = re.findall(f"{keyword}.*?(?=[.!?])", text.lower())
            analysis['market_drivers'].extend(matches)

        # Extract market barriers
        for keyword in market_keywords['barriers']:
            matches = re.findall(f"{keyword}.*?(?=[.!?])", text.lower())
            analysis['market_barriers'].extend(matches)

        # Assess technology maturity
        if any(word in text.lower() for word in ['implemented', 'deployed', 'commercial', 'product']):
            analysis['maturity_assessment']['market_ready'].append(paper['title'])
        elif any(word in text.lower() for word in ['prototype', 'demonstration', 'testing']):
            analysis['maturity_assessment']['prototype_stage'].append(paper['title'])
        else:
            analysis['maturity_assessment']['research_stage'].append(paper['title'])

    return analysis

@tool
def generate_business_report(papers: List[Dict[str, Any]], market_analysis: Dict[str, Any]) -> str:
    """
    Generates comprehensive business report

    Args:
        papers: List of research papers
        market_analysis: Market potential analysis

    Returns:
        Detailed business report in markdown format
    """
    report = "# Business Opportunity Analysis Report\n\n"

    # Executive Summary
    report += "## Executive Summary\n"
    report += f"Analysis based on {len(papers)} research publications from {min(p['year'] for p in papers)} "
    report += f"to {max(p['year'] for p in papers)}, focusing on market potential and business opportunities.\n\n"

    # Market Overview
    report += "## Market Overview\n"
    # Group papers by year
    papers_by_year = {}
    for paper in papers:
        year = paper['year']
        if year not in papers_by_year:
            papers_by_year[year] = []
        papers_by_year[year].append(paper)

    # Recent Developments
    report += "### Recent Developments\n"
    for year in sorted(papers_by_year.keys(), reverse=True):
        for paper in papers_by_year[year]:
            report += f"- ({year}) {paper['title']}\n"
            # Extract key findings from abstract
            key_findings = re.findall(r'(?:result|show|demonstrate|achieve|improve).*?(?=[.!?])', paper['abstract'].lower())
            if key_findings:
                report += "  - Key Finding: " + key_findings[0].capitalize() + "\n"
    report += "\n"

    # Market Potential
    report += "## Market Potential\n"

    # Market Segments
    if market_analysis['market_segments']:
        report += "### Target Market Segments\n"
        unique_segments = list(set(market_analysis['market_segments']))
        for segment in unique_segments[:5]:  # Top 5 segments
            report += f"- {segment.capitalize()}\n"
    report += "\n"

    # Business Models
    if market_analysis['business_models']:
        report += "### Potential Business Models\n"
        unique_models = list(set(market_analysis['business_models']))
        for model in unique_models[:5]:  # Top 5 models
            report += f"- {model.capitalize()}\n"
    report += "\n"

    # Market Drivers & Growth Factors
    if market_analysis['market_drivers']:
        report += "### Market Drivers\n"
        unique_drivers = list(set(market_analysis['market_drivers']))
        for driver in unique_drivers[:5]:  # Top 5 drivers
            report += f"- {driver.capitalize()}\n"
    report += "\n"

    # Technology Readiness
    report += "## Technology Readiness Assessment\n"

    if market_analysis['maturity_assessment']['market_ready']:
        report += "\n### Market-Ready Solutions\n"
        for tech in market_analysis['maturity_assessment']['market_ready']:
            report += f"- {tech}\n"

    if market_analysis['maturity_assessment']['prototype_stage']:
        report += "\n### In Development (Prototype Stage)\n"
        for tech in market_analysis['maturity_assessment']['prototype_stage']:
            report += f"- {tech}\n"

    if market_analysis['maturity_assessment']['research_stage']:
        report += "\n### Early Research Stage\n"
        for tech in market_analysis['maturity_assessment']['research_stage']:
            report += f"- {tech}\n"

    # Risks and Challenges
    if market_analysis['market_barriers']:
        report += "\n## Risks and Challenges\n"
        unique_barriers = list(set(market_analysis['market_barriers']))
        for barrier in unique_barriers[:5]:  # Top 5 barriers
            report += f"- {barrier.capitalize()}\n"

    # Recommendations
    report += "\n## Recommendations\n"
    report += "Based on the analysis:\n"

    # Generate recommendations based on maturity assessment
    if len(market_analysis['maturity_assessment']['market_ready']) > len(market_analysis['maturity_assessment']['research_stage']):
        report += "- Market is mature for commercial entry\n"
        report += "- Focus on differentiation and competitive advantages\n"
    else:
        report += "- Technology still in early stages\n"
        report += "- Consider R&D investments and strategic partnerships\n"

    return report


####
from smolagents import OpenAIServerModel

def run_business_analysis(query: str, max_papers: int = 10, hf_token: str = None):
    """
    Main function to run the business analysis

    Args:
        query: Search query string
        max_papers: Maximum number of papers to analyze
        hf_token: Hugging Face API token
    """
    #if not hf_token:
    #    raise ValueError("Please provide a Hugging Face API token")
    api_key="lm-studio" 
    model = OpenAIServerModel(
        model_id="deepseek-r1-distill-qwen-7b",
        api_base="http://localhost:1234/v1",
        #api_key=os.environ["OPENAI_API_KEY"],
        api_key=api_key,
    )

    agent = CodeAgent(
        tools=[search_papers, analyze_market_potential, generate_business_report],
        model=model,
        add_base_tools=True
    )

    result = agent.run(
        f"""Analyze the business potential of '{query}' by:
        1. Finding {max_papers} relevant research papers
        2. Analyzing market potential and business implications
        3. Generating a nicely formatted comprehensive business report
        Include specific market segments, business models, and recommendations along with brief 1-3 line summaries of papers,and weblinks."""
    )

    return result

# Run the business analysis
analysis = run_business_analysis(
    query="personal ai digital twin",
    max_papers=3,
    #hf_token="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"
)
print(analysis)