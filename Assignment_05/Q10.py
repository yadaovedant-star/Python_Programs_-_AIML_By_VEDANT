# Program: String Analyzer

# Function to analyze a string
def string_analyzer(user_string):
    # Length of string
    print("Length of the string:", len(user_string))

    # First half and second half
    half_index = len(user_string) // 2
    print("First half:", user_string[:half_index])
    print("Second half:", user_string[half_index:])

    # Case-insensitive check for "python"
    if "python" in user_string.lower():
        print("The word 'python' is present in the string.")
    else:
        print("The word 'python' is NOT present in the string.")

    # Characters with positive and negative indices
    print("\nCharacters with positive and negative indices:")
    for i in range(len(user_string)):
        print("Pos index", i, ":", user_string[i],
              " | Neg index", i - len(user_string), ":", user_string[i])

    # Reverse string
    print("\nString in reverse:", user_string[::-1])


# --- Main Program ---
Taking_input_from_user = input("Enter a string: ")
string_analyzer(Taking_input_from_user)
