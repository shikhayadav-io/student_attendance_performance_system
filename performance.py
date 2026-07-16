performance_records = {}
def add_marks():
    name = input("Enter student name: ")
    marks = float(input("Enter marks:"))
    performance_records[name] =marks 
    print("Marks added successfully.")
def view_performance():
    if not performance_records:
        print("\nNo performance records available.")
    else:
        print("\nPerformance Records:")
        for name, marks in performance_records.items():
            print(f"Name: {name}, Marks: {marks}")
 
