import csv
import datetime

# Step 1: Write sample data into a text file (File I/O)
with open("library.txt", "w") as f:
    f.write("BookID,Title,Author,Available\n")
    f.write("1,Python Basics,John,Yes\n")
    f.write("2,Data Science,Alice,Yes\n")
    f.write("3,Machine Learning,Bob,No\n")
    f.write("4,AI with Python,Charlie,Yes\n")

print("✅ Library data written to library.txt")

# Step 2: Convert text file into CSV
with open("library.txt", "r") as f:
    lines = f.readlines()

with open("library.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line.strip().split(","))

print("✅ Data transferred to library.csv")

# Step 3: Borrow a book
book_id = input("\nEnter Book ID to borrow: ")
borrower = input("Enter your name: ")
date = datetime.date.today()

updated_books = []
borrowed = None

with open("library.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["BookID"] == book_id and row["Available"] == "Yes":
            row["Available"] = "No"
            borrowed = (row["Title"], borrower, str(date))
        updated_books.append(row)

# Step 4: Update library CSV with new availability
with open("library.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["BookID", "Title", "Author", "Available"])
    writer.writeheader()
    writer.writerows(updated_books)

# Step 5: Record borrowed book in transactions.csv
if borrowed:
    with open("transactions.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(borrowed)
    print(f"\n📖 Book '{borrowed[0]}' borrowed by {borrowed[1]} on {borrowed[2]}")
else:
    print("\n❌ Book not available or invalid ID")
