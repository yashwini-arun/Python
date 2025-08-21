import logging

# Setup logging
logging.basicConfig(filename="math.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def divide_numbers(a, b):
    try:
        result = a / b
        logging.info("Division successful: %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError as e:
        logging.error("Division by zero error: %s", e)
        return None

print("=== Division Program ===")
num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
answer = divide_numbers(num1, num2)
if answer is not None:
    print("Result:", answer)
else:
    print("Error: Cannot divide by zero")
