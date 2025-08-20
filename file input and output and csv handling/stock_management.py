import csv

# Step 1: Write stock details in TXT
with open("stock.txt", "w") as f:
    f.write("801, Rice, 50\n")
    f.write("802, Wheat, 20\n")
    f.write("803, Sugar, 10\n")
    f.write("804, Oil, 5\n")

# Step 2: Convert TXT → CSV with reorder check
with open("stock.txt", "r") as f, open("stock.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ItemID", "Item", "Qty", "Reorder"])
    for line in f:
        iid, item, qty = line.strip().split(",")
        qty = int(qty)
        reorder = "YES" if qty < 15 else "NO"
        writer.writerow([iid, item.strip(), qty, reorder])

# Step 3: Print reorder list
with open("stock.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print("\n🏪 Items to Reorder:")
    for row in reader:
        if row["Reorder"] == "YES":
            print(f"{row['Item']} (Qty: {row['Qty']})")
