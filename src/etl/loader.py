from pathlib import Path
import pandas as pd
from loguru import logger

logger.add("logs/project.log", rotation="1 MB", level="INFO")

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA = PROJECT_ROOT / "data" / "raw"
OUTPUT = PROJECT_ROOT / "output"


def main():
    print("=" * 60)
    print("N100 Financial Intelligence Platform")
    print("Sprint 1 - Excel Loader")
    print("=" * 60)

    excel_files = sorted(RAW_DATA.glob("*.xlsx"))

    audit = []

    print(f"\nFound {len(excel_files)} Excel files\n")

    for file in excel_files:

        try:

            df = pd.read_excel(file)

            rows = len(df)
            cols = len(df.columns)

            print(f"📄 {file.name}")
            print(f"   Rows    : {rows}")
            print(f"   Columns : {cols}")
            print("-" * 60)

            logger.info(f"Loaded {file.name} ({rows} rows)")

            audit.append({
                "file_name": file.name,
                "rows_loaded": rows,
                "columns": cols,
                "status": "SUCCESS"
            })

        except Exception as e:

            logger.error(f"{file.name}: {e}")

            audit.append({
                "file_name": file.name,
                "rows_loaded": 0,
                "columns": 0,
                "status": "FAILED"
            })

    audit_df = pd.DataFrame(audit)

    OUTPUT.mkdir(exist_ok=True)

    audit_df.to_csv(
        OUTPUT / "load_audit.csv",
        index=False
    )

    print("\n✅ load_audit.csv generated successfully.")
    
if __name__ == "__main__":
    main()

   