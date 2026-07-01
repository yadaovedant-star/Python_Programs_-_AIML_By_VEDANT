# Create set
fruits = {'apple', 'banana', 'mango'}
print("Initial set is:", fruits)

# a) Add 'orange'
fruits.add('orange')
print("After adding the element:", fruits)

# b) Add 'banana' again (no change, duplicates ignored)
fruits.add('banana')
print("After adding duplicate:", fruits)

# c) Remove 'mango'
fruits.remove('mango')
print("After removing the element :", fruits)

# d) Discard 'grape' (no error if not present)
fruits.discard('grape')
print("After discarding the element:", fruits)
