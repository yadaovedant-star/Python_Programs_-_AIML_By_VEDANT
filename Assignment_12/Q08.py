# Q8. Tuples + Dictionaries + OOP
# Program: Employee class with tuple details and dictionary storage

class Employee:
    def __init__(self, emp_id, name, details):
        # details is a tuple (department, salary)
        self.emp_id = emp_id
        self.name = name
        self.details = details

    def show_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.details[0]}")
        print(f"Salary: {self.details[1]}")
        print("---------------------------")


# Dictionary: key = emp_id, value = Employee object
employees = {}

# Add 3 employees
employees[101] = Employee(101, "Rahul", ("IT", 50000))
employees[102] = Employee(102, "Sneha", ("HR", 45000))
employees[103] = Employee(103, "Vedant", ("Finance", 60000))

# Display all employees using loop
print("\n--- Employee Records ---")
for emp_id, emp_obj in employees.items():
    emp_obj.show_details()




