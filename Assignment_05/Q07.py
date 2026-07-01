
# Take string input from the user
Taking_input_from_user = input("Enter a string or character: ")

# Print each character with its index
print("Characters with their index:")
for i in range(len(Taking_input_from_user)):   # range(0, len(Taking_input_from_user)) → goes from 0 to last index
    print("Index", i, ":", Taking_input_from_user[i])#Index (i) :_____

# Print string in reverse order using negative step
print("\nString in reverse order:")
for i in range(len(Taking_input_from_user)-1, -1, -1):   # start=last index, stop=-1, step=-1
    print(Taking_input_from_user[i], end="")

