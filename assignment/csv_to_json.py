import csv
import json
import os

# Get the folder where this script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Use relative paths inside that folder
csv_file = os.path.join(base_dir, "employee.csv")
json_file = os.path.join(base_dir, "employee.json")

employees = []

try:
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(row)

    with open(json_file, mode='w') as file:
        json.dump(employees, file, indent=4)

    print(f"✅ Conversion successful! JSON saved as: {json_file}")

except FileNotFoundError:
    print(f"❌ File {csv_file} not found. Please check the path.")
