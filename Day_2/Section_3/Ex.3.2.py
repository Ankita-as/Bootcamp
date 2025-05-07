# Base class
class Book:
    category = "Fiction"

    def __init__(self, title="Untitled", author="Unknown"):
        self.title = title
        self.author = author

    def describe(self):
        return f"'{self.title}' by {self.author}"

    def __str__(self):
        return f"[Book] Title: {self.title}, Author: {self.author}"

# Subclass
class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def describe(self):
        return f"Novel: {super().describe()}, Genre: {self.genre}"

# Mixin class for audio features
class AudioMixin:
    def play_audio(self):
        return f"Playing audio version of '{self.title}'"

# Multiple inheritance
class AudioBook(Book, AudioMixin):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration

    def describe(self):
        return f"AudioBook: '{self.title}' by {self.author}, Duration: {self.duration} mins"

# Testing everything
if __name__ == "__main__":
    book = Book("1984", "George Orwell")
    novel = Novel("Pride and Prejudice", "Jane Austen", "Romance")
    audiobook = AudioBook("The Hobbit", "J.R.R. Tolkien", 720)

    # __str__ method
    print(str(book))

    # Method overriding and super()
    print(novel.describe())

    # Mixin behavior
    print(audiobook.describe())
    print(audiobook.play_audio())

    # isinstance checks
    print("Is novel a Book?", isinstance(novel, Book))
    print("Is audiobook a Book?", isinstance(audiobook, Book))

    # Polymorphism
    print("\nPolymorphism Demo:")
    for item in [book, novel, audiobook]:
        print(item.describe())
