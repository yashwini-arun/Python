
item1_price = float(input("Enter price of item 1: "))
item2_price = float(input("Enter price of item 2: "))
item3_price = float(input("Enter price of item 3: "))

total = item1_price + item2_price + item3_price
discount_rate = int(input("Enter discount percentage: "))
discount_amount = (discount_rate / 100) * total
final_amount = total - discount_amount

print("\n--- Bill ---")
print("Total Price:", total)
print("Discount:", discount_amount)
print("Amount to Pay:", final_amount)
print("Amount to Pay (Integer):", int(final_amount))
