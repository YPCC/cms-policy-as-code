# Spec Kit — Agent Specifications

This directory contains specifications that agents use to research, design, and implement components of the Policy-as-Code engine.

## Agents

| Agent | Responsibility | Output |
|-------|----------------|--------|
| Research Agent | Evaluate document extraction, entity/relation extraction, and KG frameworks against enterprise CMS criteria | Tool recommendations + scored matrix |
| Ontology Agent | Define and evolve LinkML schema, coding-system mappings, and ontology layer | LinkML YAML + generated OWL |
| Graph Agent | Design property-graph schema, versioning, and provenance model | Cypher schema + load patterns |
| Rules Agent | Translate graph constraints into deterministic rules | JSON/DMN rule sets + test cases |
| Evaluation Agent | Implement claim evaluation and Decision Trace generation | Service + golden-claim suite |
| Governance Agent | Maintain ADRs, promotion workflow, and audit controls | ADR updates + review gates |

## How to Use

Each agent receives the problem statement, current ADRs, and relevant research outputs as context. Agents propose changes via pull requests that update specs, ADRs, or implementation.
