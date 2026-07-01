# Tuple Packing: creating a tuple without parentheses
info_tuple = "Vedant", 18, "karanja"   # name, age, city
print("Packed Tuple:", info_tuple)
print("Type:", type(info_tuple))
print("--------------------------\n--------------------------")
# Tuple Unpacking: assigning tuple elements to variables
name, age, city = info_tuple
print("\nUnpacked Values:")
print("Name:", name)
print("Age:", age)
print("City:", city)
