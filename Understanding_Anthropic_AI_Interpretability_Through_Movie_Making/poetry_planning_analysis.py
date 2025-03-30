import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Dict, List, Any
import re

def load_results(filename: str = "poetry_planning_results.csv") -> pd.DataFrame:
    """Load results from CSV file"""
    return pd.DataFrame(pd.read_csv(filename))

def calculate_similarity(str1: str, str2: str) -> float:
    """
    Calculate a simple similarity score between two strings
    based on the number of shared words
    """
    # Convert to lowercase and remove punctuation
    str1 = re.sub(r'[^\w\s]', '', str1.lower())
    str2 = re.sub(r'[^\w\s]', '', str2.lower())
    
    # Split into words
    words1 = set(str1.split())
    words2 = set(str2.split())
    
    # Calculate Jaccard similarity
    if not words1 or not words2:
        return 0.0
    
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    
    return len(intersection) / len(union)

def visualize_first_line_differences(df: pd.DataFrame) -> plt.Figure:
    """
    Visualize how first lines differ based on the constraint for the second line
    """
    # Group by theme
    themes = df['theme'].unique()
    
    # Calculate similarities between base and constrained first lines
    similarities = []
    
    for theme in themes:
        theme_df = df[df['theme'] == theme]
        
        # Get the base (unconstrained) first line
        base_row = theme_df[theme_df['constraint'] == 'none']
        if base_row.empty:
            continue
            
        base_first_line = base_row.iloc[0]['first_line']
        
        # Compare with constrained versions
        for _, row in theme_df[theme_df['constraint'] != 'none'].iterrows():
            similarity = calculate_similarity(base_first_line, row['first_line'])
            
            similarities.append({
                'theme': theme,
                'constraint': row['constraint'],
                'similarity': similarity,
                'base_first_line': base_first_line,
                'constrained_first_line': row['first_line']
            })
    
    # Convert to DataFrame
    sim_df = pd.DataFrame(similarities)
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    
    # Plot similarity by theme and constraint
    sns.barplot(x='theme', y='similarity', hue='constraint', data=sim_df)
    plt.title('Similarity Between Base and Constrained First Lines')
    plt.xlabel('Theme')
    plt.ylabel('Similarity (Jaccard)')
    plt.ylim(0, 1)
    plt.legend(title='Required Ending')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return plt.gcf()

def analyze_mid_generation_steering(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyze the results of mid-generation steering experiment
    """
    # Check if we have the right columns
    if 'completion_type' not in df.columns:
        return {"error": "No mid-generation steering data found"}
    
    # Group by theme and completion_type
    result = {}
    themes = df['theme'].unique()
    
    for theme in themes:
        theme_df = df[df['theme'] == theme]
        result[theme] = {}
        
        # Get second lines for each completion type
        for completion_type in ['natural', 'unexpected', 'opposite']:
            type_rows = theme_df[theme_df['completion_type'] == completion_type]
            if not type_rows.empty:
                result[theme][completion_type] = type_rows.iloc[0]['second_line']
    
    return result

def visualize_word_choices(df: pd.DataFrame) -> plt.Figure:
    """
    Visualize the words used in first lines under different constraints
    """
    # Extract words from first lines
    word_counts = {}
    
    for theme in df['theme'].unique():
        theme_df = df[df['theme'] == theme]
        
        # Skip if no base line
        base_rows = theme_df[theme_df['constraint'] == 'none']
        if base_rows.empty:
            continue
            
        # Get words from base first line
        base_first_line = base_rows.iloc[0]['first_line'].lower()
        base_words = re.findall(r'\b\w+\b', base_first_line)
        
        # Get words from constrained first lines
        for constraint in theme_df[theme_df['constraint'] != 'none']['constraint'].unique():
            constraint_rows = theme_df[theme_df['constraint'] == constraint]
            if constraint_rows.empty:
                continue
                
            constrained_first_line = constraint_rows.iloc[0]['first_line'].lower()
            constrained_words = re.findall(r'\b\w+\b', constrained_first_line)
            
            # Find words in constrained that aren't in base
            unique_words = [word for word in constrained_words if word not in base_words]
            
            # Store in dictionary
            key = f"{theme}_{constraint}"
            word_counts[key] = len(unique_words)
    
    # Convert to DataFrame
    word_df = pd.DataFrame([
        {"theme_constraint": k, "unique_words": v} 
        for k, v in word_counts.items()
    ])
    
    # Extract theme and constraint
    word_df[['theme', 'constraint']] = word_df['theme_constraint'].str.split('_', n=1, expand=True)
    
    # Create visualization
    plt.figure(figsize=(12, 6))
    sns.barplot(x='theme', y='unique_words', hue='constraint', data=word_df)
    plt.title('Number of Unique Words in Constrained First Lines (Not in Base)')
    plt.xlabel('Theme')
    plt.ylabel('Unique Word Count')
    plt.legend(title='Required Ending')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return plt.gcf()

def create_full_report(data_file: str = "poetry_planning_results.csv") -> None:
    """Create a full report with all analyses"""
    
    try:
        df = load_results(data_file)
        print(f"Loaded data with {len(df)} rows")
        
        # Summary statistics
        themes = df['theme'].unique()
        constraints = df[df['constraint'] != 'none']['constraint'].unique()
        
        print(f"Found {len(themes)} themes and {len(constraints)} constraints")
        
        # Check if df has constrained_rhymes data
        if 'constraint' in df.columns:
            # Calculate percentage of first lines that differ
            different_count = 0
            total_count = 0
            
            for theme in themes:
                theme_df = df[df['theme'] == theme]
                
                # Get the base first line
                base_rows = theme_df[theme_df['constraint'] == 'none']
                if base_rows.empty:
                    continue
                    
                base_first_line = base_rows.iloc[0]['first_line']
                
                # Compare with constrained first lines
                for _, row in theme_df[theme_df['constraint'] != 'none'].iterrows():
                    total_count += 1
                    if row['first_line'] != base_first_line:
                        different_count += 1
            
            if total_count > 0:
                percent_different = (different_count / total_count) * 100
                print(f"Percentage of first lines that differ: {percent_different:.1f}%")
                
                # Interpretation
                if percent_different > 75:
                    print("Strong evidence of planning: Claude consistently changes the first line based on the required ending of the second line.")
                elif percent_different > 50:
                    print("Moderate evidence of planning: Claude often changes the first line based on the required ending of the second line.")
                elif percent_different > 25:
                    print("Weak evidence of planning: Claude sometimes changes the first line based on the required ending of the second line.")
                else:
                    print("Little evidence of planning: Claude rarely changes the first line based on the required ending of the second line.")
            
            # Create visualizations
            fig1 = visualize_first_line_differences(df)
            fig1.savefig("first_line_similarities.png")
            print("Saved first line similarities visualization to first_line_similarities.png")
            
            fig2 = visualize_word_choices(df)
            fig2.savefig("unique_words.png")
            print("Saved unique words visualization to unique_words.png")
            
        # Check if df has mid_generation_steering data
        if 'completion_type' in df.columns:
            steering_results = analyze_mid_generation_steering(df)
            
            print("\nMid-generation steering results:")
            for theme, completions in steering_results.items():
                print(f"\nTheme: {theme}")
                for completion_type, second_line in completions.items():
                    print(f"  {completion_type}: {second_line}")
        
        print("\nFull report complete!")
        
    except Exception as e:
        print(f"Error creating report: {e}")

if __name__ == "__main__":
    create_full_report()