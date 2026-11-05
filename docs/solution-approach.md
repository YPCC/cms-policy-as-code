# Solution Approach

## High-Level Architecture

Neuro-Symbolic pipeline:

```
CMS Documents → Ingestion (Docling + docling-context)
            → Extraction (ContextGem + GLiNER + OntoGPT grounding)
            → LinkML Schema / Ontology Layer
            → Neo4j Context Graph (versioned, provenanced)
            → Deterministic Rules Engine
            → Claim Evaluation Service → Decision Trace
```

## Key Principles

- **Provenance first**: Every triple and every decision points back to source spans and graph version
- **Grounding mandatory**: Free text is never executable; entities resolve to official coding systems
- **Deterministic runtime**: LLM only in extraction path; rules engine only at inference
- **Versioning native**: Effective dates, supersession, jurisdiction are first-class
- **Human review gates**: Low-confidence or high-impact items require clinical/coding SME approval
- **Golden-claim regression**: Every policy or rule change is tested against known covered/denied claims

## Spec-Kit Driven Development

We use a Spec Kit approach so agents can collaboratively refine and implement:

- Research Agent → evaluates extraction and KG tools against the decision framework
- Ontology Agent → maintains LinkML schema and coding-system mappings
- Rules Agent → compiles graph constraints into deterministic rules
- Evaluation Agent → runs claims and produces Decision Traces
- Governance Agent → manages ADRs and promotion workflow

See `docs/spec-kit/` for agent specifications.

## Architecture Decision Records

ADRs capture choices that drive the C4 diagrams and implementation. See `docs/adr/`.

## Target Deployment

GCP-based (see `docs/architecture/c4-deployment.md`):

- Cloud Run / GKE for services
- Neo4j Aura or self-managed on GCE
- Cloud Storage for immutable document packages
- BigQuery / Cloud Logging for audit trails
