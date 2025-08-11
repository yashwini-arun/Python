
total_cost = float(input("Enter total trip cost: "))
people = int(input("Enter number of people: "))

cost_per_person = total_cost / people
print("\n--- Trip Summary ---")
print("Total Cost:", total_cost)
print("Number of People:", people)
print("Cost per Person:", round(cost_per_person, 2))

print("Cost per Person (int):", int(cost_per_person))
