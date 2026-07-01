while True:
    print("\n--- Simple Calculator Menu ---")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        print("Exiting calculator... Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", num1 + num2)
    elif choice == 2:
        print("Result:", num1 - num2)
    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
