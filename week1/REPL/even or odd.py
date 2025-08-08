while True:
    try:
        number =int(input("enter a number: "))
        if number % 2==0:
            print("the number is even")
            break
        else:
            print("the number is odd")
    except ValueError:
            print("Please enter a vaid integer.")
    except KeyboardInterrupt:
        print("\nExiting the program.")
        break
    except Exception as e:
         print(f"An unexpectd error occured: {e}")
   


