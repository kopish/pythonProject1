# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе,
# названии, годе издания и жанре. Создайте несколько разных книг.
# Определите для него операции проверки на равенство и неравенство,
# методы __repr__ и __str__.
class Book:
    def __init__(self, title, author, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title}\n" \
               f"Author this book: {self.author}\n" \
               f"This book is published: {self.year}\n" \
               f"The book genre: {self.genre}\n"

    def __repr__(self):
        return f"{self.title}\n" \
               f"Author this book: {self.author}\n" \
               f"This book is published: {self.year}\n" \
               f"The book genre: {self.genre}\n"


book_1 = Book("The Dark Tower", "Stephen King", "1978", "dark fantasy")
book_2 = Book("Will", "Will Smith, Mark Manson", "2022", "biography")
book_3 = Book("Month of War",
              "Alexandr Krasovitsky",
              "2022",
              "historical journalism")

print(book_1.__str__())
print(book_2.__str__())
print(book_3.__repr__())

print(book_1.__str__() == book_1.__repr__())
print(book_1.__str__() != book_1.__repr__())
