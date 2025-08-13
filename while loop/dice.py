import random

score = 0
while score < 20:
    roll = random.randint(1, 6)
    print(f"You rolled: {roll}")
    score += roll
    if roll == 6:
        print("Bonus roll!")
    else:
        cont = input("Roll again? (y/n): ")
        if cont.lower() != "y":
            break
print(f"Final score: {score}")
