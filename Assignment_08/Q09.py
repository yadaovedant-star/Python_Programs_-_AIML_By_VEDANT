# Original list with duplicates
scores = [85, 92, 78, 92, 85, 88, 95, 78]
print("Original scores:", scores)

# Convert list to set → removes duplicates
unique_scores = set(scores)
print("Unique scores (set):", unique_scores)

# Convert back to sorted list
sorted_scores = sorted(unique_scores)
print("Sorted unique scores (list):", sorted_scores)

# Total number of unique scores
print("Total unique scores:", len(unique_scores))
