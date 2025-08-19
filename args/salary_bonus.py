
def total_salary(*bonuses):
    """Adds different types of salary bonuses"""
    return sum(bonuses)

print("=== Salary Bonus Calculator ===")
print("Enter bonuses (festival, performance, allowance): ")
bonuses = list(map(int, input().split()))
salary = total_salary(*bonuses)
print("Bonuses:", bonuses)
print("Total Bonus Earned: ₹", salary)
if salary > 50000:
    print("High Bonus Category!")
else:
    print("Normal Bonus Category.")
