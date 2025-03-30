import anthropic
import pandas as pd
import time
from typing import List, Dict, Any
import re

# Initialize the Anthropic client
# You'll need to replace this with your actual API key
client = anthropic.Anthropic(
    # Replace with your API key
    api_key="your_api_key_here",
)

def extract_couplet(response: str) -> tuple:
    """
    Extract the first and second line from a couplet response.
    Returns a tuple of (first_line, second_line)
    """
    # Clean the response and split by newlines
    lines = response.strip().split('\n')
    
    # Remove any empty lines
    lines = [line for line in lines if line.strip()]
    
    # If we have fewer than 2 lines, return what we have plus empty strings
    if len(lines) == 0:
        return ("", "")
    elif len(lines) == 1:
        return (lines[0], "")
    else:
        # Return the first two non-empty lines
        return (lines[0], lines[1])

def test_base_rhyming(model_name: str = "claude-3-5-haiku-20241022") -> Dict[str, Any]:
    """Generate several rhyming couplets to establish a baseline"""
    
    themes = ["sunset", "ocean", "mountain", "forest", "city"]
    responses = {}
    
    for theme in themes:
        prompt = f"Write a rhyming couplet about a {theme}."
        
        try:
            message = client.messages.create(
                model=model_name,
                max_tokens=300,
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )
            responses[theme] = message.content[0].text
            # Rate limiting to avoid API throttling
            time.sleep(1)
        except Exception as e:
            print(f"Error with theme {theme}: {e}")
            responses[theme] = f"ERROR: {str(e)}"
    
    # Process results
    results = []
    for theme, response in responses.items():
        first_line, second_line = extract_couplet(response)
        results.append({
            "theme": theme,
            "prompt": f"Write a rhyming couplet about a {theme}.",
            "first_line": first_line,
            "second_line": second_line,
            "full_response": response
        })
    
    return {
        "experiment": "base_rhyming",
        "results": results
    }

def test_constrained_rhymes(model_name: str = "claude-3-7-sonnet-20250219") -> Dict[str, Any]:
    """Test if first lines differ when second line endings are constrained"""
    
    # Each theme has multiple required ending words that could plausibly rhyme
    constraints = {
        "sunset": ["light", "sight", "bright", "night"],
        "ocean": ["deep", "sleep", "keep", "leap"],
        "mountain": ["high", "sky", "fly", "by"],
        "forest": ["green", "seen", "between", "queen"],
        "river": ["flow", "know", "glow", "slow"]
    }
    
    responses = {}
    
    for theme, endings in constraints.items():
        # First get unconstrained version
        base_prompt = f"Write a rhyming couplet about a {theme}."
        
        try:
            message = client.messages.create(
                model=model_name,
                max_tokens=300,
                temperature=0,
                messages=[{"role": "user", "content": base_prompt}]
            )
            responses[f"{theme}_base"] = message.content[0].text
            time.sleep(1)
        except Exception as e:
            print(f"Error with theme {theme} base: {e}")
            responses[f"{theme}_base"] = f"ERROR: {str(e)}"
        
        # Then get constrained versions
        for ending in endings:
            constraint_prompt = f"Write a rhyming couplet about a {theme}. The second line must end with the word '{ending}'."
            try:
                message = client.messages.create(
                    model=model_name,
                    max_tokens=300,
                    temperature=0,
                    messages=[{"role": "user", "content": constraint_prompt}]
                )
                responses[f"{theme}_{ending}"] = message.content[0].text
                time.sleep(1)
            except Exception as e:
                print(f"Error with theme {theme} ending {ending}: {e}")
                responses[f"{theme}_{ending}"] = f"ERROR: {str(e)}"
    
    # Process results
    results = []
    for theme, endings in constraints.items():
        # Process base result
        base_key = f"{theme}_base"
        if base_key in responses:
            base_first, base_second = extract_couplet(responses[base_key])
            
            results.append({
                "theme": theme,
                "constraint": "none",
                "prompt": f"Write a rhyming couplet about a {theme}.",
                "first_line": base_first,
                "second_line": base_second,
                "full_response": responses[base_key]
            })
        
        # Process constrained results
        for ending in endings:
            key = f"{theme}_{ending}"
            if key in responses:
                first_line, second_line = extract_couplet(responses[key])
                
                results.append({
                    "theme": theme,
                    "constraint": ending,
                    "prompt": f"Write a rhyming couplet about a {theme}. The second line must end with the word '{ending}'.",
                    "first_line": first_line,
                    "second_line": second_line,
                    "full_response": responses[key]
                })
    
    return {
        "experiment": "constrained_rhymes",
        "results": results
    }

