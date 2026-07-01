import numpy as np

try:
    # Ask user how many numbers to generate
    n = int(input("Enter how many numbers you want to generate please type below : "))

    if n <= 0:
        raise ValueError("Type a positive integer greater than 0.")

    # Generate random integers between 10 and 100
    U1 = np.random.randint(10, 101, n)

    # Print the array
    print("\n The Generated Array U1 is :\n", U1)

    # Statistics
    U2 = np.mean(U1)       # Mean
    U3 = np.median(U1)     # Median
    U4 = np.std(U1)        # Standard Deviation
    U5 = np.min(U1)        # Minimum
    U6 = np.max(U1)        # Maximum

    print("\n The Statistics for Array U1 are :")
    print("Mean:", U2)
    print("Median:", U3)
    print("Standard Deviation:", U4)
    print("Minimum:", U5)
    print("Maximum:", U6)

    # Reshape into 2D array if possible
    if n % 2 == 0:  # only reshape if divisible
        rows = 2 # For 2d array
        cols = n // 2 #floor division if true 
        U7 = U1.reshape(rows, cols)
        print("\nReshaped Array U7 (2D):\n", U7)

        # Row-wise sum
        U8 = U7.sum(axis=1)
        print("Row-wise Sum U8:", U8)
    else:
        print("\nReshape not possible (number of elements not divisible).")

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("Unexpected Error:", e)
