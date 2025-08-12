print("Welcome to Treasure Hunt Adventure!")
print("your mission is to find the hidden treasure.")
print("Your journey begins at a fork in the road.")
choice = input("Do you want to go left or right? (left/right): ").lower()
if choice == "left":
    print("You encounter a river. Do you want to swim across or wait for a boat? (swim/wait): ")
    river_choice = input().lower()
    if river_choice == "wait":
        print("You safely crossed the river and found a treasure chest!")
        print("Congratulations! You found the treasure!")
    else:
        print("You were swept away by the current.")
        print("Game Over.")
elif choice == "right":
    print("You encounter a wild animal .Do you want to fight or run? (fight/run):")
    animal_choice = input().lower()
    if animal_choice == "fight":
        print("You bravely fought the animal and found a treasure chest!")
        print("Congratulations! You found the treasure!")
    else:
        print("You ran away safely , but you didnt find the treasure.")
        print("Game Over.")
else:
    print("Invalid choice. Please start again.")
    print("Game Over.")