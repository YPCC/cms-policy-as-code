# Vitamin D LCD Example (L36692)

This is the canonical pilot example used throughout the repository.

## Policy Summary

- **LCD**: L36692 – Vitamin D Assay Testing
- **Jurisdiction**: Noridian (example)
- **Effective**: 2017-02-03
- **Procedures**: CPT 82306 (25-OH Vitamin D), CPT 82652 (1,25-OH Vitamin D)
- **Covered diagnoses (simplified)**: N18.3 (CKD stage 3), E21.0 (Primary hyperparathyroidism), M81.0 (Age-related osteoporosis)
- **Limitation**: Not covered for routine screening

## Sample Claims

| Claim ID   | CPT   | Diagnoses     | Expected Decision | Reason                          |
|------------|-------|---------------|-------------------|---------------------------------|
| CLAIM-001  | 82306 | N18.3         | covered           | Matches covered indication      |
| CLAIM-002  | 82306 | Z00.00        | denied            | Screening exclusion             |
| CLAIM-003  | 82306 | E21.0, N18.3  | covered           | Multiple covered diagnoses      |

## How to Reproduce

1. Start Neo4j.
2. Run `python scripts/pilot_vitamin_d.py`.
3. Inspect the Decision Traces printed to the console.

The corresponding Cypher load script is at `schemas/cypher/vitamin_d_lcd.cypher`.
