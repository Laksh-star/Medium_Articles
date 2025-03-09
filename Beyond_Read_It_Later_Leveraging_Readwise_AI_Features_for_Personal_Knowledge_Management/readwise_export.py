import os
import json
from datetime import datetime, timezone
import requests
from dotenv import load_dotenv
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

load_dotenv()

class ReadwiseExporter:
    def __init__(self, debug=False):
        self.api_token = os.getenv('READWISE_TOKEN')
        if not self.api_token:
            raise ValueError("Please set your READWISE_TOKEN in the .env file")
        self.base_url = "https://readwise.io/api/v3"
        self.headers = {
            'Authorization': f'Token {self.api_token}'
        }
        self.debug = debug

    def get_documents(self, start_date, end_date, date_field='saved'):
        """
        Fetch documents from Readwise within the specified date range
        Dates should be in ISO format: YYYY-MM-DD
        
        date_field options: 'saved', 'last_opened', 'published', 'last_status'
        """
        print(f"Fetching documents with {date_field} date between {start_date} and {end_date}")
        
        documents = []
        url = f"{self.base_url}/list"
        
        # Use the correct date field and operators according to API documentation
        params = {
            f"{date_field}__after": start_date,
            f"{date_field}__before": end_date,
            "page_size": 250  # Request maximum page size to reduce number of API calls
        }
        
        if self.debug:
            print(f"Using API parameters: {params}")
        
        page_count = 0
        total_results = 0
        
        while url:
            page_count += 1
            print(f"Fetching page {page_count}...")
            
            try:
                response = requests.get(url, headers=self.headers, params=params)
                response.raise_for_status()  # Raise exception for 4XX/5XX errors
            except requests.exceptions.RequestException as e:
                print(f"API request failed: {str(e)}")
                if hasattr(e, 'response') and hasattr(e.response, 'text'):
                    print(f"Response: {e.response.text}")
                raise
            
            data = response.json()
            
            # Check if we have pagination info
            if 'count' in data and page_count == 1:
                total_results = data.get('count', 0)
                print(f"API reports {total_results} total documents match the criteria")
            
            results_count = len(data.get('results', []))
            print(f"Page {page_count} contains {results_count} documents")
            
            if self.debug and page_count == 1 and results_count > 0:
                first_doc = data['results'][0]
                print(f"First document: '{first_doc.get('title')}', saved: {first_doc.get('saved_at')}, created: {first_doc.get('created_at')}")
            
            documents.extend(data.get('results', []))
            
            # Get next page URL, if any
            url = data.get('next')
            
            # For pagination requests, clear params as they're already in the next URL
            params = {}
        
        print(f"Retrieved {len(documents)} documents from {page_count} pages")
        
        # Sort documents by saved_at or created_at date
        sort_field = 'saved_at' if date_field == 'saved' else ('created_at' if date_field == 'published' else date_field + '_at')
        documents.sort(key=lambda x: x.get(sort_field, '0') if x.get(sort_field) else '0', reverse=False)
        
        return documents

    def try_all_date_fields(self, start_date, end_date):
        """Try fetching with all possible date fields and return the best results"""
        date_fields = ['saved', 'published', 'last_opened', 'last_status']
        best_results = []
        best_field = None
        
        for field in date_fields:
            print(f"\nTrying with date field: {field}")
            try:
                results = self.get_documents(start_date, end_date, date_field=field)
                print(f"Found {len(results)} documents with {field} date field")
                
                # If we found documents and it's more than our previous best, save these results
                if len(results) > len(best_results):
                    best_results = results
                    best_field = field
            except Exception as e:
                print(f"Error with {field} field: {str(e)}")
        
        if best_field:
            print(f"\nUsing results from '{best_field}' date field which returned {len(best_results)} documents")
        else:
            print("\nNo documents found with any date field")
            
        return best_results

    def save_to_json(self, documents, filename):
        """Save documents to a JSON file"""
        if not documents:
            print("No documents to save to JSON.")
            return
            
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(documents, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(documents)} documents to {filename}")

    def save_to_pdf(self, documents, filename):
        """Save documents to a PDF file using reportlab"""
        if not documents:
            print("No documents to save to PDF.")
            return
            
        pdf_doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Create custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=16,
            spaceAfter=30
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=12
        )
        
        metadata_style = ParagraphStyle(
            'CustomMetadata',
            parent=styles['Italic'],
            fontSize=10,
            textColor=colors.gray,
            spaceAfter=6
        )
        
        url_style = ParagraphStyle(
            'CustomURL',
            parent=styles['Italic'],
            fontSize=10,
            textColor=colors.blue,
            spaceAfter=6
        )
        
        category_style = ParagraphStyle(
            'CustomCategory',
            parent=styles['Italic'],
            fontSize=10,
            textColor=colors.blue,
            spaceAfter=12
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=20
        )
        
        # Build the PDF content
        story = []
        
        # Add main title
        story.append(Paragraph("Readwise Document Summaries", title_style))
        story.append(Spacer(1, 20))
        
        # Add date range information
        story.append(Paragraph(f"Date Range: {start_date} to {end_date}", metadata_style))
        story.append(Spacer(1, 20))
        
        for document in documents:
            # Document title
            title = str(document.get('title', 'Untitled') or 'Untitled')
            story.append(Paragraph(title, heading_style))
            
            # Metadata: Source and Author
            source = str(document.get('source') or 'Unknown')
            author = str(document.get('author') or 'Unknown')
            metadata = f"Source: {source} | Author: {author}"
            story.append(Paragraph(metadata, metadata_style))
            
            # URL as clickable link
            url = document.get('url') or document.get('source_url')
            if url:
                link_text = f'<link href="{url}"><u>View Original Source</u></link>'
                story.append(Paragraph(link_text, url_style))
            
            # Date and Category
            saved_at = document.get('saved_at')
            created_at = document.get('created_at')
            date_str = saved_at or created_at
            
            if date_str:
                try:
                    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                    formatted_date = date_obj.strftime('%B %d, %Y %I:%M %p')
                except (ValueError, AttributeError):
                    formatted_date = 'Unknown Date'
            else:
                formatted_date = 'Unknown Date'
                
            category = str(document.get('category') or 'Uncategorized')
            category = category.title()
            
            date_category = f"Date: {formatted_date} | Category: {category}"
            story.append(Paragraph(date_category, category_style))
            
            # Summary
            summary = str(document.get('summary') or 'No summary available')
            story.append(Paragraph(summary, body_style))
            
            story.append(Spacer(1, 20))
        
        # Build the PDF
        pdf_doc.build(story)
        print(f"Saved PDF file: {filename}")


