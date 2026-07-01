# Q9. Strings + Sets + Exception Handling + Modules
# Program: Unique words from sentence using set, sorted, and math module

import math

def main():
    try:
        # Step 1: Input a sentence
        sentence = input("Enter a sentence: ")

        # Step 2: Split into words and store unique ones in a set
        words = set(sentence.split())

        # Step 3: Print unique words in sorted order
        sorted_words = sorted(words)
        print("\nUnique Words (Sorted):", sorted_words)

        # Step 4: Use math module to raise count of unique words to power 2
        count = len(words)
        result = math.pow(count, 2)
        print(f"Total Unique Words: {count}")
        print(f"Unique Words Count ^ 2 = {result}")

    except Exception as e:
        print("An unexpected error occurred:", e)


# Call the function
main()
