num = int(input("Enter a number: "))
steps = 0

while num != 1:
    print(num, end=" -> ")
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    steps += 1
print(1)
print(f"Total steps: {steps}")
