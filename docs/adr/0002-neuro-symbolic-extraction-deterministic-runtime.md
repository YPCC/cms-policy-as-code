# ADR 0002: Neuro-Symbolic Architecture — LLM-Assisted Extraction, Deterministic Runtime

## Status

Accepted

## Context

Policy documents are unstructured. Full LLM evaluation at claim time is unacceptable due to hallucination, non-determinism, and audit risk. Pure rules without structured knowledge are brittle.

## Decision

- Extraction and graph construction may use LLMs, GLiNER, OntoGPT, and similar tools, always with grounding, confidence scores, and human review gates
- Runtime claim evaluation uses only a deterministic rules engine operating on the versioned Context Graph
- Every decision produces an immutable Decision Trace linking claim facts, graph version, rules version, and outcome

## Consequences

- Positive: Auditability, reproducibility, regulatory defensibility
- Negative: Extraction quality becomes the critical path; requires continuous monitoring and golden tests
- Mitigation: Shadow mode, regression suites, and SME promotion workflow
