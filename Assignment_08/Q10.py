items = set()
while True:
    print("\n--- Menu ---")
    print("1. Add item")
    print("2. Remove item (discard)")
    print("3. Show all unique items")
    print("4. Check if an item exists")
    print("5. Clear all items")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        item = input("Enter item to add: ")
        items.add(item)   # add item
        print("The Item added.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        items.discard(item)   # safe remove
        print("The Item removed (if present).")

    elif choice == "3":
        print(" for Unique items:", items)
    
    elif choice == "4":
        item = input("Enter item to check if its in the set: ")
        if item in items:
            print(item, "The element exists in the set.")
        else:
            print(item, "This item does NOT exist.")
    
    elif choice == "5":
        items.clear()   # clear all
        print("All items cleared.")
    elif choice == "6":
        print("Exiting program...")   
    else:
        print("Invalid choice.")
        break                                  
    
    