performance_records = {}
def add_marks():
    name = input("Enter student name: ")
    marks = float(input("Enter marks:"))
    performance_records[name] =marks 
    with open("performance.txt", "a") as file:
        file.write(f"{name},{marks}\n")
    print("Marks added successfully.")
def view_performance():
    if not performance_records:
        print("\nNo performance records available.")
    else:
        print("\nPerformance Records:")
        for name, marks in performance_records.items():
            print(f"Name: {name}, Marks: {marks}")
def view_performance():
    try:
        with open("performance.txt", "r") as file:   
            print("\nPerformance Records:")
            print (file.read())
    except FileNotFoundError:
        print("\nNo performance records available.")

