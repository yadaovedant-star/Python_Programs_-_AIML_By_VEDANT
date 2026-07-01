# a) Print numbers from 0 to 10
# range(stop) → generates numbers from 0 up to stop-1
print("Numbers from 0 to 10:")
for i in range(11):   # stop = 11 → prints 0 to 10
    print(i, end=" ")
print("\n")

# b) Print numbers from 5 to 15
# range(start, stop) → generates numbers from start up to stop-1
print("Numbers from 5 to 15:")
for i in range(5, 16):   # start=5, stop=16 → prints 5 to 15
    print(i, end=" ")
print("\n")

# c) Print odd numbers from 1 to 21
# range(start, stop, step) → step controls increment
print("Odd numbers from 1 to 21:")
for i in range(1, 22, 2):   # start=1, stop=22, step=2 → skips even numbers
    print(i, end=" ")
print("\n")
