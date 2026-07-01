try:
    age_str = input("Enter your Age: ")
    age = int(age_str)

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("The converted age number is:", age)

except ValueError:
    
    print("Invalid age input! Please enter a positive integer.")

finally:
    print("Program executed successfully.")
    

 