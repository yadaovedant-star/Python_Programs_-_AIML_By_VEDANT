# Q10. Mini Project - Smart Calculator & Data Manager
# Combines: Functions, OOP, Dictionaries, Sets, Modules, Exception Handling

import math
import random
import time

def basic_arithmetic():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b != 0:
                return a / b
            else:
                print("Error: Division by zero!")
                return None
        else:
            print("Invalid operation!")
            return None
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None


def scientific_calculations():
    try:
        num = float(input("Enter a number: "))
        print("Choose scientific operation:")
        print("1. Square Root")
        print("2. Power (num^2)")
        print("3. Factorial (integer only)")

        choice = input("Enter choice (1-3): ")
        if choice == "1":
            return math.sqrt(num)
        elif choice == "2":
            return math.pow(num, 2)
        elif choice == "3":
            if num.is_integer() and num >= 0:
                return math.factorial(int(num))
            else:
                print("Factorial only works for non-negative integers!")
                return None
        else:
            print("Invalid choice!")
            return None
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None


def generate_random():
    try:
        start = int(input("Enter start range: "))
        end = int(input("Enter end range: "))
        count = int(input("How many random numbers to generate? "))
        return random.sample(range(start, end+1), count)
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return None
    except Exception as e:
        print("Error:", e)
        return None


def smart_calculator():
    history = {}  # dictionary with timestamp as key, result as value

    while True:
        print("\n--- Smart Calculator & Data Manager ---")
        print("1. Basic Arithmetic")
        print("2. Scientific Calculations")
        print("3. Generate Random Numbers")
        print("4. View History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        result = None

        if choice == "1":
            result = basic_arithmetic()
        elif choice == "2":
            result = scientific_calculations()
        elif choice == "3":
            result = generate_random()
        elif choice == "4":
            print("\n--- History ---")
            if history:
                for ts, res in history.items():
                    print(f"{ts} -> {res}")
            else:
                print("No history available.")
        elif choice == "5":
            print("Exiting Smart Calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter between 1-5.")

        # Store result in history with timestamp
        if result is not None:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            history[timestamp] = result
            print("Result:", result)
    
           

# Run the program
smart_calculator()
