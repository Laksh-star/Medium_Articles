"""
Example script to run the Movie Set Optimization System
"""

from movie_set_optimization import optimize_movie_set

# Run the optimization process
results = optimize_movie_set("gladiator_colosseum_config.json")

# Access specific results if needed
print(f"Construction plan estimated cost: ${results['construction_plan']['estimated_cost']:,.2f}")
print(f"Number of physical elements to build: {len(results['construction_plan']['physical_elements'])}")
print(f"Number of CGI elements: {len(results['construction_plan']['cgi_elements'])}")
print(f"Full report available at: {results['report_path']}")

# The report will be available at: output/reports/set_optimization_report.html
