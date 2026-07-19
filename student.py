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

def search_student():
    name = input("Enter student name to search: ")
    found = False
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_name, students_class =   line.strip().split(",")
                if student_name.lower() == name.lower():
                    print(f"Name: {student_name}, Class: {students_class}")
                    found = True
                    break
        if not found:
            print(f"\nNo student record found for student '{name}'.")
    except FileNotFoundError:
        print("\nNo student registered.")
