# Создайте класс, описывающий отзыв к книге.
# Добавьте в класс книги поле – список отзывов.
# Сделайте так, что при выводе книги на экран
# при помощи функции print также будут выводиться отзывы к ней.

class BookReview:
    """Класс отзывов"""
    reviews = list()

    def __init__(self):
        pass

    def add_reference(self, review):
        return self.reviews.append(review)

    def read_ref(self):
        return self.reviews

    def read_ref_elem(self, i):
        return self.reviews[i]

    def __str__(self):
        return f"ref: {self.reviews}"


class Book:
    """Класс книги"""

    def __init__(self, author, title, year_edition, genre):
        self.author = author
        self.title = title
        self.year_edition = year_edition
        self.genre = genre
        self.info = [author, title, year_edition, genre]

    def check(self, other_book):
        # Проверка на принадлежность аргумента other_book к классу Book
        if not isinstance(other_book, Book):
            raise ValueError("Аргумент должен принадлежать к классу Book.")

        if self.info == other_book.info:
            res = "Книги равны"
        else:
            res = "Книги не равны"
        return print(res)

    def load_references(self):
        return BookReview()

    def add_review(self, comments):
        self.book_review = self.load_references()
        self.book_review.add_reference(comments)

    def open_review(self):
        return self.book_review.read_ref()

    def __str__(self):
        return f"Book: {self.info}"

    def __repr__(self):
        return f"Book('{self.info}')"


ex1 = Book('Петров', 'Python для чайников', 2016, 'IT')

print(ex1.info)

print('Comments for this book:')
ex1.add_review('good')
ex1.add_review('very good')
ex1.add_review('very bad')
print('*********************')
print(ex1.open_review())

# Проверка как работает класс отзывов
print('Class отзывы:')
r = BookReview()
r.add_reference('good')
r.add_reference('bad')
r.add_reference('very bad')
print(r.reviews)
print('----------------')
print(r.read_ref())
print('_________________')
print(r.read_ref_elem(2))