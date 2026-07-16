attendance_records = {}
def mark_attendance():
    name = input("Enter student name:")
    status = input("Present or Absent(P/A): ")
    attendance_records[name] = status.upper()
    print("Attendance marked successfully.")
