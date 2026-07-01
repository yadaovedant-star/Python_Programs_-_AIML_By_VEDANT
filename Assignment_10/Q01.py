# Q1. Basic Class and Object

class Car:   # define a class named Car
    def __init__(self, brand, model):   # constructor to initialize attributes
        self.brand = brand   # store brand name
        self.model = model   # store model name

    def display_info(self):   # method to display car details
        print("Brand:", self.brand) 
        print("Model:", self.model)   # print brand and model

# create first object of Car class
car1 = Car("Nissan", "GTR R35")   # brand = BMW, model = M3
car1.display_info()       # call method to show details

# create second object of Car class
car2 = Car("Ferrari", "SP3")  
car2.display_info()                    # call method to show details


