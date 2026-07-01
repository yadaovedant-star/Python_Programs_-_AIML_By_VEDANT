# Q8. Program to print Fizz, Buzz, or FizzBuzz using for loop

# Loop through numbers from 1 to 40
for i in range(1, 41):   # range(1, 41) generates numbers 1 to 40
    
    # Check divisibility conditions
    if i % 3 == 0 and i % 5 == 0:   # divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:   # divisible only by 3
        print("Fizz")
    elif i % 5 == 0:   # divisible only by 5
        print("Buzz")
    else:
        print(i)   # if not divisible by 3 or 5, print the number itself
