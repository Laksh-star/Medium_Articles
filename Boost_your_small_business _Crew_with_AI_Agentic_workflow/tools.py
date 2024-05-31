import os
import openai
from crewai_tools import BaseTool
from openai import OpenAI
client =OpenAI()
class DocumentSummarizationTool(BaseTool):
    name: str = "Document Summarization Tool"
    description: str = "Summarizes the content of a specified file into a concise summary."

    def _run(self, file_path: str) -> str:
        # Read the content of the specified file
        try:
            with open(file_path, 'r') as file:
                document = file.read()
        except FileNotFoundError:
            return f"Error: File {file_path} not found."
        except Exception as e:
            return f"Error: {str(e)}"

        # Summarize the document content
        #response = openai.Completion.create(
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
        prompt=f"Summarize the following document in themes and bullet points:\n\n{document}\n\nSummary:",
        max_tokens=150)
        summary = response.choices[0].text.strip()
        return summary
