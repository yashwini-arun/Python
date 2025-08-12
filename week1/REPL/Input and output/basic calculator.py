num1=float(input("Enter first number: "))
num2 =float(input("Enter second number: "))
operation =input("enter operation (+,-,*,/):").strip()
while True:
    try:
        if operation == "+":
            result = num1 + num2
        elif operation =="-":
            result = num1 - num2
        elif operation =="*":
            result = num1 * num2
        elif operation =="/":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid Operation")
        print(f"The result of {num1} {operation} {num2} is :{result}")
        break 
    except Exception as e:
        print(f"Error: {e}")
        break