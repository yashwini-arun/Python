attendance = {}

def mark_present(student):
    attendance[student] = "Present"

def mark_absent(student):
    attendance[student] = "Absent"

def get_status(student):
    return attendance.get(student, "Not marked")

def all_records():
    return attendance
