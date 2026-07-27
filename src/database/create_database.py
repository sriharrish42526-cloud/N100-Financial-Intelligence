from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DB_FILE = PROJECT_ROOT / "db" / "nifty100.db"
SCHEMA_FILE = PROJECT_ROOT / "db" / "schema.sql"


def main():

    conn = sqlite3.connect(DB_FILE)

    conn.execute("PRAGMA foreign_keys = ON")

    with open(SCHEMA_FILE, "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("✅ SQLite database created successfully")


if __name__ == "__main__":
    main()