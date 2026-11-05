# Research Agent Specification

## Purpose

Evaluate and recommend tooling for knowledge graph generation, entity extraction, and relationship extraction suitable for enterprise-scale CMS NCD/LCD processing.

## Inputs

- Problem statement
- Decision frameworks (structure preservation, grounding, versioning, scale, enterprise readiness, coding linkage)
- Current tool landscape (Docling, ContextGem, GLiNER, OntoGPT, LinkML, Neo4j, RDF stores, etc.)

## Process

1. Score candidate tools against the evaluation matrix dimensions
2. Recommend a composable pipeline (not a single tool)
3. Identify failure modes specific to policy documents (nested conditions, Article separation, versioning)
4. Propose mitigations

## Outputs

- Scored evaluation matrix
- Recommended extraction + grounding + graph stack
- ADR draft for tooling choices
- Open questions for human review

## Constraints

- Prefer tools with strong provenance and citation support
- Require grounding to official coding systems
- Runtime path must remain deterministic
