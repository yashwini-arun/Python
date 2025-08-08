choice = input("Convert to (C)elsius or (F)ahrenheit? ").upper()
temp = float(input("Enter temperature: "))

if choice == 'F':
    result = (temp * 9/5) + 32
    print(f"{temp}°C = {result:.2f}°F")
elif choice == 'C':
    result = (temp - 32) * 5/9
    print(f"{temp}°F = {result:.2f}°C")
else:
    print("Invalid option.")
