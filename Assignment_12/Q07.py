# Q7. Lambda + range() + Lists + Exception Handling
# Program: Squares using lambda, range, lists, and exception handling

def main():
    try:
        # Step 1: Lambda function for square
        square = lambda x: x ** 2

        # Step 2: Generate numbers from 1 to 20 using range()
        numbers = range(1, 21)
        print("Numbers from 1 to 20:", list(numbers))

        # Step 3: Store squares in a list using lambda
        squares = [square(num) for num in numbers]
        print("Squares List:", squares)

        # Step 4: Print only even squares
        even_squares = [sq for sq in squares if sq % 2 == 0]
        print("Even Squares:", even_squares)

    except Exception as e:
        print("An unexpected error occurred:", e)


# Call the function
main()
