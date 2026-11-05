# ADR 0001: Hybrid Ontology (LinkML) + Property Graph (Neo4j) for Context Graph

## Status

Accepted

## Context

CMS reimbursement policies require both formal semantic grounding to coding systems (ICD-10-CM, CPT, HCPCS, SNOMED CT) and high-performance operational queries for claim-time context selection, versioning, and Decision Trace navigation.

## Decision

Use a hybrid model:

- **LinkML** as the formal schema / ontology layer (generates OWL, supports OntoGPT grounding, validation)
- **Neo4j property graph** as the operational Context Graph store (versioning on nodes/edges, fast Cypher subgraph retrieval, provenance properties)

Data is validated against the LinkML schema, then materialized into Neo4j.

## Consequences

- Positive: Formal grounding + operational performance; clear separation of concerns
- Negative: Dual representation requires a materialization step and synchronization discipline
- Mitigation: Automated pipelines and golden-claim regression tests on every change

## Alternatives Considered

- Pure RDF/OWL store: Strong inference but weaker operational performance and tooling for high-volume claim evaluation
- Pure property graph without formal schema: Faster to start but harder to enforce coding-system grounding and long-term consistency
