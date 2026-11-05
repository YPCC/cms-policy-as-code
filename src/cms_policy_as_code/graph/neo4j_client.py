"""Small Neo4j connection helper for the Context Graph."""

from __future__ import annotations

import os
from typing import Any

from neo4j import GraphDatabase, Driver


class Neo4jClient:
    def __init__(
        self,
        uri: str | None = None,
        user: str | None = None,
        password: str | None = None,
    ) -> None:
        self.uri = uri or os.getenv("NEO4J_URI", "bolt://localhost:7687")
        self.user = user or os.getenv("NEO4J_USER", "neo4j")
        self.password = password or os.getenv("NEO4J_PASSWORD", "password")
        self._driver: Driver | None = None

    def connect(self) -> Driver:
        if self._driver is None:
            self._driver = GraphDatabase.driver(
                self.uri, auth=(self.user, self.password)
            )
        return self._driver

    def close(self) -> None:
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    def run(self, query: str, parameters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        driver = self.connect()
        with driver.session() as session:
            result = session.run(query, parameters or {})
            return [record.data() for record in result]

    def __enter__(self) -> "Neo4jClient":
        self.connect()
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
