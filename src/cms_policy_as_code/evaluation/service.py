"""Stub for the Claim Evaluation Service."""

from __future__ import annotations

from datetime import date
from typing import Any

from pydantic import BaseModel

from cms_policy_as_code.graph.neo4j_client import Neo4jClient


class ClaimRequest(BaseModel):
    claim_id: str
    cpt_code: str
    diagnosis_codes: list[str]
    date_of_service: date
    jurisdiction: str | None = None


class DecisionTrace(BaseModel):
    claim_id: str
    decision: str  # "covered" | "denied" | "review"
    matched_policy: str | None = None
    matched_diagnoses: list[str] = []
    limitations_applied: list[str] = []
    graph_version: str | None = None
    explanation: str


class ClaimEvaluationService:
    def __init__(self, client: Neo4jClient | None = None) -> None:
        self.client = client or Neo4jClient()

    def evaluate(self, claim: ClaimRequest) -> DecisionTrace:
        """Evaluate a claim against the Context Graph.

        This is a stub. In production it will:
        1. Query Neo4j for the relevant policy subgraph
        2. Apply deterministic rules
        3. Produce a full Decision Trace
        """
        # Example Cypher that a real implementation would run
        query = """
        MATCH (c:CPT {code: $cpt})<-[:APPLIES_TO]-(p:Policy)
        WHERE p.effective_from <= date($dos)
          AND (p.effective_to IS NULL OR p.effective_to >= date($dos))
        OPTIONAL MATCH (p)-[:COVERS_IF_DIAGNOSIS]->(d:ICD10)
        WHERE d.code IN $diagnoses
        RETURN p.id AS policy_id, collect(DISTINCT d.code) AS covered
        """
        params = {
            "cpt": claim.cpt_code,
            "dos": claim.date_of_service.isoformat(),
            "diagnoses": claim.diagnosis_codes,
        }

        try:
            results = self.client.run(query, params)
        except Exception as exc:  # noqa: BLE001
            return DecisionTrace(
                claim_id=claim.claim_id,
                decision="review",
                explanation=f"Graph query failed: {exc}",
            )

        if not results:
            return DecisionTrace(
                claim_id=claim.claim_id,
                decision="denied",
                explanation="No matching policy found for the procedure and date of service.",
            )

        row = results[0]
        covered = row.get("covered") or []
        if covered:
            return DecisionTrace(
                claim_id=claim.claim_id,
                decision="covered",
                matched_policy=row.get("policy_id"),
                matched_diagnoses=covered,
                explanation="Diagnosis matches covered indications under the policy.",
            )

        return DecisionTrace(
            claim_id=claim.claim_id,
            decision="denied",
            matched_policy=row.get("policy_id"),
            explanation="Procedure is covered by policy but diagnosis is not in the covered list.",
        )
