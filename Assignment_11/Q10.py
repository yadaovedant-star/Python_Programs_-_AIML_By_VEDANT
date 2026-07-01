while True:
    # Display menu
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        # Take user choice
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting program. Goodbye!")
            break

        # Take two numbers
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        # Perform operation
        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            print("Result:", a / b)   # may raise ZeroDivisionError
        else:
            print("Invalid choice! Please select between 1-5.")

    except ValueError:
        # Handles invalid input (non-integer)
        print("Error: Please enter valid integers only!")

    except ZeroDivisionError:
        # Handles division by zero
        print("Error: Division by zero is not allowed.")

    finally:
        # Always runs after each attempt
        print("Operation attempted.")
