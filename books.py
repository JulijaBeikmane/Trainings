class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():  
            raise ValueError("Название книги не может быть пустым.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value.strip(): 
            raise ValueError("Имя автора не может быть пустым.")
        self._author = value

 
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < 1800:  
            raise ValueError("Год издания должен быть больше или равен 1800.")
        self._year = value


    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if not value.strip():  
            raise ValueError("Жанр книги не может быть пустым.")
        self._genre = value
    def get_info(self):
            return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Жанр: {self.genre}"
    
class Library(): 
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def get_books_by_author(self, author):
        books_by_author = [book for book in self.books if book.author == author]
        return books_by_author
    #    if author == author:
    #        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Жанр: {self.genre}"
    #    for book in self.books:
    #         if book.author == author:
    #             return self.book
    
    def get_books_by_genre(self, genre):
        books_by_genre = [book for book in self.books if book.genre == genre]
        return books_by_genre

#Для 1 задания
book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман")
# print(book1.get_info())
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1940, "Роман")
#Для 2 задания
library = Library()
library.add_book(book1)
library.get_books_by_author("Лев Толстой")

books_by_tolstoy = library.get_books_by_author("Лев Толстой")
print("Книги Льва Толстого:")
for book in books_by_tolstoy:
    print(book.get_info())
books_by_roman = library.get_books_by_genre("Роман")
print("Жанр:")
for book in books_by_roman:
    print(book.get_info())
