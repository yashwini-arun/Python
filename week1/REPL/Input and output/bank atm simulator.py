balance = 10000
print("1. Withdraw\n2. Deposit\n3. Check Balance")
choice = int(input("Choose an option: "))

if choice == 1:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful. Remaining:", balance)
    else:
        print("Insufficient balance.")
elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful. Total:", balance)
elif choice == 3:
    print("Current Balance:", balance)
else:
    print("Invalid option.")
