# Q1. Creating Dictionaries in Python
# a) Creating an empty dictionary in two ways
dict1 = {}    # {}
dict2 = dict()      # dict() constructor

print("Empty Dictionary 1:", dict1, "\nType:", type(dict1))
print("Empty Dictionary 2:", dict2, "\nType:", type(dict2))

# b) Dictionary with string keys
student_info = {
    "name": "HomeLander",   # key is a string, value is also a string
    "city": "USA",
    "course": "Soldier"
}
print("\nDictionary with string keys:", student_info, "\nType:", type(student_info))

# c) Dictionary with integer keys
marks = {
    1 : "Math",   #Key As integer
    2 : "Physics",
    3 : "Chemistry"
}
print("\nDictionary with integer keys:", marks, "\nType:", type(marks))

# d) Mixed data type dictionary
mixed_dictionary = {
    "name": "Annirudh",   
    "age": 22,         
   "Height" : 178.5     
}
print("\nAll Mixed data type dictionary:", mixed_dictionary, "\nType:", type(mixed_dictionary))
