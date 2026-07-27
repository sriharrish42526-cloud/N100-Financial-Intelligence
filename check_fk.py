import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_key_check;")
rows = cursor.fetchall()

if not rows:
    print("✅ Foreign Keys OK")
else:
    print(rows)

conn.close()