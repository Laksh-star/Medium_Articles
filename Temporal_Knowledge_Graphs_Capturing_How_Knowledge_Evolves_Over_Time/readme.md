# Medical Temporal Knowledge Graph

A hands-on implementation of temporal knowledge graphs for medical research, adapted from OpenAI's temporal agents cookbook. This project demonstrates how to extract time-aware medical facts from research papers and build queryable knowledge graphs.

## 🎯 Overview

This implementation transforms medical research papers into temporal knowledge graphs that can answer questions like:
- "What treatments for Alzheimer's disease were considered effective in 2023?"
- "How has CRISPR therapy effectiveness evolved over time?"
- "What did we know about vaccine effectiveness against Omicron in January 2022?"

## 🏥 Key Features

- **Medical Entity Recognition**: Drugs, diseases, organizations, researchers, outcomes
- **Temporal Classification**: Static events vs dynamic states vs atemporal facts
- **Confidence Scoring**: HIGH/MEDIUM/LOW evidence levels based on study types
- **Interactive Queries**: Search by entity type, relationship, and time period
- **Visual Knowledge Graph**: Color-coded medical entities with relationship mapping

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- OpenAI API key
- Google Colab (recommended) or local Jupyter environment

### Installation

1. **Open in Google Colab** (easiest option):
   ```
   Click "Open in Colab" button above or visit: [Colab Link]
   ```


### Setup

1. Set your OpenAI API key:
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key-here"
   ```

2. Run the main notebook:
   ```python
   # In Colab or Jupyter
   %run temporal_agents_medical.py
   ```

## 📊 Sample Data

The implementation includes realistic medical research scenarios:

- **Clinical Trial**: Phase II Alzheimer's drug (AD-2023) showing cognitive improvements
- **Gene Therapy**: CRISPR treatments for sickle cell disease with 24-month follow-up
- **Meta-Analysis**: COVID vaccine effectiveness across variants and time periods

## 🔍 Example Queries

```python
# Find treatments for specific diseases
medical_factual_qa(G, 'Alzheimer', entity_type='disease')

# Track what organizations have developed
medical_factual_qa(G, 'Pfizer', entity_type='organization')

# See effectiveness demonstrations for treatments
medical_factual_qa(G, 'vaccine', 'DEMONSTRATES')
```

**Sample Output:**
```
🔬 Found 3 medical relationships for 'vaccine':

1. 🟢 mRNA Vaccine --[DEMONSTRATES]--> 95% Effectiveness (Value: vs original strain)
   📝 Statement: Pfizer-BioNTech vaccine maintained 78% effectiveness...
   📅 Date: 2021-12-01
   🎯 Confidence: HIGH
```

## 🏗️ Architecture

```
Research Papers → Text Chunking → Medical Fact Extraction → Knowledge Graph → Temporal Queries
```

### Core Components

1. **Medical Temporal Agent**: GPT-4 powered fact extraction with medical domain awareness
2. **Confidence Scoring**: Evidence-based reliability assessment (peer-reviewed > observational > case reports)
3. **Medical Graph Builder**: NetworkX graphs with medical entity type classification
4. **Temporal Query Engine**: Time-bounded searches with entity type filtering

## 📈 Medical Entity Types

- 🔴 **Treatments/Drugs**: Medications, therapies, interventions
- 🟢 **Diseases**: Medical conditions, syndromes, disorders  
- 🔵 **Organizations**: FDA, hospitals, pharmaceutical companies
- 🟡 **Researchers**: Clinical investigators, study authors
- 🟣 **Outcomes**: Effectiveness rates, safety profiles, patient responses

## 🔬 Compared to OpenAI Cookbook

| Feature | OpenAI Cookbook | Our Medical Demo | Status |
|---------|-----------------|------------------|---------|
| **Domain** | Financial earnings | Medical research | ✅ Adapted |
| **Entity Resolution** | ✅ Full implementation | ❌ Simplified | 🟡 Basic |
| **Temporal Classification** | ✅ Static/Dynamic/Atemporal | ✅ Static/Dynamic/Atemporal | ✅ Complete |
| **Confidence Scoring** | ❌ Not emphasized | ✅ Medical evidence levels | ✅ Enhanced |
| **Multi-Step Retrieval** | ✅ LLM orchestration | ❌ Simple Q&A | 🔴 Missing |
| **Visualization** | ✅ Basic graphs | ✅ Medical color-coding | ✅ Enhanced |

## 📝 Sample Medical Facts Extracted

```python
{
    "statement": "AD-2023 demonstrated significant cognitive improvement vs placebo",
    "subject": "AD-2023",
    "predicate": "DEMONSTRATES", 
    "object": "cognitive improvement",
    "value": "3.2 points MMSE improvement, p<0.001",
    "confidence": "HIGH",
    "temporal_type": "STATIC",
    "valid_at": "2024-01-15"
}
```

## 🎓 Educational Use

This implementation is designed for:
- **Medical AI researchers** exploring temporal reasoning
- **Healthcare data scientists** learning knowledge graph concepts
- **Students** studying temporal data modeling
- **Developers** adapting the OpenAI cookbook to new domains

## 🛠️ Extending the System

### Add New Medical Entities
```python
# Extend the medical ontology
entity_types = {
    'biomarker': '#FF9F43',     # Orange for biomarkers
    'procedure': '#6C5CE7',     # Purple for procedures  
    'device': '#A29BFE'         # Light purple for medical devices
}
```

### Customize Confidence Scoring
```python
def get_confidence_level(study_type, sample_size, peer_reviewed):
    if peer_reviewed and sample_size > 1000:
        return "HIGH"
    elif peer_reviewed or sample_size > 100:
        return "MEDIUM"
    else:
        return "LOW"
```

## 🚧 Limitations

- **Simplified Entity Resolution**: No fuzzy matching for medical terminology variants
- **No Fact Invalidation**: Missing temporal conflict detection from full cookbook
- **Basic Chunking**: Uses paragraph splitting instead of semantic chunking
- **Demo Scale**: Designed for learning, not production deployment

## 🔗 Related Resources

- [OpenAI Temporal Agents Cookbook](https://cookbook.openai.com/examples/partners/temporal_agents_with_knowledge_graphs/temporal_agents_with_knowledge_graphs) - Original financial implementation
- [Graphiti Framework](https://github.com/getzep/graphiti) - Production temporal knowledge graphs
- [Neo4j Temporal Queries](https://neo4j.com/docs/cypher-manual/current/syntax/temporal/) - Scaling to production databases

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Entity resolution for medical terminology
- Fact invalidation mechanisms  
- Multi-step retrieval implementation
- Additional medical domains (genomics, pharmacology, etc.)

## 📧 Contact

Questions or feedback? Open an issue or reach out!

---

*Built with ❤️ for the medical AI community. Inspired by OpenAI's temporal knowledge graph cookbook.*
