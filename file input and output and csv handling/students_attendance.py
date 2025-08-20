import csv
import datetime

# Step 1: Create attendance list in a text file
with open("attendance.txt", "w") as f:
    f.write("RollNo,Name,Status\n")
    f.write("1,Alice,Present\n")
    f.write("2,Bob,Absent\n")
    f.write("3,Charlie,Present\n")

print("✅ Initial attendance written to attendance.txt")

# Step 2: Convert to CSV
with open("attendance.txt", "r") as f:
    lines = f.readlines()

with open("attendance.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line.strip().split(","))

print("✅ Data saved to attendance.csv")

# Step 3: Mark attendance for today
roll = input("\nEnter Roll No to update: ")
status = input("Enter status (Present/Absent): ")
date = datetime.date.today()

updated = []
with open("attendance.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["RollNo"] == roll:
            row["Status"] = status
        updated.append(row)

# Step 4: Save updates
with open("attendance.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["RollNo", "Name", "Status"])
    writer.writeheader()
    writer.writerows(updated)

# Step 5: Record update in log file
with open("attendance_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([roll, status, str(date)])

print(f"📌 Attendance updated for Roll {roll} on {date}")
