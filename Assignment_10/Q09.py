# Q9. Debugging OOP Code

class Person:   # define a class named Person
    def __init__(self, name, age):   # FIX: added self as first parameter
        self.name = name             # FIX: use self.name to assign to object attribute
        self.age = age               # FIX: use self.age to assign to object attribute

    def introduce(self):   # FIX: added self as first parameter in method
        # FIX: corrected print syntax by using commas instead of string concatenation errors
        print("My name is", self.name, "and I am", self.age, "years old.")

# create object of Person class
p1 = Person("Annirudh", )   # FIX: constructor now works with self, name, age
p1.introduce()             # FIX: method call works because self is included


