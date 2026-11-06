# Data Sources for CMS Policy-as-Code / Context Graph

## Primary Policy Data (Authoritative)

The system is grounded in the **CMS Medicare Coverage Database (MCD)** and its APIs and bulk downloads.

| Source | Contents | Access | Notes |
|--------|----------|--------|-------|
| **Medicare Coverage Database (MCD)** | NCDs, LCDs, Billing & Coding Articles, contractor info, revision history | https://www.cms.gov/medicare-coverage-database/ | Primary human-readable source |
| **CMS Coverage API** (`https://api.coverage.cms.gov`) | Structured endpoints for NCDs, LCDs, Articles, HCPC codes, ICD-10 covered lists, contractors, revision history | OpenAPI/Swagger at `/docs/swagger/index.html` | Preferred for automation. Some LCD/Article endpoints require a short-lived license agreement Bearer token obtained from `/v1/metadata/license-agreement`. |
| **MCD Downloads** | Current + retired LCDs, Articles, NCDs | Zipped CSV + Access databases with data dictionaries | Bulk historical loads |
| **Laboratory NCD ICD-10 Code Lists** | National covered / non-covered / do-not-support-medical-necessity diagnosis lists for ~23 lab NCDs | Quarterly spreadsheets/ZIPs from CMS | Best structured ground truth for lab policies |
| **Standard coding systems** | ICD-10-CM, CPT, HCPCS, SNOMED CT, LOINC, RxNorm | Official releases + UMLS | Required for entity grounding |

**Important structural note**: Clinical narrative usually lives in the LCD; definitive CPT/HCPCS and ICD-10 covered lists live in companion **Billing and Coding Articles**. Extraction must join these correctly.

## Claims / Operational Data (Secondary, for Evaluation)

- **CMS Blue Button 2.0 / FHIR**: Beneficiary-authorized Medicare Part A/B/D claims. Sandbox provides synthetic data. Useful for realistic claim shapes, not public ground-truth labels.
- **Beneficiary Claims Data API (BCDA)**: Bulk FHIR claims for accountable care organizations.
- Real historical claims with denial reasons are typically proprietary to payers.

## Benchmark / Evaluation Datasets

There is no large public gold-standard benchmark of “claim + policy → correct coverage decision” for CMS NCD/LCD adjudication. Closest resources:

| Resource | What it offers | Limitations | Recommended use |
|----------|----------------|-------------|-----------------|
| **HICRIC** (Persius) | ~8,300 documents on health insurance coverage rules + annotated appeal task | Broader than pure CMS NCD/LCD | Pre-training or retrieval baselines |
| **Persius IMR-appeals** | Labeled appeal decisions with medical-necessity text | State-level IMR, not CMS LCD/NCD | Secondary evaluation |
| **CMS Lab NCD ICD-10 lists** | Explicit covered/non-covered diagnosis lists | Lab subset only | Best structured ground truth for golden claims |
| **Synthetic / hand-crafted golden claims** | Project-owned examples (e.g., Vitamin D LCD L36692) | Small and manual | Primary near-term benchmark; expand from official LCD/Article pairs |

## Practical Pilot Recommendation

1. Ingest via CMS Coverage API + MCD bulk downloads (LCDs + companion Articles + Lab NCD lists).
2. Ground all entities to official ICD-10-CM / CPT / HCPCS (and SNOMED where useful).
3. Build and version a golden-claim regression suite from official CMS sources. This suite becomes the project benchmark.

## Next Steps in Code

See `scripts/fetch_sample_lcd_article.py` for a starter that obtains a license token and fetches a sample LCD and related Article.
