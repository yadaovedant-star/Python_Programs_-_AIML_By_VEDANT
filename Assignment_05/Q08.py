# Program: Membership with range()
Taking_input_from_user = int(input("Enter a number: "))

# Check if number is in range(1, 51)
if Taking_input_from_user in range(1, 51):
    print(Taking_input_from_user, "is present in range(1, 51)")
else:
    print(Taking_input_from_user, "is NOT present in range(1, 51)")

# Check if number is in range(10, 100, 5)
if Taking_input_from_user in range(10, 100, 5):
    print(Taking_input_from_user, "is present in range(10, 100, 5)")
else:
    print(Taking_input_from_user, "is NOT present in range(10, 100, 5)")
