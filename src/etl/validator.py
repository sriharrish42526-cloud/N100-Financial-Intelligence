"""
validator.py

Sprint 1
Data Quality Validator
"""

from pathlib import Path
import pandas as pd
from loguru import logger

# ------------------------------------
# Project Paths
# ------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = PROJECT_ROOT / "data" / "raw"
OUTPUT = PROJECT_ROOT / "output"

logger.add("logs/project.log", rotation="1 MB")


class Validator:

    def __init__(self):
        self.failures = []

    # ------------------------------------
    # Store Validation Failure
    # ------------------------------------

    def add_failure(self, rule, severity, file_name, message):

        self.failures.append({
            "rule": rule,
            "severity": severity,
            "file": file_name,
            "message": message
        })

    # ------------------------------------
    # Save Report
    # ------------------------------------

    def save_report(self):

        OUTPUT.mkdir(exist_ok=True)

        df = pd.DataFrame(self.failures)

        df.to_csv(
            OUTPUT / "validation_failures.csv",
            index=False
        )

        print("\n✅ validation_failures.csv generated")

    # ------------------------------------
    # DQ-01
    # Primary Key
    # ------------------------------------

    def check_company_primary_key(self):

        df = pd.read_excel(RAW_DATA / "companies.xlsx")

        duplicates = df[df["company_id"].duplicated()]

        if duplicates.empty:

            print("✅ DQ-01 Passed : company_id is unique")

        else:

            print("❌ DQ-01 Failed")

            for _, row in duplicates.iterrows():

                self.add_failure(
                    "DQ-01",
                    "CRITICAL",
                    "companies.xlsx",
                    f"Duplicate company_id : {row['company_id']}"
                )

    # ------------------------------------
    # DQ-02
    # Company + Year uniqueness
    # ------------------------------------

    def check_company_year_uniqueness(self):

        df = pd.read_excel(RAW_DATA / "profitandloss.xlsx")

        duplicates = df[df.duplicated(
            subset=["company_id", "year"],
            keep=False
        )]

        if duplicates.empty:

            print("✅ DQ-02 Passed : (company_id, year) is unique")

        else:

            print("❌ DQ-02 Failed")

            for _, row in duplicates.iterrows():

                self.add_failure(
                    "DQ-02",
                    "CRITICAL",
                    "profitandloss.xlsx",
                    f"Duplicate ({row['company_id']}, {row['year']})"
                )

    # ------------------------------------
    # DQ-03
    # Foreign Key Integrity
    # ------------------------------------

    def check_foreign_key(self):

        companies = pd.read_excel(RAW_DATA / "companies.xlsx")

        pnl = pd.read_excel(RAW_DATA / "profitandloss.xlsx")

        valid_company_ids = set(companies["company_id"])

        invalid = pnl[
            ~pnl["company_id"].isin(valid_company_ids)
        ]

        if invalid.empty:

            print("✅ DQ-03 Passed : Foreign Key Integrity")

        else:

            print("❌ DQ-03 Failed")

            for _, row in invalid.iterrows():

                self.add_failure(
                    "DQ-03",
                    "CRITICAL",
                    "profitandloss.xlsx",
                    f"Invalid company_id : {row['company_id']}"
                )


# ------------------------------------
# Main
# ------------------------------------

if __name__ == "__main__":

    print("=" * 55)
    print("Running Data Quality Checks")
    print("=" * 55)

    validator = Validator()

    validator.check_company_primary_key()

    validator.check_company_year_uniqueness()

    validator.check_foreign_key()

    validator.save_report()

    print("\n🎉 Validation Complete")