print("🕵️ Welcome, Detective! A crime has been committed.")
name = input("What's your name, Detective? ")

place = input("Do you investigate the Park or the Library? ").lower()

if place == "park":
    clue = input("You see footprints. Follow them or Ignore? ").lower()
    if clue == "follow":
        print(" You found the thief hiding in a bush!")
    else:
        print("The thief escaped into the city.")
elif place == "library":
    clue = input("You hear whispers. Confront or Hide? ").lower()
    if clue == "confront":
        print("You caught the suspect stealing rare books!")
    else:
        print(" They slipped away unnoticed.")
else:
    print(" You got lost and found no clues.")

print(f"Case closed, Detective {name}!")
