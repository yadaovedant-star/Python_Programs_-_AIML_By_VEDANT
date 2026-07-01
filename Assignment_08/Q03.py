# Take 5 colors as input from user
# Take 5 colors one by one
colors = set()
colors.add(input("Enter color 1: "))
colors.add(input("Enter color 2: "))
colors.add(input("Enter color 3: "))
colors.add(input("Enter color 4: "))
colors.add(input("Enter color 5: "))
print("\nColors set:", colors)

# Ask user for a color to check
check_color = input("Enter a color to search: ")

# Membership testing
if check_color in colors:
    print(check_color, "is present in the set.")
else:
    print(check_color, "is NOT present in the set.")


# Ask user for a color to check
Find_color = input("Enter a color to search: ")

# Membership testing
if Find_color in colors:
    print(Find_color, "is present in the set.")
else:
    print(Find_color, "is NOT present in the set.")

#'in' checks If it is in set, 'not in' checks if not 
