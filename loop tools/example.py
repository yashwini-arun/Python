# Python Loop Tools Example

print("1️For loop with range()")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

print("2️ While loop")
x = 0
while x < 5:
    print(x, end=" ")
    x += 1
print("\n")

print("3️ Break example")
for i in range(1, 6):
    if i == 4:
        print("Breaking at", i)
        break
    print(i, end=" ")
print("\n")

print("4️ Continue example")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print("\n")

print("5️ Else in loop example")
for i in range(3):
    print(i, end=" ")
else:
    print("\nLoop finished without break!")
print("\n")

print("6️ Enumerate example")
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
print("\n")

print("7️ Zip example")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
print("\n")

print("8️ Iter and Next example")
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))
