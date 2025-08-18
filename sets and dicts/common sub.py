
student1_subjects = {"Math", "Science", "English", "History"}
student2_subjects = {"Science", "Math", "Computer", "Art"}

print("Subjects chosen by Student 1:", student1_subjects)
print("Subjects chosen by Student 2:", student2_subjects)


common = student1_subjects & student2_subjects
print("\nCommon Subjects:", common)


only_student1 = student1_subjects - student2_subjects
only_student2 = student2_subjects - student1_subjects

print("Subjects only Student 1 has:", only_student1)
print("Subjects only Student 2 has:", only_student2)


all_subjects = student1_subjects | student2_subjects
print("All unique subjects:", all_subjects)
