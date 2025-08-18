
numbers = [1, 2, 2, 3, 4, 5, 5, 6, 1, 7, 8, 2, 9, 5]

frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Number Frequencies:")
for num, count in frequency.items():
    print(num, ":", count)

duplicates = {num for num, count in frequency.items() if count > 1}
print("\nDuplicate Numbers:", duplicates)
