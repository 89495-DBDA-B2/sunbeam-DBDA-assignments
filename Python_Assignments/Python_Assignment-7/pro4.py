class Book:
    def __init__(self, book_id, title, author):
        # Initializer to set the attributes for the Book
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        # Return a string representation of the book
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}"


class Library:
    def __init__(self):
        # Initialize an empty list to hold books
        self.books = []

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)
        print(f"Book '{book.title}' by {book.author} added to the library.")

    def display_books(self):
        # Display all books in the library
        if self.books:
            print("\nBooks in Library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

# Function to interact with the library system
def library_system():
    # Create a Library object
    library = Library()

    while True:
        # Display options to the user
        print("\nLibrary System Menu:")
        print("1. Add a Book")
        print("2. Display all Books")
        print("3. Exit")
        
        # Get the user choice
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Add a book
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            
            # Create a new Book object and add it to the library
            book = Book(book_id, title, author)
            library.add_book(book)
        
        elif choice == '2':
            # Display all books in the library
            library.display_books()

        elif choice == '3':
            # Exit the system
            print("Exiting the library system.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the library system
library_system()
