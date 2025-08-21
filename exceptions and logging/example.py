import logging

logging.basicConfig(filename="finally.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

print("=== File Reader with Finally ===")
filename = input("Enter filename: ")

f = None
try:
    f = open(filename, "r")
    content = f.read()
    print("File content:\n", content)
    logging.info("File opened successfully")
except FileNotFoundError as e:
    logging.error("File not found: %s", e)
    print("Error: File missing")
finally:
    if f:
        f.close()
        print("File closed properly")
        logging.info("File closed")
    print("Program ended.")
