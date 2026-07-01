# Q5. Dictionaries + Functions + Control Structures
# Program: Student Database using dictionary, functions, and exception handling

def student_database():
    students = {}  # roll number as key, details as value

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Search Student by Roll Number")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        # 1. Add Student
        if choice == "1":
            try:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                # store in dictionary
                students[roll] = {"name": name, "age": age, "city": city}
                print("Student added successfully!")
            except ValueError:
                print("Invalid input! Roll number and age must be numeric.")

        # 2. Search Student
        elif choice == "2":
            try:
                roll = int(input("Enter Roll Number to search: "))
                student = students.get(roll)  # get() method
                if student:
                    print("Student Found:", student)
                else:
                    print("Student not found!")
            except ValueError:
                print("Invalid input! Roll number must be numeric.")

        # 3. Display All Students
        elif choice == "3":
            if students:
                print("\nAll Students:")
                for roll, details in students.items():  # items() method
                    print("Roll:", roll, "Details:", details)
            else:
                print("No student records available.")

        # 4. Exit
        elif choice == "4":
            print("Exiting Student Database. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter between 1-4.")


# Call the function
student_database()
