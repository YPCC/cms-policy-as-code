// Sample Cypher for Vitamin D Assay Testing LCD (L36692) pilot
// Run against a clean Neo4j database

MERGE (p:Policy {id: "L36692"})
SET p.title = "Vitamin D Assay Testing",
    p.type = "LCD",
    p.effective_from = date("2017-02-03"),
    p.jurisdiction = "Noridian",
    p.source_uri = "cms://lcd/L36692"

MERGE (cpt1:CPT {code: "82306"})
SET cpt1.display = "Vitamin D; 25 hydroxy",
    cpt1.system = "CPT"

MERGE (cpt2:CPT {code: "82652"})
SET cpt2.display = "Vitamin D; 1, 25 dihydroxy",
    cpt2.system = "CPT"

MERGE (p)-[:APPLIES_TO]->(cpt1)
MERGE (p)-[:APPLIES_TO]->(cpt2)

// Covered diagnoses (simplified)
MERGE (d1:ICD10 {code: "N18.3"})
SET d1.display = "Chronic kidney disease, stage 3"

MERGE (d2:ICD10 {code: "E21.0"})
SET d2.display = "Primary hyperparathyroidism"

MERGE (d3:ICD10 {code: "M81.0"})
SET d3.display = "Age-related osteoporosis without current pathological fracture"

MERGE (p)-[:COVERS_IF_DIAGNOSIS]->(d1)
MERGE (p)-[:COVERS_IF_DIAGNOSIS]->(d2)
MERGE (p)-[:COVERS_IF_DIAGNOSIS]->(d3)

// Limitation
MERGE (lim:Limitation {id: "NO_SCREENING"})
SET lim.description = "Vitamin D testing is not covered for routine screening",
    lim.type = "no_screening"

MERGE (p)-[:HAS_LIMITATION]->(lim)
