students = []
def register_student():
    name = input("Enter student name: ")
    student_class = input("Enter student class: ")
    student = {"name": name, "class": student_class}
    students.append(student)
    with open("students.txt", "a") as file:
        file.write(f"{name},{student_class}\n")
    print(f"Student {name} registered successfully.")
def view_students():
    if not students:
        print("\nNo students registered.")
    else:
        print("\nRegistered Students:")
        for student in students:
            print(f"Name: {student['name']}, Class: {student['class']}")