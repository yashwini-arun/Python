print(" Welcome to Space Mission Control ")
name = input("Astronaut, what’s your name? ")

fuel = int(input("Enter fuel level (0-100): "))
weather = input("Is space weather clear or stormy? ").lower()

if fuel < 30:
    status = " Not enough fuel for launch!"
elif weather == "stormy":
    status = " Weather too risky. Mission postponed."
else:
    decision = input("All systems go. Launch now? (yes/no): ").lower()
    if decision == "yes":
        status = "Lift-off successful! Enjoy your mission, Commander!"
    else:
        status = "Mission aborted by commander’s choice."

print(f"\nCommander {name}, Mission Status: {status}")
print("End of Transmission ")
