# Problem Statement

## The Challenge

Large healthcare payers must interpret and apply thousands of CMS National Coverage Determinations (NCDs), Local Coverage Determinations (LCDs), and associated Billing and Coding Articles to decide whether claims and prior-authorization requests meet medical necessity and coverage rules.

These policies are published as unstructured or semi-structured documents (PDFs, HTML) containing:

- Nested clinical indications and limitations
- Frequency and documentation constraints
- Code lists (often in companion Articles)
- Jurisdiction-specific (MAC) variations
- Effective-date versioning and supersession

### Current State Pain

- Manual interpretation is slow, inconsistent, and expensive
- Pure LLM approaches introduce hallucination and audit risk for financial/regulatory decisions
- Pure rules systems without a living knowledge graph are brittle and costly to maintain
- Results: delayed payments, high denial/appeal volumes, revenue leakage, provider abrasion, and compliance exposure

## What We Are Solving

An enterprise-scale **Policy-as-Code / Context Graph Engine** that:

1. Ingests and versions CMS policy documents with full provenance and citations
2. Extracts structured entities, relationships, and constraints into a governed knowledge graph / ontology (grounded to official coding systems: ICD-10-CM, CPT, HCPCS, SNOMED CT)
3. Selects the relevant policy context for any given claim or prior-authorization request
4. Executes **deterministic** rules (no LLM at inference time) to produce a coverage decision plus a full Decision Trace
5. Supports continuous updates, multi-jurisdiction logic, and operational scale

The system is Neuro-Symbolic by design: neural/LLM-assisted extraction and graph construction; deterministic rules engine for runtime evaluation.
