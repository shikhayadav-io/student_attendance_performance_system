attendance_records = {}
def mark_attendance():
    
    name = input("Enter student name:")
    status = input("Present or Absent(P/A): ")
    attendance_records[name] = status.upper()
    with open("attendance.txt", "a") as file:
        file.write(f"{name},{status}:\n")
    print("Attendance marked successfully.")
