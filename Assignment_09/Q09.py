# Q9. Practical Application - Contact Management using Dictionary
# Creating an empty dictionary to store contacts
contacts = {}

# Taking user input for one contact
name = input("Enter An contact name: ")
phone = input("Enter The phone number: ")
email = input("Enter An email: ")

# Storing contact info with name as key
contacts[name] = {"phone": phone, "email": email}

# Searching a contact by name using get()
search_name = input("\nEnter name to search: ")
result = contacts.get(search_name)

if result:
    print("Contact found:", result)
else:
    print("Contact not found.")

# Printing all contacts using items()
print("\nAll Contacts:")
for contact_name, details in contacts.items():
    print(contact_name, ":", details)

