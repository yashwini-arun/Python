import csv

# Step 1: Store employees in TXT
with open("employees.txt", "w") as f:
    f.write("201, John, 50000\n")
    f.write("202, Alice, 60000\n")
    f.write("203, Bob, 55000\n")

# Step 2: Convert TXT → CSV with allowances & deductions
with open("employees.txt", "r") as f, open("payroll.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["EmpID", "Name", "Basic", "HRA", "Tax", "NetSalary"])
    for line in f:
        emp_id, name, basic = line.strip().split(",")
        basic = int(basic)
        hra = 0.2 * basic
        tax = 0.1 * basic
        net = basic + hra - tax
        writer.writerow([emp_id, name.strip(), basic, hra, tax, net])

# Step 3: Display payroll
with open("payroll.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print("\n💰 Employee Payroll:")
    for row in reader:
        print(f"{row['Name']} → Net Salary: ₹{row['NetSalary']}")
