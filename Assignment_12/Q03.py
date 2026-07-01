# Q3. Lists + Functions + Exception Handling
# Program: Manage subject marks using list, function, and exception handling

def manage_marks():
    marks = []  # empty list to store marks
    
    # Input 5 subject marks with error handling
    for i in range(5):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i+1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Please enter numeric marks only.")
    
    # Display entered marks
    print("\nMarks List:", marks)
    
    # Calculate average, highest, lowest
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    
    # Sort in descending order
    marks.sort(reverse=True)
    print("Marks in Descending Order:", marks)


# Call the function
manage_marks()
