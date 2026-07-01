
fruits = ["apple", "banana", "mango", "orange", "grape"]

print("First item:", fruits[0])        # index 0 → first element
print("Third item:", fruits[2])        # index 2 → third element
print("Last item (negative index):", fruits[-1])      # -1 → last element
print("Second last item (negative index):", fruits[-2])  # -2 → second last element

index = int(input("Enter an index (0 to 4): "))
print("Fruit at index", index, "is:", fruits[index])