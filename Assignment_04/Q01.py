#using the lamda function to calculate the square of a number
square=lambda x:x**2
x=int(input("Enter a number: ")) #Auto returned the value and output the square of the number 
print("The square of the number is: ",square(x))

#using def function to calculate the square of a number
def square(x):
    return x**2 #Requires a return statement to return the value of the square of the number
x=int(input("Enter a number: "))
print("The square of the number is: ",square(x)) 