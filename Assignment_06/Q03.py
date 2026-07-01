# Program: Slicing Lists

numbers = [10,20,30,40,50,60,70,80,90,100]

# Slicing format → [start:end:step]
# start = index to begin (inclusive)
# end   = index to stop (exclusive)
# step  = jump size (default = 1)

print("First 4 elements:", numbers[:4])       # indices 0–3
print("Last 3 elements:", numbers[-3:])       # last three items
print("Index 2 to 7:", numbers[2:7])          # indices 2–6
print("Every 2nd element:", numbers[::2])     # step of 2
print("Reverse list:", numbers[::-1])         # step -1 reverses
