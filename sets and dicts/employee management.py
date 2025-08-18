
employees = {
    101: {"name": "Arun", "dept": "HR", "salary": 35000},
    102: {"name": "Meena", "dept": "IT", "salary": 55000},
    103: {"name": "Ravi", "dept": "Finance", "salary": 45000}
}

for emp_id, details in employees.items():
    print(f"\nEmployee ID: {emp_id}")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

for emp_id, details in employees.items():
    if details["dept"] == "IT":
        details["salary"] *= 1.1

print("\nUpdated Employee Records:")
for emp_id, details in employees.items():
    print(emp_id, ":", details)
