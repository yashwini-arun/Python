import csv

# Step 1: Write data to a text file (File I/O)
with open("students.txt", "w") as f:
    f.write("Name,Subject,Marks\n")
    f.write("Alice,Math,85\n")
    f.write("Bob,Science,90\n")
    f.write("Charlie,History,78\n")

print("✅ Data written to students.txt")

# Step 2: Read from the text file and write into a CSV file
with open("students.txt", "r") as f:
    lines = f.readlines()

with open("students.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for line in lines:
        writer.writerow(line.strip().split(","))

print("✅ Data transferred to students.csv")

# Step 3: Read CSV file and process data
with open("students.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    total_marks = 0
    count = 0
    for row in reader:
        print(f"Student: {row[0]}, Subject: {row[1]}, Marks: {row[2]}")
        total_marks += int(row[2])
        count += 1

    print(f"\n📊 Average Marks: {total_marks/count}")
