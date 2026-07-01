# Q6. Sets + Tuples + Modules
# Program: Unique numbers in set, convert to tuple, use random & math modules

import random
import math

def main():
    try:
        # Step 1: Input 10 numbers and store unique values in a set
        numbers = set()
        for i in range(10):
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.add(num)   # duplicates automatically removed
            except ValueError:
                print("Invalid input! Please enter numeric values only.")
        
        print("\nUnique Numbers (Set):", numbers)

        # Step 2: Convert set to tuple
        num_tuple = tuple(numbers)
        print("Tuple:", num_tuple)

        # Step 3: Pick 3 random numbers from tuple
        if len(num_tuple) >= 3:
            random_nums = random.sample(num_tuple, 3)
            print("3 Random Numbers from Tuple:", random_nums)
        else:
            print("Not enough unique numbers to pick 3!")

        # Step 4: Square root of sum of tuple elements
        total = sum(num_tuple)
        print("Sum of Tuple Elements:", total)
        print("Square Root of Sum:", math.sqrt(total))

    except Exception as e:
        print("An unexpected error occurred:", e)


# Call the function
main()
