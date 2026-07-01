# Q2. Using __init__ Constructor

class Book:   # define a class named Book
    def __init__(self, title, author, price):   # constructor to initialize attributes
        self.title = title   
        self.author = author 
        self.price = price    

    def show_details(self):   # method
        print("Title:", self.title)    
        print("Author:", self.author)  
        print("Price:", self.price)    
       

# create first book object
book1 = Book("Cant Hurt Me", "David Goggins", 250)   # title, author, price
book1.show_details()   # call method to show details

# create second book object
book2 = Book("The psychology of money", "Morgan Housel", 180)   # title, author, price
book2.show_details()   # call method to show details


