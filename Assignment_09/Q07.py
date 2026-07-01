# Q7. Using copy() and setdefault() in a Dictionary

# Creating the dictionary
d = {"a": 1, "b": 2}

# Making a copy of the dictionary
d_copy = d.copy()   # copy() 

# Using setdefault() to add a new key "c" with value 3 (if it doesn't exist)
d.setdefault("c", 3)  

# Using setdefault() again for an existing key "a"
result = d.setdefault("a", 100)   

# Printing the original and copied dictionaries
print("Original Dictionary:", d)
print("Copied Dictionary:", d_copy)
print("Result of setdefault on existing key 'a':", result)
