print("=== Weather Outfit Advisor ===")
name = input("Enter your name: ")

temp = int(input("Enter temperature in °C: "))
weather = input("Is it sunny, cloudy, or rainy? ").lower()

if temp < 10:
    outfit = "Warm jacket and gloves"
elif temp < 20:
    outfit = "Light sweater"
else:
    outfit = "T-shirt and shorts"

if weather == "rainy":
    extra = "Don't forget an umbrella!"
elif weather == "sunny" and temp > 25:
    extra = "Wear sunglasses and drink water!"
else:
    extra = "Enjoy your day!"

print(f"\nHello {name}!")
print(f"Suggested outfit: {outfit}")
print(extra)
print("=== Stay safe & stylish! ===")