def test_mid_generation_steering(model_name: str = "claude-3-7-sonnet-20250219") -> Dict[str, Any]:
    """
    Test if we can steer the second line by interrupting generation and
    providing a new constraint partway through
    """
    themes = ["sunset", "ocean", "mountain", "forest", "river"]
    responses = {}
    
    for theme in themes:
        # First get Claude to generate just the first line
        first_line_prompt = f"Write the first line of a rhyming couplet about a {theme}. Only write the first line."
        
        try:
            first_line_message = client.messages.create(
                model=model_name,
                max_tokens=100,
                temperature=0,
                messages=[{"role": "user", "content": first_line_prompt}]
            )
            first_line = first_line_message.content[0].text.strip()
            responses[f"{theme}_first_line"] = first_line
            time.sleep(1)
            
            # Now use the same first line but ask for different second lines
            completions = ["natural", "unexpected", "opposite"]
            
            for completion_type in completions:
                second_line_prompt = f"Complete this rhyming couplet with a {completion_type} second line:\n{first_line}"
                
                message = client.messages.create(
                    model=model_name,
                    max_tokens=100,
                    temperature=0,
                    messages=[{"role": "user", "content": second_line_prompt}]
                )
                responses[f"{theme}_{completion_type}"] = message.content[0].text
                time.sleep(1)
                
        except Exception as e:
            print(f"Error with theme {theme}: {e}")
            responses[f"{theme}_first_line"] = f"ERROR: {str(e)}"
    
    # Process results
    results = []
    for theme in themes:
        first_line_key = f"{theme}_first_line"
        if first_line_key in responses and not responses[first_line_key].startswith("ERROR"):
            first_line = responses[first_line_key]
            
            for completion_type in ["natural", "unexpected", "opposite"]:
                key = f"{theme}_{completion_type}"
                if key in responses:
                    second_line = responses[key].strip()
                    
                    results.append({
                        "theme": theme,
                        "completion_type": completion_type,
                        "first_line": first_line,
                        "second_line": second_line,
                        "full_response": first_line + "\n" + second_line
                    })
    
    return {
        "experiment": "mid_generation_steering",
        "results": results
    }

def test_planning_hints(model_name: str = "claude-3-7-sonnet-20250219") -> Dict[str, Any]:
    """
    Ask Claude to explain its planning process for creating rhyming couplets
    """
    prompts = [
        "When you write a rhyming couplet, do you plan the second line's ending before writing the first line? Please explain your process step by step.",
        "Describe how you decide what words to use at the end of each line in a rhyming couplet. Do you think ahead or just write one line at a time?",
        "What mental process do you use to ensure two lines rhyme in a couplet? Do you consider multiple possible endings before starting?",
        "When you're generating a rhyming couplet, do you first think of rhyming words and then construct lines around them, or do you write the first line and then find a rhyme for the second?"
    ]
    
    responses = {}
    
    for i, prompt in enumerate(prompts):
        try:
            message = client.messages.create(
                model=model_name,
                max_tokens=500,
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )
            responses[f"planning_{i}"] = {
                "prompt": prompt,
                "response": message.content[0].text
            }
            time.sleep(1)
        except Exception as e:
            print(f"Error with prompt {i}: {e}")
            responses[f"planning_{i}"] = {
                "prompt": prompt,
                "response": f"ERROR: {str(e)}"
            }
    
    return {
        "experiment": "planning_hints",
        "results": responses
    }

