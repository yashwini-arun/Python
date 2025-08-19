
def restaurant_bill(*orders):
    """Adds all item costs from restaurant order"""
    return sum(orders)

print("=== Restaurant Order Calculator ===")
print("Enter food item prices separated by space: ")
items = list(map(float, input().split()))
bill = restaurant_bill(*items)
print("Your Order:", items)
print("Total Bill: ₹", bill)
if bill > 1000:
    print("You get a 10% discount!")
    print("Discounted Price: ₹", bill * 0.9)
else:
    print("No discount available.")
