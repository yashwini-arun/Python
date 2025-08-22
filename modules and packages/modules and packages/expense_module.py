import csv
import datetime

FILENAME = "expenses.csv"

def init_file():
    try:
        with open(FILENAME, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount"])
    except FileExistsError:
        pass

def add_expense(category, amount):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])

def total_expenses():
    total = 0
    with open(FILENAME, "r") as f:
        next(f)
        for line in f:
            total += float(line.strip().split(",")[2])
    return total
