
from student import register_student, view_students,search_student
from attendance import mark_attendance
from performance import add_marks, view_performance
print("===== Student Attendance & Performance Management System =====")

while True:
    print("\n1. Student Registration")
    print("2. View students")
    print("3. Attendance Management")
    print("4. Performance Evaluation")
    print("5. View Performance Report")
    print("6. Search Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        mark_attendance()

    elif choice == '4':
        add_marks()
    
    elif choice == '5':
        view_performance()
    
    elif choice == '6':
        search_student()
    elif choice == '7':
        print("Thankyou!!")
        break
    else:
        print("Invalid choice.") 
