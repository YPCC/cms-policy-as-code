# CMS Policy-as-Code / Context Graph Engine

Enterprise-scale Neuro-Symbolic system for converting CMS NCD/LCD policies into executable, auditable coverage rules.

The system extracts structured knowledge from CMS policy documents, grounds it to official coding systems, stores it in a versioned Context Graph, and evaluates claims with a deterministic rules engine that produces full Decision Traces.

## Status

Early-stage public repository with specification, architecture, schemas, and pilot scaffolding. Live data ingestion starters are in place.

## Quick Start

```bash
# Clone and install
git clone https://github.com/YPCC/cms-policy-as-code.git
cd cms-policy-as-code
pip install -e .

# Optional: set Neo4j connection (see .env.example)
export NEO4J_URI=bolt://localhost:7687
export NEO4J_USER=neo4j
export NEO4J_PASSWORD=password

# Run the synthetic Vitamin D LCD pilot
python scripts/pilot_vitamin_d.py
```

## Repository Structure

```
docs/
  problem-statement.md          # What we are solving
  solution-approach.md          # Neuro-symbolic approach and principles
  data-sources.md               # CMS data sources and benchmarks
  architecture/                 # C4 Context, Container, and GCP Deployment diagrams
  adr/                          # Architecture Decision Records
  spec-kit/                     # Agent specifications for Spec-Kit driven development
schemas/
  linkml/cms_policy.yaml        # Formal ontology schema
  cypher/vitamin_d_lcd.cypher   # Sample graph load
scripts/
  pilot_vitamin_d.py            # End-to-end synthetic pilot
  fetch_sample_lcd_article.py   # Live LCD + Article via Coverage API
  fetch_lab_ncd_icd10.py        # Laboratory NCD ICD-10 code lists
src/cms_policy_as_code/
  graph/neo4j_client.py         # Neo4j connection helper
  evaluation/service.py         # Claim Evaluation Service stub
```

## Key Concepts

- **Neuro-Symbolic**: LLM-assisted extraction into a knowledge graph; deterministic rules at runtime.
- **Context Graph**: Versioned property graph (Neo4j) of policies, codes, limitations, and provenance.
- **Decision Trace**: Immutable record linking claim facts, graph version, rules, and outcome.
- **Grounding**: Free text always resolves to official coding systems (ICD-10-CM, CPT, HCPCS, SNOMED CT).

## Data Sources

See `docs/data-sources.md` for the full list. Primary sources are the CMS Coverage API and MCD downloads. The Laboratory NCD ICD-10 lists provide the best structured ground truth for golden claims.

## Architecture

- [System Context](docs/architecture/c4-context.md)
- [Container Diagram](docs/architecture/c4-container.md)
- [GCP Deployment](docs/architecture/c4-deployment.md)

## Next Steps

1. Run the Vitamin D pilot against a local Neo4j instance.
2. Pull live data with the Coverage API and Lab NCD scripts.
3. Expand the golden-claim suite from official CMS sources.
4. Harden the evaluation service and Decision Trace.

Contributions and issues that map to the Spec Kit agents are welcome.
