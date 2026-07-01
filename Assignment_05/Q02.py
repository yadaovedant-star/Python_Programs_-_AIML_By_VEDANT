String_Input_From_User = input("Enter a string or character: ")
print("The first 5 characters are: ", String_Input_From_User[0:5]) # 0,1,2,3,4
print("The last 4 characters are: ", String_Input_From_User[-4:]) # -4, -3, -2, -1
print("The string in reverse order is as follows: ", String_Input_From_User[::-1]) # reverse order
print("The every 2nd character in the string is: ", String_Input_From_User[::2]) # every 2nd character
# Slicing Syntax: [start:end:step]
# start → index where slicing begins 
# end   → index where slicing stops 
# step  → jump size or skip size for slicing 