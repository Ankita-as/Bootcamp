from typing import Dict
import json

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author}"

    # 1. Static Method: Validate ISBN
    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        return isbn.isdigit() and len(isbn) in [10, 13]

    # 2 & 3. Class Method: Alternative Constructor
    @classmethod
    def from_string(cls, s: str):
        title, author = s.split('|')
        return cls(title.strip(), author.strip())

    # 5. Alternative constructor from JSON
    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(data['title'], data['author'])

    # 5. Alternative constructor from dict
    @classmethod
    def from_dict(cls, d: Dict[str, str]):
        return cls(d['title'], d['author'])

class Novel(Book):
    def __init__(self, title: str, author: str, genre: str):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: {self.title} by {self.author} [{self.genre}]"

    # 7. Method Resolution
    @classmethod
    def from_string(cls, s: str):
        title, author, genre = s.split('|')
        return cls(title.strip(), author.strip(), genre.strip())

# 8. Hybrid Use Case Example Class
class Logger:
    logs = []

    def __init__(self, name):
        self.name = name

    def log(self, msg):
        print(f"[{self.name}] {msg}")
        Logger.logs.append(msg)

    @staticmethod
    def status():
        return "Logger is operational."

    @classmethod
    def log_count(cls):
        return len(cls.logs)

# --- Main Execution ---
if __name__ == "__main__":
    print("Static Method Test:")
    print(Book.is_valid_isbn("1234567890"))   # True
    print(Book.is_valid_isbn("abc"))          # False

    print("\nClass Method from_string:")
    b1 = Book.from_string("1984 | George Orwell")
    print(b1.describe())

    print("\nUse cls in subclass from_string:")
    n1 = Novel.from_string("Dune | Frank Herbert | Sci-Fi")
    print(n1.describe())

    print("\nAlternative constructors:")
    b2 = Book.from_json('{"title": "Sapiens", "author": "Yuval Noah Harari"}')
    b3 = Book.from_dict({'title': 'Atomic Habits', 'author': 'James Clear'})
    print(b2.describe())
    print(b3.describe())

    print("\nInvoke static method via instance:")
    print(b1.is_valid_isbn("9780134685991"))  # True

    print("\nMethod Resolution Check:")
    print(isinstance(n1, Book))  # True

    print("\nHybrid Example (Logger):")
    logger = Logger("Main")
    logger.log("System started")
    logger.log("Processing...")
    print(Logger.status())
    print(Logger.log_count())
