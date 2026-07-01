# Q10. Simple Math Utility Program
# Demonstrates functions, lambda, loops, and modules

import math       # for power calculation
import random     # for random number generation

# Lambda function to calculate square
square = lambda x: x ** 2

# Normal function using math module to calculate power
def calculate_power(base, exp):
    return math.pow(base, exp)

# Main loop
while True:
    print("\n--- Simple Math Utility ---")
    print("1. The Square of given number")
    print("2. Power of The Given number")
    print("3. Generate Random Number between 1 and 100")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        num = int(input("Enter a number: "))
        print(f"Square of {num} is {square(num)}")

    elif choice == "2":
        base = int(input("Enter base: "))
        exp = int(input("Enter exponent: "))
        print(f"{base} raised to {exp} is {calculate_power(base, exp)}")

    elif choice == "3":
        print("Random number between 1 and 100:", random.randint(1, 100))

    elif choice == "4":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
