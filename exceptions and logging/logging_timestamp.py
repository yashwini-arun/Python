import logging

logging.basicConfig(filename="timestamp.log", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

print("=== Timestamp Logging ===")

try:
    num = int(input("Enter a number: "))
    sqrt = num ** 0.5
    print("Square root:", sqrt)
    logging.info("Square root calculated successfully")
except ValueError as e:
    logging.error("Invalid conversion: %s", e)
    print("Error: Input was not a number")
except Exception as e:
    logging.critical("Unexpected error: %s", e)
    print("Unexpected error occurred")
finally:
    print("Execution finished")
