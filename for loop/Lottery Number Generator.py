import random
numbers = []

for i in range(6):
    num = random.randint(1, 50)
    while num in numbers:
        num = random.randint(1, 50)
    numbers.append(num)
    print(f"Generated number: {num}")

print("\nYour lottery numbers are:", numbers)
print("Good luck!")
