"""
Movie Set Optimization System

This script analyzes script scenes, shot lists, and reference images to determine
the minimal physical set construction needed for a film production, with visualizations
of both physical sets and final composites with CGI elements.

Example use case: Planning the Colosseum set for a film like Gladiator.
"""

import os
import json
import base64
from io import BytesIO
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI
import matplotlib.pyplot as plt

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Create output directories
os.makedirs("output/reconstructions", exist_ok=True)
os.makedirs("output/physical_sets", exist_ok=True)
os.makedirs("output/composites", exist_ok=True)
os.makedirs("output/comparisons", exist_ok=True)
os.makedirs("output/reports", exist_ok=True)

def load_input_data(config_path):
    """
    Load project configuration, script scenes, shot list and budget constraints
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print(f"Loaded project: {config['project_name']}")
    print(f"Found {len(config['script_scenes'])} scenes to analyze")
    
    return config

def load_reference_images(image_paths):
    """
    Load reference images for archaeological reconstruction
    """
    images = []
    for path in image_paths:
        try:
            img = Image.open(path)
            images.append(img)
            print(f"Loaded reference image: {path}")
        except Exception as e:
            print(f"Error loading image {path}: {e}")
    
    return images

def create_complete_model(reference_images, set_name, historical_period):
    """
    Create a comprehensive digital reconstruction of the historical setting
    """
    print(f"Creating complete digital reconstruction of {set_name}...")
    
    # Combine reference images into a collage for context
    collage = create_reference_collage(reference_images)
    collage_path = "output/reference_collage.jpg"
    collage.save(collage_path)
    
    # Get historical context using GPT
    historical_context = get_historical_context(set_name, historical_period)
    
    # Generate full reconstruction visualization
    with open(collage_path, "rb") as img_file:
        full_reconstruction = client.images.edit(
            model="gpt-image-1",
            image=img_file,
            prompt=f"Create a comprehensive archaeological reconstruction of a {historical_period} {set_name} based on these reference images. {historical_context} Show multiple angles including aerial view, interior, and exterior perspectives. Include accurate architectural details, textures, and lighting. This should be a complete academic-quality reconstruction.",
            quality="high",
            size="1024x1024"
        )
    
    # Save the reconstruction image
    image_base64 = full_reconstruction.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)
    image = Image.open(BytesIO(image_bytes))
    
    output_path = f"output/reconstructions/full_{set_name.lower().replace(' ', '_')}.jpg"
    image.save(output_path, format="JPEG", quality=95)
    print(f"Full reconstruction saved to {output_path}")
    
    return {
        "image": image,
        "path": output_path,
        "historical_context": historical_context
    }

def create_reference_collage(images):
    """
    Create a collage from reference images
    """
    # Calculate collage dimensions
    max_width = 1024
    max_height = 1024
    n_images = len(images)
    
    if n_images <= 2:
        cols, rows = n_images, 1
    else:
        cols = int(np.ceil(np.sqrt(n_images)))
        rows = int(np.ceil(n_images / cols))
    
    # Resize images to fit collage
    thumb_width = max_width // cols
    thumb_height = max_height // rows
    
    # Create blank collage
    collage = Image.new('RGB', (max_width, max_height), (255, 255, 255))
    
    # Paste images into collage
    for i, img in enumerate(images):
        if i >= cols * rows:
            break
            
        row = i // cols
        col = i % cols
        
        # Resize image
        img_aspect = img.width / img.height
        thumb_aspect = thumb_width / thumb_height
        
        if img_aspect > thumb_aspect:
            # Image is wider than thumbnail
            new_width = thumb_width
            new_height = int(thumb_width / img_aspect)
        else:
            # Image is taller than thumbnail
            new_height = thumb_height
            new_width = int(thumb_height * img_aspect)
            
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)
        
        # Calculate position
        x = col * thumb_width + (thumb_width - new_width) // 2
        y = row * thumb_height + (thumb_height - new_height) // 2
        
        collage.paste(img_resized, (x, y))
    
    return collage

def get_historical_context(set_name, historical_period):
    """
    Get historical architectural information for accurate reconstruction
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert archaeologist and architectural historian."},
            {"role": "user", "content": f"Provide detailed architectural information about {set_name} from {historical_period}. Include information about construction materials, dimensions, distinctive features, and any regional variations. Format your response as a concise paragraph focusing on visual elements that would be important for accurate reconstruction."}
        ]
    )
    
    return response.choices[0].message.content

