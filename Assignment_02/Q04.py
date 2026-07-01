# Q4. Using for loop with range()

# a) Print all numbers from 1 to 30
print("Numbers from 1 to 30:")
for i in range(1, 31):   # range(start, stop) → generates numbers from start up to stop-1
    print(i, end=" ")    # end=" " prints numbers in one line separated by space
print("\n")              # newline after loop

# b) Print all odd numbers from 1 to 50
print("Odd numbers from 1 to 50:")
for i in range(1, 51, 2):   # range(start, stop, step) → step=2 skips even numbers
    print(i, end=" ")
print("\n")

# c) Print the sum of numbers from 1 to 15
sum_numbers = 0
for i in range(1, 16):   # generates numbers 1 to 15
    sum_numbers += i     # add each number to sum
print("Sum of numbers from 1 to 15:", sum_numbers)
