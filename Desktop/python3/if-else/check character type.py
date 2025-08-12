char = input("Enter a character: ")

def check_character_type(char):
    if char.isupper():
        print("The character is an uppercase letter.")
    elif char.islower():
        print("The character is a lowercase letter.")
    elif char.isdigit():
        print("The character is a digit.")
    elif char.isspace():
        print("The character is a whitespace character.")
    else:
        print("The character is a special character.")

check_character_type(char)
