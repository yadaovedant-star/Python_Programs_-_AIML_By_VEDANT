# Tuple of fruits
fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

# a) First index of 'banana'
print("First index of 'banana':", fruits.index('banana'))

# b) First index of 'banana' starting search from index 2
print("First index of 'banana' from index 2:", fruits.index('banana', 2))

# c) Safely find the index of 'kiwi' using try-except
try:
    print("Index of 'kiwi':", fruits.index('kiwi'))
except ValueError:
    print("Index of 'kiwi': Not found")
