# Q5. Using update() and pop() in a Dictionary

# Creating the dictionary
info = {"brand": "Samsung", "model": "A52", "price": 25000}

# Updating with new information
info.update({"color": "Black", "price": 24000})
# update() → adds new key-value pairs or modifies existing ones

# Removing the key "model" using pop()
removed_value = info.pop("model")
# pop() → removes the specified key and returns its value

print("Removed Value (model):", removed_value)

# Printing the final dictionary
print("Final Dictionary:", info)



