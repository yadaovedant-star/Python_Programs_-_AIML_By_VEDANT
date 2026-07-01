# Create sets
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# Make a copy of set1
the_copy_set = set1.copy()
print("Copy of set1:", the_copy_set)

# Update set1 with elements from set2
set1.update(set2)
print("Updated set1:", set1)
