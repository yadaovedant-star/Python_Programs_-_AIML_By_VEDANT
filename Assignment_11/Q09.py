try:   # Added missing colon after 'try'
    # Convert input to integer
    num = int(input("Enter a number: "))   # Indented properly under try
    
    # Perform division
    result = 100 / num
    print("Result:", result)

except ValueError:   # Added missing colon after 'except ValueError'
    # Handles invalid input (non-integer)
    print("Please enter a valid number")   # Indented properly under except

except Exception:   # Changed bare 'except:' to 'except Exception' (best practice)
    # Handles any other unexpected error (like division by zero)
    print("Some error occurred")   # Indented properly under except
