# Define the Book class
class Book:
    # __init__ is a dunder method used to initialize the class when an instance is created.
    def __init__(self, title: str, pages: int):
        self.title = title  # Set the title of the book
        self.pages = pages  # Set the number of pages of the book

    # __len__ is a dunder method that allows us to use the len() function on Book objects.
    def __len__(self) -> int:
        return self.pages  # Return the number of pages when len() is called

    # __add__ is a dunder method that defines the behavior of the "+" operator for Book objects.
    def __add__(self, other: 'Book') -> 'Book':
        # Combine titles of both books
        combined_title = f"{self.title} & {other.title}"
        # Sum the pages of both books
        combined_pages = self.pages + other.pages
        # Return a new Book object with the combined title and pages
        return Book(combined_title, combined_pages)

# Code to test the Book class functionality
if __name__ == "__main__":
    # Create two Book instances
    book1 = Book("Pi Daily", 100)
    book2 = Book("Harry Potter", 340)

    # Use the __len__ dunder method via the len() function
    print(f"Length of '{book1.title}': {len(book1)} pages")  # Output: 100
    print(f"Length of '{book2.title}': {len(book2)} pages")  # Output: 340

    # Use the __add__ dunder method via the "+" operator
    combined_book = book1 + book2
    print(f"Combined Book Title: {combined_book.title}")  # Output: Pi Daily & Harry Potter
    print(f"Combined Book Pages: {combined_book.pages}")  # Output: 440
