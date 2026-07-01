class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    def give_raise(self, amount):
        self.salary += amount
        print("New Salary after raise:", self.salary)

    def yearly_bonus(self):
        return self.salary * 0.10

emp1 = Employee("Vedant", 100000)

emp1.display_details()
emp1.give_raise(20000)
emp1.display_details()
print("Yearly Bonus:", emp1.yearly_bonus())


