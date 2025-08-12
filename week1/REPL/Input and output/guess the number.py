secret = 7
guess = int(input("Guess the secret number(between 1 and 10):"))
if guess< secret:
        print("Too low! Try again.")
else:
        print("Too high! Try again.")
        guess = int(input("Guess the secret number(between 1 and 10):"))
        print("Congratulations! You've guessed the secret number.")
