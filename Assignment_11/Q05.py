try:

    a = int(input("Enter the 1st number for division :"))
    b = int(input("Enter the 2nd number for division :"))
    print("The result is :",a/b)
    
except ValueError:
    print("Only Integer Number !!!!")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Program execution completed.")
    