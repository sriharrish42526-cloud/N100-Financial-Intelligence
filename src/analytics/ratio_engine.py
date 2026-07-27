"""
ratio_engine.py

Financial Ratio Engine
Sprint 2
"""

from pathlib import Path
import sqlite3
import pandas as pd
from loguru import logger

from src.analytics.ratios import (
    net_profit_margin,
    debt_to_equity,
    asset_turnover,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_FILE = PROJECT_ROOT / "db" / "nifty100.db"

logger.add("logs/project.log", rotation="1 MB")


def load_data(conn):

    query = """
    SELECT

        p.company_id,
        p.year,

        p.sales,
        p.net_profit,
        p.eps,

        b.assets,
        b.liabilities,
        b.equity

    FROM profitandloss p

    INNER JOIN balancesheet b

    ON p.company_id = b.company_id
    AND p.year = b.year

    ORDER BY p.company_id, p.year
    """

    return pd.read_sql(query, conn)


def calculate_ratios(df):

    output = []

    for _, row in df.iterrows():

        output.append({

            "company_id": row["company_id"],

            "year": row["year"],

            "net_profit_margin_pct":
                net_profit_margin(
                    row["net_profit"],
                    row["sales"]
                ),

            "debt_to_equity":
                debt_to_equity(
                    row["liabilities"],
                    row["equity"],
                    0
                ),

            "asset_turnover":
                asset_turnover(
                    row["sales"],
                    row["assets"]
                ),

            "earnings_per_share":
                row["eps"]

        })

    return pd.DataFrame(output)


def save_ratios(df, conn):

    df.to_sql(
        "financial_ratios",
        conn,
        if_exists="replace",
        index=False
    )

    logger.info(f"{len(df)} ratio records saved.")


def main():

    print("=" * 60)
    print("FINANCIAL RATIO ENGINE")
    print("=" * 60)

    conn = sqlite3.connect(DB_FILE)

    df = load_data(conn)

    print(f"Loaded {len(df)} financial records")

    ratios = calculate_ratios(df)

    save_ratios(ratios, conn)

    print("\nPreview\n")

    print(ratios.head())

    conn.close()

    print("\nSUCCESS")


if __name__ == "__main__":
    main()