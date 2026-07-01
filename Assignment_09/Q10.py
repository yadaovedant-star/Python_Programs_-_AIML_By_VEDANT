# Dictionary to store student records
students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add New Student")
    print("2. Update Marks of a Student")
    print("3. Search Student by Roll Number")
    print("4. Display All Students")
    print("5. Remove a Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    # 1. Add new student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        marks = input("Enter Marks: ")

        # Nested dictionary for student details
        students[roll] = {"name": name, "age": age, "marks": marks}
        print("Student added successfully!")

    # 2. Update marks of a student
    elif choice == "2":
        roll = input("Enter Roll Number to update marks: ")
        if roll in students:
            new_marks = input("Enter new marks: ")
            students[roll].update({"marks": new_marks})  # update() method
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # 3. Search student by roll number
    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)  # get() method
        if student:
            print("Student Found:", student)
        else:
            print("Student not found!")

    # 4. Display all students
    elif choice == "4":
        print("\nAll Students:")
        for roll, details in students.items():  # items() method
            print("Roll:", roll, "Details:", details)

    # 5. Remove a student
    elif choice == "5":
        roll = input("Enter Roll Number to remove: ")
        removed = students.pop(roll, None)  # pop() method
        if removed:
            print("Removed Student:", removed)
        else:
            print("Student not found!")

    # 6. Exit
    elif choice == "6":
        print("Exiting Student Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter between 1-6.")
