# C4 Deployment Diagram (GCP)

```mermaid
C4Deployment
  title Deployment Diagram - GCP Production

  Deployment_Node(client, "Client / Claims Platform", "External") {
    Container(claimsSystem, "Claims & Prior-Auth Systems", "Enterprise", "Submits requests")
  }

  Deployment_Node(gcp, "Google Cloud Platform", "us-central1") {
    Deployment_Node(run, "Cloud Run / GKE", "Managed") {
      Container(evalService, "Claim Evaluation Service", "Python / FastAPI", "Low-latency decision path")
      Container(adminApi, "Admin & Review API", "Python / FastAPI", "Human review and promotion")
      Container(ingestion, "Policy Ingestion Service", "Python", "Document conversion")
      Container(extraction, "Knowledge Extraction Pipeline", "Python", "Batch / event-driven extraction")
    }

    Deployment_Node(neo4j, "Neo4j", "Aura or GCE") {
      ContainerDb(graphStore, "Context Graph Store", "Neo4j", "Versioned policy graph")
    }

    Deployment_Node(storage, "Cloud Storage", "Regional") {
      ContainerDb(docStore, "Immutable Document Packages", "GCS", "docling-context .dclx and source artifacts")
    }

    Deployment_Node(logging, "Cloud Logging / BigQuery", "Managed") {
      ContainerDb(auditLog, "Audit & Decision Trace Store", "BigQuery", "Immutable traces and analytics")
    }
  }

  Rel(claimsSystem, evalService, "HTTPS")
  Rel(evalService, graphStore, "Bolt / Cypher")
  Rel(evalService, auditLog, "Writes traces")
  Rel(ingestion, docStore, "Stores packages")
  Rel(extraction, graphStore, "Loads triples")
```

## Notes

- Evaluation path is sized for sub-second latency under expected claim volume
- Extraction path is batch-oriented and can scale independently
- All Decision Traces and graph versions are retained for audit
- Secrets and coding-system licenses managed via Secret Manager / appropriate controls
