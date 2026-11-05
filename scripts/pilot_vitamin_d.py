"""Pilot script: load Vitamin D LCD example and evaluate sample claims."""

from datetime import date

from cms_policy_as_code.evaluation.service import ClaimEvaluationService, ClaimRequest
from cms_policy_as_code.graph.neo4j_client import Neo4jClient


def load_sample_data(client: Neo4jClient) -> None:
    cypher = open("schemas/cypher/vitamin_d_lcd.cypher").read()
    # Simple split for demo; production would use better loading
    statements = [s.strip() for s in cypher.split(";") if s.strip() and not s.strip().startswith("//")]
    for stmt in statements:
        client.run(stmt)


def main() -> None:
    client = Neo4jClient()
    service = ClaimEvaluationService(client)

    print("Loading Vitamin D LCD sample data...")
    try:
        load_sample_data(client)
        print("Load complete.\n")
    except Exception as exc:
        print(f"Load skipped or failed (is Neo4j running?): {exc}\n")

    claims = [
        ClaimRequest(
            claim_id="CLAIM-001",
            cpt_code="82306",
            diagnosis_codes=["N18.3"],
            date_of_service=date(2024, 6, 15),
        ),
        ClaimRequest(
            claim_id="CLAIM-002",
            cpt_code="82306",
            diagnosis_codes=["Z00.00"],  # screening
            date_of_service=date(2024, 6, 15),
        ),
        ClaimRequest(
            claim_id="CLAIM-003",
            cpt_code="82306",
            diagnosis_codes=["E21.0", "N18.3"],
            date_of_service=date(2024, 6, 15),
        ),
    ]

    for claim in claims:
        trace = service.evaluate(claim)
        print(f"{trace.claim_id}: {trace.decision.upper()}")
        print(f"  Policy: {trace.matched_policy}")
        print(f"  Diagnoses: {trace.matched_diagnoses}")
        print(f"  Explanation: {trace.explanation}\n")

    client.close()


if __name__ == "__main__":
    main()
