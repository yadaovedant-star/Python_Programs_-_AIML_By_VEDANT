# Q2. Accessing and Modifying Elements in a Dictionary
# Creating the dictionary
student = {
    "name": "Vedant",   
    "age": 20,         
    "city": "Karanja",    
    "marks": 00      
}
# Accessing the value of "name" using square brackets
print("Name:", student["name"])   # prints the value stored at key "name"

# Updating the "marks" to 92
student["marks"] = 92             # modifies the value of existing key "marks"

# Adding a new key "grade" with value "A"
student["grade"] = "A"            # adds a new key-value pair to dictionary


# Printing the updated dictionary
print("\nUpdated Dictionary:", student)


