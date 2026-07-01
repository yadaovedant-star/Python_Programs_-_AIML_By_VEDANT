# Program: extend() vs append()

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# a) Using extend() → adds elements of list2 individually
list1.extend(list2)
print("After extend:", list1)

# b) Using append() → adds list2 as a single element
list1_copy = [1, 2, 3]   # copy of original list1
list1_copy.append(list2)
print("After append:", list1_copy)
