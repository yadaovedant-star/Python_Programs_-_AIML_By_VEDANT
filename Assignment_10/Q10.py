class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"

    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")

    def show_info(self):
        print("Title:", self.title, "| Author:", self.author, "| Status:", self.status)

library = []

while True:
    print("\n1. Add Book  2. Issue Book  3. Return Book  4. Show All Books  5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        library.append(Book(title, author))
        print("Book added successfully.")

    elif choice == "2":
        title = input("Enter book title to issue: ")
        found = False
        for book in library:
            if book.title == title:
                book.issue_book()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "3":
        title = input("Enter book title to return: ")
        found = False
        for book in library:
            if book.title == title:
                book.return_book()
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "4":
        if not library:
            print("No books in library.")
        else:
            for book in library:
                book.show_info()

    elif choice == "5":
        print("Exiting Library System.")
        break

    else:
        print("Invalid choice. Try again.")
