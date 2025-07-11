import json
import os
from typing import List, Dict, Optional

LIBRARY_FILE = "my_library.json"

class Book:
    def __init__(self, title: str, author: str, year: int, isbn: str, tags: List[str]):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.tags = tags

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
            "tags": self.tags
        }

    @staticmethod
    def from_dict(data: Dict):
        return Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            isbn=data["isbn"],
            tags=data["tags"]
        )

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def load(self):
        if os.path.exists(LIBRARY_FILE):
            with open(LIBRARY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]
        else:
            self.books = []

    def save(self):
        with open(LIBRARY_FILE, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=2)

    def add_book(self, book: Book):
        self.books.append(book)
        self.save()

    def list_books(self):
        if not self.books:
            print("Your library is empty.")
            return
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book.title} by {book.author} ({book.year}) [ISBN: {book.isbn}] Tags: {', '.join(book.tags)}")

    def search_books(self, keyword: str) -> List[Book]:
        keyword = keyword.lower()
        return [
            book for book in self.books
            if keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword in book.isbn.lower()
            or any(keyword in tag.lower() for tag in book.tags)
        ]

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def update_book(self, isbn: str, **kwargs):
        book = self.find_by_isbn(isbn)
        if not book:
            print("Book not found.")
            return False
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        self.save()
        print("Book updated.")
        return True

    def delete_book(self, isbn: str):
        book = self.find_by_isbn(isbn)
        if book:
            self.books.remove(book)
            self.save()
            print("Book deleted.")
        else:
            print("Book not found.")

def prompt_for_book() -> Book:
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    while True:
        try:
            year = int(input("Year: ").strip())
            break
        except ValueError:
            print("Please enter a valid year.")
    isbn = input("ISBN: ").strip()
    tags = input("Tags (comma separated): ").strip().split(",")
    tags = [tag.strip() for tag in tags if tag.strip()]
    return Book(title, author, year, isbn, tags)

def main_menu():
    print("\n=== Personal Library Manager ===")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Search books")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Exit")

def main():
    library = Library()
    library.load()

    while True:
        main_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print("\nEnter book details:")
            book = prompt_for_book()
            if library.find_by_isbn(book.isbn):
                print("A book with this ISBN already exists.")
            else:
                library.add_book(book)
                print("Book added.")
        elif choice == "2":
            print("\nYour Books:")
            library.list_books()
        elif choice == "3":
            keyword = input("Enter search keyword: ").strip()
            results = library.search_books(keyword)
            if results:
                print(f"\nFound {len(results)} books:")
                for idx, book in enumerate(results, 1):
                    print(f"{idx}. {book.title} by {book.author} ({book.year}) [ISBN: {book.isbn}] Tags: {', '.join(book.tags)}")
            else:
                print("No books found.")
        elif choice == "4":
            isbn = input("Enter ISBN of the book to update: ").strip()
            book = library.find_by_isbn(isbn)
            if not book:
                print("Book not found.")
                continue
            print("Leave fields blank to keep current value.")
            new_title = input(f"New title [{book.title}]: ").strip() or book.title
            new_author = input(f"New author [{book.author}]: ").strip() or book.author
            new_year_input = input(f"New year [{book.year}]: ").strip()
            new_year = int(new_year_input) if new_year_input else book.year
            new_tags_input = input(f"New tags (comma separated) [{', '.join(book.tags)}]: ").strip()
            new_tags = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()] if new_tags_input else book.tags
            library.update_book(isbn, title=new_title, author=new_author, year=new_year, tags=new_tags)
        elif choice == "5":
            isbn = input("Enter ISBN of the book to delete: ").strip()
            library.delete_book(isbn)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
