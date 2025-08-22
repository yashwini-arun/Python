import attendance

print("📅 Attendance Tracker")
print("-" * 40)

attendance.mark_present("Alice")
attendance.mark_absent("Bob")
attendance.mark_present("Charlie")

print("Alice:", attendance.get_status("Alice"))
print("Bob:", attendance.get_status("Bob"))
print("All Records:", attendance.all_records())