def validate_date_format(date_str):
    """Validate that the date string is in YYYY-MM-DD format"""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def main(start_date, end_date, date_field=None, debug=False, try_all=False, max_date_range=False):
    # Validate date format
    if not validate_date_format(start_date) or not validate_date_format(end_date):
        print("Error: Dates must be in YYYY-MM-DD format")
        return
    
    exporter = ReadwiseExporter(debug=debug)
    
    try:
        # Print a warning if the date range is very large
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
        days_difference = (end_dt - start_dt).days
        
        if days_difference > 90 and not max_date_range:
            print(f"\n⚠️ Warning: You're requesting documents over a {days_difference} day period.")
            print("The Readwise API might limit results to the most recent documents.")
            print("Consider using smaller date ranges for better results.")
            print("If you want to proceed anyway, use the --max-date-range flag.\n")
            
            # Suggest a smaller date range
            if days_difference > 180:
                print(f"Suggestion: Try a 30-day range instead: --start-date {end_date} --end-date {(end_dt + datetime.timedelta(days=30)).strftime('%Y-%m-%d')}")
            return
        
        if try_all:
            documents = exporter.try_all_date_fields(start_date, end_date)
        else:
            if date_field:
                documents = exporter.get_documents(start_date, end_date, date_field=date_field)
            else:
                documents = exporter.get_documents(start_date, end_date)  # Default to 'saved'
        
        if not documents:
            print(f"No documents found between {start_date} and {end_date}")
            return
        
        print(f"Found {len(documents)} documents between {start_date} and {end_date}")
        
        # Date range analysis of the received documents
        if documents:
            # Find earliest and latest dates in the returned documents
            earliest_date = None
            latest_date = None
            date_fields = ['saved_at', 'created_at', 'updated_at', 'published_date']
            
            for doc in documents:
                for field in date_fields:
                    if doc.get(field):
                        date_str = doc.get(field)
                        if isinstance(date_str, str):
                            try:
                                # Convert to datetime for comparison
                                if 'T' in date_str:  # ISO format
                                    date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                                else:  # Handle other formats
                                    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                                
                                if earliest_date is None or date_obj < earliest_date:
                                    earliest_date = date_obj
                                if latest_date is None or date_obj > latest_date:
                                    latest_date = date_obj
                            except (ValueError, TypeError):
                                continue
            
            if earliest_date and latest_date:
                print(f"Document date range: {earliest_date.strftime('%Y-%m-%d')} to {latest_date.strftime('%Y-%m-%d')}")
                
                # Check if the returned dates match the requested range
                requested_start = datetime.strptime(start_date, '%Y-%m-%d')
                requested_end = datetime.strptime(end_date, '%Y-%m-%d')
                
                if abs((earliest_date.date() - requested_start.date()).days) > 7 or \
                   abs((latest_date.date() - requested_end.date()).days) > 7:
                    print("\n⚠️ Warning: The dates of returned documents don't match your requested range.")
                    print("This may indicate the API is limiting results to recent documents.")
                    print("Try using a smaller date range closer to the dates of the returned documents.")
        
        # Display the first few documents for verification
        if documents and debug:
            print("\nFirst 3 documents:")
            for i, doc in enumerate(documents[:3]):
                print(f"{i+1}. '{doc.get('title')}' - Saved: {doc.get('saved_at')}, Created: {doc.get('created_at')}")
            
            # Also show the last document to help understand the date range
            if len(documents) > 3:
                print(f"Last document: '{documents[-1].get('title')}' - " + 
                      f"Saved: {documents[-1].get('saved_at')}, Created: {documents[-1].get('created_at')}")
        
        # Save to JSON
        json_filename = f"readwise_summaries_{start_date}_to_{end_date}.json"
        exporter.save_to_json(documents, json_filename)
        
        # Save to PDF
        pdf_filename = f"readwise_summaries_{start_date}_to_{end_date}.pdf"
        exporter.save_to_pdf(documents, pdf_filename)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Export Readwise documents within a date range')
    parser.add_argument('--start-date', required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--end-date', required=True, help='End date in YYYY-MM-DD format')
    parser.add_argument('--date-field', choices=['saved', 'published', 'last_opened', 'last_status'],
                       help='Which date field to filter by (default: saved)')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--try-all', action='store_true', 
                       help='Try all date fields and use the one that returns the most results')
    parser.add_argument('--max-date-range', action='store_true',
                       help='Allow very large date ranges without warnings')
    
    args = parser.parse_args()
    main(args.start_date, args.end_date, date_field=args.date_field, 
         debug=args.debug, try_all=args.try_all, max_date_range=args.max_date_range)