from pathlib import Path
import sqlite3
import pandas as pd
from loguru import logger

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA = PROJECT_ROOT / "data" / "raw"
DB_FILE = PROJECT_ROOT / "db" / "nifty100.db"

logger.add("logs/project.log", rotation="1 MB")


def load_table(conn, excel_file, table_name):

    df = pd.read_excel(RAW_DATA / excel_file)

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    print(f"✅ Loaded {len(df)} rows into {table_name}")

    logger.info(f"{table_name} : {len(df)} rows loaded")


def main():

    conn = sqlite3.connect(DB_FILE)

    conn.execute("PRAGMA foreign_keys = ON")

    print("=" * 60)
    print("Loading Excel Files into SQLite")
    print("=" * 60)

    load_table(conn, "companies.xlsx", "companies")
    load_table(conn, "profitandloss.xlsx", "profitandloss")
    load_table(conn, "balancesheet.xlsx", "balancesheet")
    load_table(conn, "cashflow.xlsx", "cashflow")
    load_table(conn, "analysis.xlsx", "analysis")
    load_table(conn, "documents.xlsx", "documents")
    load_table(conn, "prosandcons.xlsx", "prosandcons")
    load_table(conn, "sectors.xlsx", "sectors")
    load_table(conn, "stock_prices.xlsx", "stock_prices")
    load_table(conn, "peer_groups.xlsx", "peer_groups")

    conn.commit()
    conn.close()

    print("\n🎉 Database Loading Completed")


if __name__ == "__main__":
    main()