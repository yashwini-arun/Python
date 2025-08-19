

def student_info(**kwargs):
    print("\n=== Student Information ===")
    for key, value in kwargs.items():
        print(f"{key.capitalize()} : {value}")

print("Enter student details")
name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")
roll = input("Enter roll number: ")
city = input("Enter city: ")

student_info(Name=name, Age=age, Course=course, Roll=roll, City=city)
