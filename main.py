print("===== Student Attendance & Performance Management System =====")

while True:
    print("\n1. Student Registration")
    print("2. Attendance Management")
    print("3. Performance Evaluation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Student Registration Module")

    elif choice == '2':
        print("Attendance Management Module")

    elif choice == '3':
        print("Performance Evaluation Module")

    elif choice == '4':
        print("Thank you!!!")
        break

    else:
        print("Invalid choice.")
