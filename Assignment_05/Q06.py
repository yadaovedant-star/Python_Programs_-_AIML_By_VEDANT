# a) Numbers from 20 down to 10 (decreasing)
# range(start, stop, step) → step = -1 means count backwards
print("Numbers from 20 down to 10:")
for i in range(20, 9, -1):   # start=20, stop=9, step=-1
    print(i, end="  ")
print("\n")

# b) Numbers from 15 down to 1 in steps of 2
# step = -2 Skips every 2nd number while counting backwards
print("Numbers from 15 down to 1 in steps of 2:")
for i in range(15, 0, -2):   # start=15, stop=0, step=-2
    print(i, end="  ")
print("\n")
