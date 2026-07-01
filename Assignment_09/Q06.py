# Q6. Using popitem() and clear() in a Dictionary
# Creating a dictionary with 5 key-value pairs
info = {
    "brand": "Hauwei",
    "model": "Pura 80 ultra",
    "price": 320000,
    "color": "Silver",
    "warranty": "3 Year"
}

# Using popitem() twice → removes the last inserted key-value pair each time
removed1 = info.popitem()
print("First popitem removed:", removed1)

removed2 = info.popitem()
print("Second popitem removed:", removed2)

# Clearing the entire dictionary
info.clear()

# Printing the final result
print("Final Dictionary after clear():", info)