def run_all_experiments(model_name: str = "claude-3-7-sonnet-20250219") -> Dict[str, Any]:
    """Run all experiments and compile results"""
    
    results = {}
    
    print("Running base rhyming experiment...")
    results["base_rhyming"] = test_base_rhyming(model_name)
    
    print("Running constrained rhymes experiment...")
    results["constrained_rhymes"] = test_constrained_rhymes(model_name)
    
    print("Running mid-generation steering experiment...")
    results["mid_generation_steering"] = test_mid_generation_steering(model_name)
    
    print("Running planning hints experiment...")
    results["planning_hints"] = test_planning_hints(model_name)
    
    return results

def analyze_results(results: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze the results and draw conclusions about planning behavior"""
    
    analysis = {}
    
    # Analyze constrained rhymes to see if first lines differ based on second line constraint
    if "constrained_rhymes" in results:
        constrained_data = results["constrained_rhymes"]["results"]
        
        # Convert to DataFrame for easier analysis
        df = pd.DataFrame(constrained_data)
        
        # Group by theme to compare different constraints for the same theme
        theme_groups = df.groupby("theme")
        
        first_line_differences = {}
        for theme, group in theme_groups:
            base_row = group[group["constraint"] == "none"]
            if not base_row.empty:
                base_first_line = base_row.iloc[0]["first_line"]
                
                # Compare each constrained first line to the base first line
                differences = []
                for _, row in group[group["constraint"] != "none"].iterrows():
                    constrained_first_line = row["first_line"]
                    ending = row["constraint"]
                    
                    # Simple difference measure: are they different at all?
                    is_different = base_first_line != constrained_first_line
                    
                    differences.append({
                        "ending": ending,
                        "base_first_line": base_first_line,
                        "constrained_first_line": constrained_first_line,
                        "is_different": is_different
                    })
                
                first_line_differences[theme] = differences
        
        analysis["first_line_differences"] = first_line_differences
        
        # Calculate overall percentage of constrained first lines that differ from base
        different_count = sum(1 for theme_diffs in first_line_differences.values() 
                             for diff in theme_diffs if diff["is_different"])
        total_count = sum(len(theme_diffs) for theme_diffs in first_line_differences.values())
        
        if total_count > 0:
            percent_different = (different_count / total_count) * 100
            analysis["percent_first_lines_different"] = percent_different
            
            # Interpretation
            if percent_different > 75:
                analysis["planning_evidence"] = "Strong evidence of planning: Claude consistently changes the first line based on the required ending of the second line."
            elif percent_different > 50:
                analysis["planning_evidence"] = "Moderate evidence of planning: Claude often changes the first line based on the required ending of the second line."
            elif percent_different > 25:
                analysis["planning_evidence"] = "Weak evidence of planning: Claude sometimes changes the first line based on the required ending of the second line."
            else:
                analysis["planning_evidence"] = "Little evidence of planning: Claude rarely changes the first line based on the required ending of the second line."
    
    return analysis

def main():
    """Main function to run the experiment and save results"""
    
    print("Starting poetry planning experiment...")
    
    # You can change the model here if needed
    model_name = "claude-3-7-sonnet-20250219"
    
    results = run_all_experiments(model_name)
    analysis = analyze_results(results)
    
    # Combine results and analysis
    output = {
        "model": model_name,
        "results": results,
        "analysis": analysis
    }
    
    # Convert to DataFrame and save to CSV
    if "constrained_rhymes" in results:
        df = pd.DataFrame(results["constrained_rhymes"]["results"])
        df.to_csv("poetry_planning_results.csv", index=False)
        print("Results saved to poetry_planning_results.csv")
    
    print("Analysis summary:")
    if "planning_evidence" in analysis:
        print(analysis["planning_evidence"])
    
    if "percent_first_lines_different" in analysis:
        print(f"Percentage of first lines that differ when second line is constrained: {analysis['percent_first_lines_different']:.1f}%")
    
    return output

if __name__ == "__main__":
    main()