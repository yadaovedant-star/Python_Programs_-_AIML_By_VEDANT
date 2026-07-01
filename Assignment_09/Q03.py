# Q3. Demonstrating get(), keys(), values(), items()

# Creating the dictionary
person = {"name": "Priya", "age": 21, "profession": "Engineer"}

# a) Using get() to access "age" and a non-existing key "salary"
print("Age:", person.get("age"))                    
print("Salary:", person.get("salary", "Not Found"))  

# b) Print all keys using keys()
print("\nKeys:", person.keys())   

# c) Print all values using values()
print("Values:", person.values()) 

# d) Print all key-value pairs using items()
print("Items:", person.items())   
