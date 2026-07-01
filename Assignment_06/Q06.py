# Program: remove(), pop(), and clear()

items = [10, 20, 30, 20, 40, 50]

# remove() deletes by value (first match)
items.remove(20)
print("After remove(20):", items)

# pop() deletes by index and returns the value
removed = items.pop(3)
print("Removed at index 3:", removed)
print("After pop(3):", items)

# pop() with no index deletes last item
items.pop()
print("After pop():", items)

# clear() empties the list
items.clear()
print("After clear():", items)
