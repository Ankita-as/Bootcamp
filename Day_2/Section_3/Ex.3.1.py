# 1. Define a Class
class Book:
    # Class Variable
    category = "Fiction"

    # Constructor with default values
    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    # Method to describe the book
    def describe(self):
        return f"'{self.title}' by {self.author}"

    # Method to update title
    def update_title(self, new_title):
        self.title = new_title


# 2. Create an Object
book1 = Book("1984", "Orwell")
print("\n[2] Book Attributes:")
print("Title:", book1.title)
print("Author:", book1.author)

# 3. Use describe() method
print("\n[3] Describe Method:")
print(book1.describe())

# 4. Class vs Instance Variable
print("\n[4] Category (Class Variable):", book1.category)

# 5. Update Object State
book1.update_title("Animal Farm")
print("\n[5] Updated Title:", book1.title)

# 6. __init__ Logic with Default Values
default_book = Book()
print("\n[6] Default Constructor:")
print(default_book.describe())

# 7. Dynamic Attribute
book1.year = 1945
print("\n[7] Dynamic Attribute (year):", book1.year)

# 8. Check Type
print("\n[8] Type Check:")
print("Is book1 a Book?", isinstance(book1, Book))
