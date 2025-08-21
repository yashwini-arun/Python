import logging

logging.basicConfig(filename="input.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

print("=== Integer Input Program ===")

try:
    value = input("Enter a number: ")
    num = int(value)
    print("You entered:", num)
    logging.info("Valid integer entered: %s", num)
except ValueError as e:
    logging.warning("Invalid input: %s", e)
    print("Error: Not a valid integer")
else:
    if num % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
finally:
    print("Execution completed.")
