# Assignment/utils/csv_parser.py
import csv
from pathlib import Path

def read_csv(filename):
    """Read rows from a CSV file as a list of dictionaries."""
    filepath = Path(filename)
    if not filepath.exists():
        return []

    with filepath.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(filename, fieldnames, rows):
    """Write rows (list of dicts) to a CSV file."""
    filepath = Path(filename)
    with filepath.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
