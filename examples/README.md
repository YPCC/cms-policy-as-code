# Examples

## Vitamin D LCD Pilot (Synthetic)

The primary end-to-end example is `scripts/pilot_vitamin_d.py`.

It:
1. Loads a simplified version of LCD L36692 (Vitamin D Assay Testing) into Neo4j.
2. Evaluates three sample claims:
   - Covered diagnosis (N18.3 – CKD stage 3)
   - Screening diagnosis (Z00.00) → expected denial
   - Multiple covered diagnoses
3. Prints Decision Traces.

### Prerequisites

- Neo4j running locally (or set `NEO4J_URI`, `NEO4J_USER`, `NEO4J_PASSWORD`)
- Package installed: `pip install -e .`

### Run

```bash
python scripts/pilot_vitamin_d.py
```

## Live Data Starters

- `scripts/fetch_sample_lcd_article.py` — Pulls a real LCD and related Article via the CMS Coverage API (requires license token, obtained automatically).
- `scripts/fetch_lab_ncd_icd10.py` — Downloads the Laboratory NCD ICD-10 code lists (best structured ground truth).

These scripts write raw data that can later be mapped into the LinkML schema and Neo4j load patterns.
