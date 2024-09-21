"""
Magic methods
"""


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author} has {self.pages} pages"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Book):
            return self.title == value.title and self.author == value.author

        return False


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 218)
book2 = Book("The Catcher in the Rye", "J.D. Salinger", 234)
book3 = Book("The Catcher in the Rye", "J.D. Salinger", 123)

print(book1)
print(book2 == book3)
