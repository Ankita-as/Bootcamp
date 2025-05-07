# Book class with __str__, __repr__, __eq__, __hash__, __lt__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __lt__(self, other):
        return self.title < other.title

# Library class with __len__ and __getitem__
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

# Callable class
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return f"Hello, {self.name}!"

# Boolean check class
class Container:
    def __init__(self, items=None):
        self.items = items or []

    def __bool__(self):
        return bool(self.items)

# Testing all features
if __name__ == "__main__":
    book1 = Book("1984", "Orwell")
    book2 = Book("1984", "Orwell")
    book3 = Book("Brave New World", "Huxley")

    print(str(book1))
    print(repr(book1))

    print("book1 == book2:", book1 == book2)

    book_set = {book1, book2, book3}
    print("Books in set:", book_set)

    sorted_books = sorted(book_set)
    print("Sorted books:", sorted_books)

    library = Library()
    library.add_book(book1)
    library.add_book(book3)

    print("Library size:", len(library))
    print("First book in library:", library[0])

    greeter = Greeter("Ankita")
    print(greeter())  # Using object as a function

    container1 = Container()
    container2 = Container(["item"])

    print("Empty container is True?", bool(container1))
    print("Non-empty container is True?", bool(container2))
