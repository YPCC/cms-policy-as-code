# Scripts

- `pilot_vitamin_d.py` — Loads the synthetic Vitamin D LCD example into Neo4j and runs sample claim evaluations.
- `fetch_sample_lcd_article.py` — Starter for pulling live LCD + related Article data from the CMS Coverage API.
- `fetch_lab_ncd_icd10.py` — Starter for the Laboratory NCD ICD-10 code lists (best structured ground truth for medical necessity).

## Requirements

```bash
pip install requests
```

For the Neo4j pilot, also install the package and set `NEO4J_*` environment variables (see `.env.example`).
