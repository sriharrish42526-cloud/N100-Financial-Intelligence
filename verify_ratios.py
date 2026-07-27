import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM financial_ratios")
count = cursor.fetchone()[0]

print("=" * 50)
print("FINANCIAL RATIOS TABLE")
print("=" * 50)
print(f"Rows : {count}")

print("\nSample Records\n")

cursor.execute("""
SELECT *
FROM financial_ratios
LIMIT 10
""")

for row in cursor.fetchall():
    print(row)

conn.close()