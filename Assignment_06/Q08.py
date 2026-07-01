# Program: sort() and reverse()

marks = [45, 78, 65, 90, 34, 82, 71]

# Sort ascending
marks.sort()
print("Ascending order:", marks)

# Sort descending
marks.sort(reverse=True)
print("Descending order:", marks)

# Reverse original list (without sorting)
marks = [45, 78, 65, 90, 34, 82, 71]  # reset to original
marks.reverse()
print("Original list reversed:", marks)


