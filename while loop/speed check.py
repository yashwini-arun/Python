import time

text = "Python while loops can be fun!"
print("Type this sentence exactly:")
print(text)
start = time.time()
typed = ""

while typed != text:
    typed = input("Your input: ")
end = time.time()
speed = len(text.split()) / ((end - start) / 60)
print(f"Time taken: {end - start:.2f} seconds")
print(f"Speed: {speed:.2f} words per minute")
