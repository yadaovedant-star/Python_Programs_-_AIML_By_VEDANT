# Q9. Demonstrating __name__ == "__main__"

def greet():
    print("Hello! This is a greeting function.")

# This block runs only if the file is executed directly
if __name__ == "__main__":
    print("File is being run directly this is the main file.")
    greet()

