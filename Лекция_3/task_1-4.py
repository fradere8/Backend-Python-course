from datetime import datetime
from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Book(Printable):
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        
    def info(self):
        return f"{self.title}: {self.author}, {self.year}"
    
    def __str__(self):
        return self.info()
    
    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title and self.author == other.author
    
    @property
    def book_age(self):
        return datetime.now().year - self.year
    
    @classmethod
    def from_string(cls, book_str: str):
        title, author, year = book_str.split(', ')
        return cls(title, author, int(year))
    
    def print_info(self):
        print(self.info())
    
book1 = Book('Евгений Онегин', 'А.С. Пушкин', 1833)
book1.print_info()
print(f"Возраст книги: {book1.book_age} лет")
book2 = Book.from_string('Война и мир, Л.Н. Толстой, 1869')
book2.print_info()

class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, format: str):
        super().__init__(title, author, year)
        self.format = format

    def info(self):
        return f"{self.title}: {self.author}, {self.year}, формат: {self.format}"
    
ebook1 = Ebook('1984', 'Джордж Оруэлл', 1949, 'PDF')
ebook1.print_info()