def analyze_script_scene(scene, set_name):
    """
    Analyze a script scene to determine required set elements
    """
    print(f"Analyzing scene {scene['id']}: {scene['title']}")
    
    # Use LLM to analyze scene requirements
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert film production designer and VFX supervisor."},
            {"role": "user", "content": f"""
            For this {set_name} scene: "{scene['description']}", please provide:
            
            1. PHYSICAL ELEMENTS: List all physical set elements actors directly interact with
            2. FOREGROUND ELEMENTS: List elements needed in the foreground (within 10 feet of camera)
            3. MIDGROUND ELEMENTS: List elements needed in the midground (10-50 feet from camera)
            4. BACKGROUND ELEMENTS: List elements needed in the background (beyond 50 feet)
            5. CAMERA ANGLES: List all camera angles and movements described or implied
            
            Format your response as a JSON object with these categories as keys, and arrays of strings as values.
            For each element, note whether it should be PHYSICAL or CGI in brackets after the element name.
            """}
        ],
        response_format={"type": "json_object"}
    )
    
    # Parse the JSON response
    try:
        scene_analysis = json.loads(response.choices[0].message.content)
        return scene_analysis
    except json.JSONDecodeError as e:
        print(f"Error parsing scene analysis: {e}")
        print(f"Raw response: {response.choices[0].message.content}")
        return {
            "PHYSICAL_ELEMENTS": [],
            "FOREGROUND_ELEMENTS": [],
            "MIDGROUND_ELEMENTS": [],
            "BACKGROUND_ELEMENTS": [],
            "CAMERA_ANGLES": []
        }

def determine_physical_construction(scene_analyses, budget_constraints, set_name):
    """
    Determine which elements need physical construction vs. CGI across all scenes
    """
    print("Determining physical construction requirements...")
    
    # Aggregate all elements across scenes
    all_elements = {
        "physical_interactions": set(),
        "foreground": set(),
        "midground": set(),
        "background": set()
    }
    
    for scene_id, analysis in scene_analyses.items():
        for elem in analysis.get("PHYSICAL_ELEMENTS", []):
            all_elements["physical_interactions"].add(elem)
            
        for elem in analysis.get("FOREGROUND_ELEMENTS", []):
            all_elements["foreground"].add(elem)
            
        for elem in analysis.get("MIDGROUND_ELEMENTS", []):
            all_elements["midground"].add(elem)
            
        for elem in analysis.get("BACKGROUND_ELEMENTS", []):
            all_elements["background"].add(elem)
    
    # Use LLM to determine optimal physical/CGI balance
    elements_list = "\n".join([
        f"Physical interactions: {', '.join(all_elements['physical_interactions'])}",
        f"Foreground elements: {', '.join(all_elements['foreground'])}",
        f"Midground elements: {', '.join(all_elements['midground'])}",
        f"Background elements: {', '.join(all_elements['background'])}"
    ])
    
    budget_info = f"Budget constraints: ${budget_constraints['total_budget']:,} total, with max ${budget_constraints['max_physical_budget']:,} for physical construction"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert film production designer, set builder, and VFX supervisor with experience optimizing film budgets."},
            {"role": "user", "content": f"""
            Based on these required elements for all scenes in a {set_name} set:
            
            {elements_list}
            
            And these budget constraints:
            {budget_info}
            
            Determine the optimal balance of physical construction versus CGI elements. 
            
            1. Create a comprehensive list of what should be physically built
            2. Create a list of what should be created with CGI
            3. Provide a rough cost estimate for the physical construction
            4. Explain your reasoning for these decisions
            
            Format your response as a JSON object with these keys: "physical_elements" (array), "cgi_elements" (array), "estimated_cost" (number), "reasoning" (string).
            """}
        ],
        response_format={"type": "json_object"}
    )
    
    try:
        construction_plan = json.loads(response.choices[0].message.content)
        return construction_plan
    except json.JSONDecodeError as e:
        print(f"Error parsing construction plan: {e}")
        return {
            "physical_elements": list(all_elements["physical_interactions"]),
            "cgi_elements": list(all_elements["background"]),
            "estimated_cost": budget_constraints["max_physical_budget"] / 2,
            "reasoning": "Error in analysis. Default to building physical interaction elements only."
        }

