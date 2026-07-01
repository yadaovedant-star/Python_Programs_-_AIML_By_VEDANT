class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

l = float(input("Enter length: "))
w = float(input("Enter width: "))

rect1 = Rectangle(l, w)
rect1.display()


