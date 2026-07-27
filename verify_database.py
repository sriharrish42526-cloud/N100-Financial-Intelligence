import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "sectors",
    "stock_prices",
    "peer_groups"
]

print("=" * 50)
print("DATABASE VERIFICATION")
print("=" * 50)

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"{table:<20} {count}")

conn.close()