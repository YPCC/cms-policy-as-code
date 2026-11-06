"""Starter script for the Laboratory NCD ICD-10 code lists.

This is the second major CMS source after the Coverage API. The Lab NCD lists
are the best structured ground truth available for medical-necessity evaluation
(covered / non-covered / do-not-support-medical-necessity diagnosis codes for
~23 laboratory NCDs).

The lists are published as quarterly ZIP files on:
https://www.cms.gov/medicare/coverage/determination-process/basics/lab-ncds-icd-10

Usage:
    python scripts/fetch_lab_ncd_icd10.py

The script currently demonstrates the download + extraction pattern. Update the
ZIP_URL constant to the latest file linked from the CMS page.
"""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import requests

# Update this URL to the latest ZIP linked from the CMS Lab NCD page.
# Example pattern (verify on the page):
# https://www.cms.gov/files/zip/october-2026-lab-code-list-icd-10.zip
ZIP_URL = "https://www.cms.gov/files/zip/october-2026-lab-code-list-icd-10.zip"

OUTPUT_DIR = Path("data/raw/lab_ncd_icd10")


def download_and_extract(url: str, dest: Path) -> None:
    """Download the Lab NCD ZIP and extract its contents."""
    dest.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {url} ...")
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        zf.extractall(dest)
        print(f"Extracted {len(zf.namelist())} files to {dest}")
        for name in zf.namelist()[:20]:
            print(f"  - {name}")


def summarize_extracted(dest: Path) -> None:
    """Print a short summary of what was extracted."""
    files = list(dest.rglob("*"))
    print(f"\nTotal files extracted: {len(files)}")
    csv_files = [f for f in files if f.suffix.lower() in {".csv", ".xlsx", ".xls"}]
    print(f"Spreadsheet/CSV files: {len(csv_files)}")
    for f in csv_files[:10]:
        print(f"  - {f.relative_to(dest)}")


def main() -> None:
    print("Laboratory NCD ICD-10 Code Lists")
    print("Source page: https://www.cms.gov/medicare/coverage/determination-process/basics/lab-ncds-icd-10")
    print()
    print("NOTE: Update ZIP_URL in this script to the current file linked on the CMS page.")
    print()

    try:
        download_and_extract(ZIP_URL, OUTPUT_DIR)
        summarize_extracted(OUTPUT_DIR)
        print("\nNext steps:")
        print("- Inspect the extracted spreadsheets (usually one sheet or file per NCD section).")
        print("- Map covered / non-covered / do-not-support lists into the Context Graph.")
        print("- Use these lists as high-quality ground truth for golden-claim construction.")
    except requests.HTTPError as exc:
        print(f"Download failed: {exc}")
        print("The ZIP URL may have changed. Visit the CMS page and update ZIP_URL.")
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
