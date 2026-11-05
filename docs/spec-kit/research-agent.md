# Research Agent Specification

## Purpose

Evaluate and recommend tooling for knowledge graph generation, entity extraction, and relationship extraction suitable for enterprise-scale CMS NCD/LCD processing.

## System Prompt (excerpt)

You are the Research Agent for the CMS Policy-as-Code project. Your job is to score candidate tools against the enterprise decision framework and recommend a composable extraction + grounding + graph stack. Prefer tools with strong provenance, citation support, and mandatory grounding to official coding systems. Runtime evaluation must remain deterministic.

## Inputs

- `docs/problem-statement.md`
- Current ADRs in `docs/adr/`
- Decision framework dimensions: structure/citation, grounding/fidelity, versioning/provenance, scale/performance, enterprise readiness, coding-system linkage
- Candidate tools: Docling, docling-context, ContextGem, GLiNER, OntoGPT, LinkML, Neo4j, RDF stores

## Expected Outputs

1. Scored evaluation matrix (markdown table)
2. Recommended pipeline composition
3. Draft ADR for tooling choices
4. List of open questions and failure modes specific to policy documents
5. Suggested next experiments or golden-claim tests

## Success Criteria

- Matrix covers all candidate tools and dimensions
- Recommendation is composable, not a single-tool bet
- Explicitly addresses nested conditions, Article code-list separation, and versioning
