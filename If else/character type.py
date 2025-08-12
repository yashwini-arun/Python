char = input("Enter a character: ")

if char.isdigit():
    print("It's a digit.")
elif char.isalpha():
    if char.isupper():
        print("Uppercase letter.")
    else:
        print("Lowercase letter.")
else:
    print("Special character.")
