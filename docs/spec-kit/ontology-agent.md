# Ontology Agent Specification

## Purpose

Define and evolve the LinkML schema, coding-system mappings, and formal ontology layer.

## Inputs

- Problem statement and ADRs
- Current `schemas/linkml/cms_policy.yaml`
- Research Agent outputs on grounding tools

## Expected Outputs

- Updated LinkML schema with new classes/slots as needed
- Mappings to ICD-10-CM, CPT, HCPCS, SNOMED CT
- Generated OWL or validation report
- ADR draft if schema changes affect architecture

## Constraints

- Free-text medical terms must resolve to standard codes or be flagged for review
- Schema must support versioning and effective dates
