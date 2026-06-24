class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        if self.available:
            print("Status: Available")
        else:
            print("Status: Checked out")

    def checkout(self):
        if self.available:
            print(f"Success: '{self.title}' has been checked out.")
            self.available = False
        else:
            print(f"Error: '{self.title}' is currently checked out.")

    def checkin(self):
        if not self.available:
            print(f"Success: '{self.title}' has been successfully returned.")
            self.available = True
        else:
            print(f"Info: '{self.title}' is already in the library.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\n=== Library Books ===")
        for book in self.books:
            book.display_info()
            print("-" * 20)  

book1 = Book("Hamlet", "Shakespeare")
book2 = Book("The Silent Patient", "Alex M.")
book3 = Book("1984", "George Orwell")


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


library.display_books()


book2.checkout()
library.display_books()


book2.checkin()
library.display_books()
