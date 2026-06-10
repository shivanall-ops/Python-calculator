class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False
        self.issued_to = None

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        issued_info = f" (Issued to: {self.issued_to})" if self.is_issued else ""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}{issued_info}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                print("Book with this ISBN already exists!")
                return False
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")
        return True

    def search_book(self, query):
        results = []
        query = query.lower()
        for book in self.books:
            if (query in book.title.lower() or 
                query in book.author.lower() or 
                query in book.isbn.lower()):
                results.append(book)
        return results

    def view_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- All Books ---")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")

    def issue_book(self, isbn, borrower_name):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_issued:
                    print(f"Book '{book.title}' is already issued to {book.issued_to}.")
                    return False
                book.is_issued = True
                book.issued_to = borrower_name
                print(f"Book '{book.title}' issued to {borrower_name} successfully!")
                return True
        print("Book with this ISBN not found!")
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_issued:
                    print(f"Book '{book.title}' is not currently issued.")
                    return False
                borrower = book.issued_to
                book.is_issued = False
                book.issued_to = None
                print(f"Book '{book.title}' returned by {borrower} successfully!")
                return True
        print("Book with this ISBN not found!")
        return False


def display_menu():
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. Search Book")
    print("3. View All Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
    print("=" * 35)


def main():
    library = Library()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print("\n--- Add Book ---")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        
        elif choice == "2":
            print("\n--- Search Book ---")
            query = input("Enter title, author, or ISBN to search: ")
            results = library.search_book(query)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for i, book in enumerate(results, 1):
                    print(f"{i}. {book}")
            else:
                print("No books found matching your search.")
        
        elif choice == "3":
            library.view_all_books()
        
        elif choice == "4":
            print("\n--- Issue Book ---")
            isbn = input("Enter ISBN of the book to issue: ")
            borrower_name = input("Enter borrower name: ")
            library.issue_book(isbn, borrower_name)
        
        elif choice == "5":
            print("\n--- Return Book ---")
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        
        elif choice == "6":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
