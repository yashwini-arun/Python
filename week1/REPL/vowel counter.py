while True:
    try:
        text = input("Enter a string to count vowels: ")
        vowels = "aeiouAEIOU"
        count =sum(1 for char in text if char in vowels)
        print(f"The number of vowels in the string is : {count}")
        break
    except KeyboardInterrupt:
        print("\nExiting the program.")
        break
    
        