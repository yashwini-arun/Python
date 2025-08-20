import csv
import datetime

# Step 1: Create patient file
with open("patients.txt", "w") as f:
    f.write("ID,Name,Age,Disease,Admitted\n")
    f.write("1,Alice,30,Flu,Yes\n")
    f.write("2,Bob,45,Diabetes,No\n")

print("✅ Patient data written to patients.txt")

# Step 2: Convert to CSV
with open("patients.txt", "r") as f:
    lines = f.readlines()

with open("patients.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line.strip().split(","))

print("✅ Data saved to patients.csv")

# Step 3: Admit new patient
pid = input("\nEnter new Patient ID: ")
name = input("Enter name: ")
age = input("Enter age: ")
disease = input("Enter disease: ")
date = datetime.date.today()

with open("patients.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([pid, name, age, disease, "Yes"])

# Step 4: Record admission log
with open("admission_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([pid, name, disease, str(date)])

print(f"Patient {name} admitted on {date}")
