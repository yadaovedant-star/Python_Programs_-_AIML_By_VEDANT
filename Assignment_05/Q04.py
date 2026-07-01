Taking_string_input_from_user = input("Enter a string or character: ")
print("The length of the string is: ", len(Taking_string_input_from_user)) # len() function is used to find the length of the string
print("The last Character in the string without using indexing is: ", Taking_string_input_from_user[len(Taking_string_input_from_user)-1]) 

if len(Taking_string_input_from_user) % 2 != 0:  # odd length check
    middle_index = len(Taking_string_input_from_user) // 2  # integer division gives middle position
    print("Middle character:", Taking_string_input_from_user[middle_index])
else:
    print("No single middle character (string length is even).")

    