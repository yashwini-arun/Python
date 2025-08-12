print("Welcome to Python Café!")
name = input("Enter your name: ")

coffee_qty = int(input("How many coffees? "))
cake_qty = int(input("How many cakes? "))

coffee_price = coffee_qty * 80
cake_price = cake_qty * 120
total = coffee_price + cake_price

if total >= 500:
    discount = 0.15
    print(" You get 15% discount!")
elif total >= 300:
    discount = 0.1
    print("You get 10% discount!")
else:
    discount = 0

total_after_discount = total - (total * discount)

if coffee_qty >= 2 and cake_qty >= 1:
    print(" Free cupcake added!")
    
print(f"Bill for {name}: ₹{total_after_discount}")
print("Thank you for visiting Python Café!")
