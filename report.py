def generate_report():
    # Implementation for generating report
    name = input("Enter student name to generate report: ")
    print("\n============ ")
    print("Student Report ")
    print("============ \n") 
    found = False
    
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_name, student_class = line.strip().split(",")
                if student_name.lower() == name.lower():
                    print(f"Name: {student_name}, Class: {student_class}")
                    found = True
                    break
        if not found:
            print(f"\nNo student record found for student '{name}'.")
            return

    except FileNotFoundError:
        print("\nNo students Registered.")
    try:
        with open("attendance.txt","r") as file:
            for line in file: 
                if line.startswith("#"):continue
                data = line.strip().split(",")
                if len(data) == 3:
                    student_name = data[0]
                    total = int(data[1])
                    present = int(data[2])
                    if student_name.lower() == name.lower():
                    
                     absent  = total - present
                     percentage = (present/total)*100
                     print(f"\nAttendance: Total Days: {total}, \nPresent: {present}, \nAbsent:{absent}, Percentage: {percentage:.2f}%")
                     break
    except FileNotFoundError:
        print("No Attendance records found.")
        print("\nMarks:")
        marks = 0
    try:
        with open("performance.txt","r")as file:
            for line in file:
                if line.startswith("#"):continue
                student_name, student_marks = line.strip().split(",")
                if student_name.lower() == name.lower():
                    marks = float(student_marks)
                    print(f"\nMarks: {marks}")
                    break
    except FileNotFoundError:
        print("No marks records found.")
    if marks >= 90:
            grade = "A+"
    elif marks >= 80:
            grade = "A"
    elif marks >= 70:
            grade = "B"
    elif marks >= 60:
            grade = "C"
    elif marks >= 40:
            grade = "D"
    else:
            grade = "FAIL"
    print(f"\nGrade: {grade}")
    print("\nResult:")
    if marks >= 40:
            print("PASS")
    else:
            print("FAIL")