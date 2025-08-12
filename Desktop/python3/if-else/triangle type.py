a= input("Enter the first side of the triangle: ")
b = input("Enter the second side of the triangle: ")
c =input("Enter the third side of the triangle: ")

if a==b and b==c:
    print("The triangle is equilateral.")
elif a==b or b==c or a==c:
    print("The triangle is isosceles.")
else:
    print("the triangle is scalene.")
    