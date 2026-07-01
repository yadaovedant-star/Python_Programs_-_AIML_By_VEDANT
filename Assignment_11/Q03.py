try:
    num_str = input("Enter an Number to convert it :")
    print("The Number Before converting :",(type(num_str)))
    
    num = int(num_str)
     
    print("The Number After converting :",(type(num)))

    
    a = int(input("Enter the 1st number for division :"))
    b = int(input("Enter the 2nd number for division :"))
   
    print("The converted number :",num)
    print("The Result is :",a/b)

except ValueError:
    print("Only Integer Number !!!!")

except ZeroDivisionError:
    print("Division by zero is not allowed.") 
    
    