def generate_set_visualizations(scene, construction_plan, set_name):
    """
    Generate visualizations of physical set and final composite for a scene
    """
    scene_id = scene["id"]
    scene_title = scene["title"]
    scene_desc = scene["description"]
    
    print(f"Generating visualizations for scene {scene_id}: {scene_title}")
    
    # Join the construction elements into comma-separated strings
    physical_elements = ", ".join(construction_plan["physical_elements"])
    cgi_elements = ", ".join(construction_plan["cgi_elements"])
    
    # Generate physical set visualization
    physical_prompt = f"""
    Technical visualization of the minimal physical set construction required for filming this {set_name} scene: "{scene_desc}".
    
    Show only these physical elements: {physical_elements}.
    
    Use realistic construction materials like plywood, scaffolding, and partial stonework.
    Include measurement markers, green screens where CGI will be added, and construction annotations.
    Use a slightly elevated angle to show the full set layout. Show crew and equipment positions.
    This should look like a detailed production design concept for set builders.
    """
    
    physical_result = client.images.generate(
        model="gpt-image-1",
        prompt=physical_prompt,
        quality="high",
        size="1024x1024"
    )
    
    # Generate final composite visualization
    composite_prompt = f"""
    Cinematic visualization of the final composited shot for this {set_name} scene: "{scene_desc}".
    
    Show the physical set elements ({physical_elements}) seamlessly blended with CGI elements ({cgi_elements}).
    
    This should look like a finished film frame with professional cinematography, lighting, and atmosphere.
    Use film production quality with appropriate depth of field, color grading, and atmospheric effects.
    """
    
    composite_result = client.images.generate(
        model="gpt-image-1",
        prompt=composite_prompt,
        quality="high",
        size="1024x1024"
    )
    
    # Save images
    physical_image = Image.open(BytesIO(base64.b64decode(physical_result.data[0].b64_json)))
    composite_image = Image.open(BytesIO(base64.b64decode(composite_result.data[0].b64_json)))
    
    physical_path = f"output/physical_sets/scene_{scene_id}_physical.jpg"
    composite_path = f"output/composites/scene_{scene_id}_composite.jpg"
    
    physical_image.save(physical_path, format="JPEG", quality=95)
    composite_image.save(composite_path, format="JPEG", quality=95)
    
    # Create side-by-side comparison
    comparison = create_comparison_image(physical_image, composite_image, scene_title)
    comparison_path = f"output/comparisons/scene_{scene_id}_comparison.jpg"
    comparison.save(comparison_path, format="JPEG", quality=95)
    
    return {
        "physical": {
            "image": physical_image,
            "path": physical_path
        },
        "composite": {
            "image": composite_image,
            "path": composite_path
        },
        "comparison": {
            "image": comparison,
            "path": comparison_path
        }
    }

