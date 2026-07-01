Taking_MainString_Input_From_User = input("Enter a string or character: ") 
Taking_SubString_Input_From_User = input("Enter a substring to search in the main string: ")
#inputs in this are case-sensitive, so "Hello" and "hello" are different strings

#If else conditions used 
if Taking_SubString_Input_From_User in Taking_MainString_Input_From_User:
    print("The substring is present in the main string.")  
    print("Substring Found !!")
else:
    print("The substring is not present in the main string.")
    print("Substring Not Found !!")