import logging
from fetcher import fetch_data
from database import Database
from analyzer import analyze_data
from report import generate_report
from config import DB_PATH


def main():
    logging.basicConfig(level=logging.INFO)

    db = Database(DB_PATH)

    try:
        data = fetch_data()
        db.insert_data(data)
        logging.info("Data fetched and inserted successfully.")
    except Exception as e:
        logging.error(f"Failed to fetch or insert data: {e}")
        return

    rows = db.fetch_all_data()
    danger_periods, daily_report = analyze_data(rows)
    report = generate_report(danger_periods, daily_report)

    print(report)


if __name__ == "__main__":
    main()
