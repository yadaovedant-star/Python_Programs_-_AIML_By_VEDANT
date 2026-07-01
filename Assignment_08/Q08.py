# Take 6 numbers as input (duplicates auto removed)
nums = set()
for i in range(6):
    n = int(input(f"Enter number {i+1}: "))
    nums.add(n)

# Add two more numbers
nums.add(99)
nums.add(100)

# Remove one number safely using discard()
nums.discard(50)  

# Final set and its length
print("Final set:", nums)
print("Length of set:", len(nums))
