# Function : Created As analyse string
def analyze_string(s):
    # Handle empty string case
    if s == "":
        print("Empty string provided. Nothing to analyze.")
        return
    # 1. Print length using len()
    print("Length of the string:", len(s))
    
    # 2. Print string in reverse using slicing
    print("Reversed string:", s[::-1])
    
    # 3. Count vowels (case-insensitive)
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
    
    # 4. Print each character with positive and negative index
    print("\nCharacters with indices:")
    for i in range(len(s)):
        print("Positive index", i, ":", s[i], 
              "| Negative index", i - len(s), ":", s[i])

# --- Main Program ---
user_input = input("Enter a string: ")
analyze_string(user_input)