def create_comparison_image(physical_image, composite_image, title):
    """
    Create a side-by-side comparison of physical set and final composite
    """
    # Create a new image with both side by side
    width = physical_image.width * 2 + 20  # 20px spacing
    height = physical_image.height + 60  # Space for title
    comparison = Image.new('RGB', (width, height), (255, 255, 255))
    
    # Add title
    draw = ImageDraw.Draw(comparison)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        # Fallback to default font if arial is not available
        font = ImageFont.load_default()
        
    draw.text((10, 10), f"Scene: {title}", fill=(0, 0, 0), font=font)
    draw.text((10, 40), "Physical Construction", fill=(0, 0, 0), font=font)
    draw.text((physical_image.width + 30, 40), "Final Composite with CGI", fill=(0, 0, 0), font=font)
    
    # Paste the images
    comparison.paste(physical_image, (0, 60))
    comparison.paste(composite_image, (physical_image.width + 20, 60))
    
    return comparison

def generate_budget_chart(construction_plan, budget_constraints):
    """
    Generate a budget visualization chart
    """
    # Create budget data
    estimated_cost = construction_plan["estimated_cost"]
    max_budget = budget_constraints["max_physical_budget"]
    remaining = max_budget - estimated_cost
    
    # Create pie chart
    labels = ['Physical Construction', 'Remaining Budget']
    sizes = [estimated_cost, remaining]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # explode the 1st slice
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', startangle=90, shadow=True)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    plt.title(f'Physical Construction Budget: ${estimated_cost:,.2f} of ${max_budget:,.2f}')
    
    budget_chart_path = "output/reports/budget_chart.jpg"
    plt.savefig(budget_chart_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    return budget_chart_path

def generate_final_report(project_config, reconstruction, construction_plan, scene_visualizations):
    """
    Generate a comprehensive final report with all analyses and visualizations
    """
    print("Generating final report...")
    
    # Create HTML report structure
    report_content = f"""
    <html>
    <head>
        <title>Set Optimization Report: {project_config['project_name']}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1, h2, h3 {{ color: #333366; }}
            .section {{ margin-bottom: 30px; }}
            .image-container {{ margin: 20px 0; }}
            img {{ max-width: 100%; border: 1px solid #ddd; }}
            .scene {{ margin-bottom: 40px; border-bottom: 1px solid #ccc; padding-bottom: 20px; }}
            .construction-list {{ column-count: 2; }}
            .budget {{ display: flex; align-items: center; }}
            .reasoning {{ background-color: #f9f9f9; padding: 15px; border-left: 4px solid #333366; }}
        </style>
    </head>
    <body>
        <h1>Set Optimization Report: {project_config['project_name']}</h1>
        <div class="section">
            <h2>Project Overview</h2>
            <p><strong>Set:</strong> {project_config['set_name']}</p>
            <p><strong>Historical Period:</strong> {project_config['historical_period']}</p>
            <p><strong>Budget Constraints:</strong> Total ${project_config['budget_constraints']['total_budget']:,}, 
               Max Physical ${project_config['budget_constraints']['max_physical_budget']:,}</p>
            <p><strong>Number of Scenes:</strong> {len(project_config['script_scenes'])}</p>
        </div>
        
        <div class="section">
            <h2>Full Archaeological Reconstruction</h2>
            <p>{reconstruction['historical_context']}</p>
            <div class="image-container">
                <img src="{os.path.basename(reconstruction['path'])}" alt="Full Reconstruction">
            </div>
        </div>
        
        <div class="section">
            <h2>Construction Plan</h2>
            <div class="budget">
                <div>
                    <h3>Budget Allocation</h3>
                    <p><strong>Estimated Physical Construction Cost:</strong> ${construction_plan['estimated_cost']:,.2f}</p>
                    <p><strong>Percentage of Max Budget:</strong> 
                       {(construction_plan['estimated_cost'] / project_config['budget_constraints']['max_physical_budget']) * 100:.1f}%</p>
                </div>
                <div>
                    <img src="budget_chart.jpg" alt="Budget Chart" style="max-width: 400px;">
                </div>
            </div>
            
            <h3>Physical Elements to Build</h3>
            <div class="construction-list">
                <ul>
    """
    
    # Add physical elements
    for element in construction_plan['physical_elements']:
        report_content += f"<li>{element}</li>\n"
    
    report_content += """
                </ul>
            </div>
            
            <h3>CGI Elements</h3>
            <div class="construction-list">
                <ul>
    """
    
    # Add CGI elements
    for element in construction_plan['cgi_elements']:
        report_content += f"<li>{element}</li>\n"
    
    report_content += f"""
                </ul>
            </div>
            
            <h3>Reasoning</h3>
            <div class="reasoning">
                <p>{construction_plan['reasoning']}</p>
            </div>
        </div>
        
        <div class="section">
            <h2>Scene Visualizations</h2>
    """
    
    # Add each scene
    for scene in project_config['script_scenes']:
        scene_id = scene['id']
        if scene_id in scene_visualizations:
            viz = scene_visualizations[scene_id]
            report_content += f"""
            <div class="scene">
                <h3>Scene {scene_id}: {scene['title']}</h3>
                <p><strong>Description:</strong> {scene['description']}</p>
                
                <h4>Physical Set vs. Final Composite Comparison</h4>
                <div class="image-container">
                    <img src="{os.path.basename(viz['comparison']['path'])}" alt="Comparison for Scene {scene_id}">
                </div>
                
                <h4>Detailed Views</h4>
                <p><strong>Physical Construction Only:</strong></p>
                <div class="image-container">
                    <img src="{os.path.basename(viz['physical']['path'])}" alt="Physical Set for Scene {scene_id}">
                </div>
                
                <p><strong>Final Composite with CGI:</strong></p>
                <div class="image-container">
                    <img src="{os.path.basename(viz['composite']['path'])}" alt="Composite for Scene {scene_id}">
                </div>
            </div>
            """
    
    # Close HTML
    report_content += """
        </div>
    </body>
    </html>
    """
    
    # Save the report
    report_path = "output/reports/set_optimization_report.html"
    with open(report_path, "w") as f:
        f.write(report_content)
    
    print(f"Final report saved to {report_path}")
    return report_path

def optimize_movie_set(config_path):
    """
    Main function to run the entire set optimization process
    """
    # Load input data
    project_config = load_input_data(config_path)
    
    # Load reference images
    reference_images = load_reference_images(project_config['reference_image_paths'])
    
    # Create complete archaeological reconstruction
    reconstruction = create_complete_model(
        reference_images, 
        project_config['set_name'], 
        project_config['historical_period']
    )
    
    # Analyze each scene in the script
    scene_analyses = {}
    for scene in project_config['script_scenes']:
        scene_analyses[scene['id']] = analyze_script_scene(scene, project_config['set_name'])
    
    # Determine physical construction needs
    construction_plan = determine_physical_construction(
        scene_analyses, 
        project_config['budget_constraints'],
        project_config['set_name']
    )
    
    # Generate visualizations for each scene
    scene_visualizations = {}
    for scene in project_config['script_scenes']:
        scene_visualizations[scene['id']] = generate_set_visualizations(
            scene,
            construction_plan,
            project_config['set_name']
        )
    
    # Generate budget chart
    budget_chart_path = generate_budget_chart(construction_plan, project_config['budget_constraints'])
    
    # Generate final report
    report_path = generate_final_report(
        project_config, 
        reconstruction,
        construction_plan,
        scene_visualizations
    )
    
    print("\n========================================================")
    print(f"Set optimization complete for {project_config['project_name']}")
    print(f"Final report available at: {report_path}")
    print("========================================================\n")
    
    return {
        "project_config": project_config,
        "reconstruction": reconstruction,
        "scene_analyses": scene_analyses,
        "construction_plan": construction_plan,
        "scene_visualizations": scene_visualizations,
        "report_path": report_path
    }

if __name__ == "__main__":
    # Example usage
    optimize_movie_set("gladiator_colosseum_config.json")
