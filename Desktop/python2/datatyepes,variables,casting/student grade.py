name = input("Enter student name: ")
age = int(input("Enter age: "))        
math_score = float(input("Enter Math score: "))
science_score = float(input("Enter Science score: "))
english_score = float(input("Enter English score: "))
total = math_score + science_score + english_score
average = total / 3
avg_int = int(average)
if avg_int >= 90:
    grade = "A"
elif avg_int >= 75:
    grade = "B"
else:
    grade = "C"
print(f"\n{name} ({age} years old) scored an average of {average:.2f} → Grade: {grade}")
