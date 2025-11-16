
# Anthropic Claude: Structured Output & Tool Use Examples

This repository contains Python notebooks demonstrating how to get reliable, structured data (JSON) and build agentic workflows using the Anthropic Claude API.

These examples use the `betas=["structured-outputs-2025-11-13"]` features.

## Notebooks

### 1\. `Claude_Structured_Ouptuts_1.ipynb`

  * **Focus:** Forced JSON Output (`output_format`)
  * **Description:** This notebook shows how to force Claude's response to perfectly match a specific JSON schema. This is ideal for parsing unstructured text into a clean, predictable format.
  * **Examples:**
      * Extracting a person's info (name, age, hobbies) from a bio.
      * Parsing an email order confirmation into a nested JSON object.
      * Batch-processing support emails into a structured `tickets.csv` file using `pandas`.

### 2\. `Claude_Structured_Output_2.ipynb`

  * **Focus:** Strict Tool Use (`tools`)
  * **Description:** This notebook demonstrates an agentic workflow. Claude analyzes a user's request, decides which "tools" (functions) to call, and generates the arguments for them, matching a provided schema.
  * **Examples:**
      * A customer support message ("My internet is down") triggers Claude to call `classify_issue` and `generate_ticket_fields`.
      * Sending the (fake) tool results back to Claude.
      * Asking Claude to summarize the tool results into a final, structured JSON ticket.

## How to Run

1.  **Install dependencies:**

    ```bash
    pip install anthropic pandas
    ```

2.  **Get an API Key:**

      * You will need an API key from [Anthropic](https://console.anthropic.com/).

3.  **Run the Notebook:**

      * Open either `.ipynb` file in an environment like Google Colab, VS Code, or Jupyter.
      * Run the first code cell. It will securely prompt you to enter your API key.
