"""Starter script to pull a sample LCD and related Article via the CMS Coverage API.

This demonstrates the path to live data. LCD and Article detail endpoints require
a short-lived license agreement Bearer token.

Usage:
    python scripts/fetch_sample_lcd_article.py

Environment:
    No API key required. The script requests a license token automatically.
"""

from __future__ import annotations

import json
import os
from typing import Any

import requests

BASE_URL = "https://api.coverage.cms.gov"
# Example: Vitamin D Assay Testing LCD used in the pilot
SAMPLE_LCD_ID = "L36692"


def get_license_token() -> str:
    """Obtain a short-lived license agreement token.

    Calling this endpoint implies acceptance of the AMA/ADA/AHA license terms.
    Token is valid for approximately one hour.
    """
    url = f"{BASE_URL}/v1/metadata/license-agreement"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    # Response shape may vary; adjust if the key differs
    token = data.get("token") or data.get("licenseToken") or data.get("access_token")
    if not token:
        raise RuntimeError(f"Could not extract token from response: {data}")
    return token


def api_get(path: str, token: str | None = None, params: dict[str, Any] | None = None) -> dict[str, Any]:
    url = f"{BASE_URL}{path}"
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = requests.get(url, headers=headers, params=params or {}, timeout=60)
    resp.raise_for_status()
    return resp.json()


def fetch_lcd(lcd_id: str, token: str) -> dict[str, Any]:
    """Fetch LCD document-level information."""
    # Endpoint pattern from Coverage API release notes
    return api_get(f"/v1/data/lcd/{lcd_id}", token=token)


def fetch_related_articles(lcd_id: str, token: str) -> list[dict[str, Any]]:
    """Attempt to locate related Articles for an LCD.

    Exact endpoint may need adjustment based on current OpenAPI.
    Common patterns include search or related-document endpoints.
    """
    # Placeholder — replace with the actual related-article or search endpoint
    # once confirmed against Swagger.
    try:
        return api_get("/v1/data/article/", token=token, params={"lcdId": lcd_id})
    except requests.HTTPError:
        print("Related-article endpoint pattern may need update. Falling back to empty list.")
        return []


def main() -> None:
    print("Requesting license agreement token...")
    token = get_license_token()
    print("Token obtained (valid ~1 hour).\n")

    print(f"Fetching LCD {SAMPLE_LCD_ID}...")
    try:
        lcd = fetch_lcd(SAMPLE_LCD_ID, token)
        print(json.dumps(lcd, indent=2)[:2000])  # truncate for console
        print("\n... (truncated)\n")
    except Exception as exc:
        print(f"LCD fetch failed: {exc}")
        print("Check the exact path against the current Swagger at")
        print("https://api.coverage.cms.gov/docs/swagger/index.html")

    print(f"Attempting to fetch related Articles for {SAMPLE_LCD_ID}...")
    articles = fetch_related_articles(SAMPLE_LCD_ID, token)
    print(f"Found {len(articles) if isinstance(articles, list) else 'unknown'} article(s).")
    if articles:
        print(json.dumps(articles[:1], indent=2)[:1500])

    print("\nDone. Next steps:")
    print("- Confirm exact endpoint paths against the live Swagger.")
    print("- Persist raw JSON under data/raw/ for provenance.")
    print("- Map into the LinkML schema and Neo4j load scripts.")


if __name__ == "__main__":
    main()
