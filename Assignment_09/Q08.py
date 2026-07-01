# Q8. Using fromkeys() and Membership in a Dictionary

# Creating a dictionary with keys and default value None
d = dict.fromkeys(["name", "age", "city"], None)
# fromkeys() → creates a dictionary with given keys and assigns the same default value to all

print("Initial Dictionary:", d)

# Taking user input to fill these keys
d["name"] = input("Enter name: ")
d["age"] = input("Enter age: ")
d["city"] = input("Enter city: ")

print("\nUpdated Dictionary:", d)

# Checking if a given key exists using 'in' operator
key_to_check = input("\nEnter a key to check: ")
if key_to_check in d:
    print(f"Key '{key_to_check}' exists with value:", d[key_to_check])
else:
    print(f"Key '{key_to_check}' does not exist in dictionary.")
