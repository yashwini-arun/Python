import logging

logging.basicConfig(filename="list.log", level=logging.DEBUG,
                    format="%(levelname)s - %(message)s")

print("=== List Access Program ===")
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index to access: "))
    value = numbers[index]
    print("Value at index", index, "is", value)
    logging.info("Access successful at index %d", index)
except IndexError as e:
    logging.error("Index out of range: %s", e)
    print("Error: Index not valid")
except ValueError as e:
    logging.warning("Invalid input: %s", e)
    print("Error: Please enter a number")
finally:
    print("List access completed.")
