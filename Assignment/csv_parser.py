import csv
import logging

# Configure logging
logging.basicConfig(
    filename="csv_parser.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_csv(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader, start=1):
                try:
                    # Example: Expecting "id" as int, "name" as str, "age" as int
                    id_val = int(row["id"])
                    name_val = row["name"]
                    age_val = int(row["age"])
                    print(f"Row {row_num}: ID={id_val}, Name={name_val}, Age={age_val}")
                except (ValueError, KeyError) as e:
                    logging.error("Error parsing row %d: %s | Data: %s", row_num, e, row)
    except FileNotFoundError as e:
        logging.critical("CSV file not found: %s", e)
        print("Error: File not found.")
    except Exception as e:
        logging.critical("Unexpected error: %s", e)
        print("An unexpected error occurred.")

# Run the parser
if __name__ == "__main__":
    filename = input("Enter CSV filename: ")
    parse_csv(filename)
    print("CSV parsing complete. Check 'csv_parser.log' for errors.")
