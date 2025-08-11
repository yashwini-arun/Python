
name = input("Enter your name: ")
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("\n--- BMI Report ---")
print("Name:", name)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
else:
    print("Category: Overweight")
