# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле –
# список отзывов. Сделайте так, что при выводе книги на экран при помощи
# функции print также будут выводиться отзывы к ней.
class Comment:
    def __init__(self, user, title, comment):
        self.user = user
        self.title = title
        self.comment = comment

    def __str__(self):
        return f"{self.user} writes about {self.title} - {self.comment}"


comment_1 = Comment("Jack", "The Dark Tower", "Very interesting book")
comment_2 = Comment("Galya", "The Dark Tower", "I recommend reading")
comment_3 = Comment("Jack", "Will", "Very interesting book")
comment_4 = Comment("Susy", "Month of War", "I recommend reading")


class Library:

    def __init__(self, title, author, year, genre, *comment):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.comment = comment

    def __str__(self):
        return f"{self.title}\n" \
               f"Author this book: {self.author}\n" \
               f"This book is published: {self.year}\n" \
               f"The book genre: {self.genre}\n" \
               f"Comments:\n" \
               f"{self.print_comments()}\n"

    def print_comments(self):
        comment = ''
        for n, c in enumerate(self.comment, start=1):
            comment += '%d.%s\n' % (n, str(c))
        return comment


book_1 = Library("The Dark Tower",
                 "Stephen King",
                 "1978",
                 "dark fantasy",
                 comment_1, comment_2)
book_2 = Library("Will",
                 "Will Smith, Mark Manson",
                 "2022",
                 "biography",
                 comment_3)
book_3 = Library("Month of War",
                 "Alexandr Krasovitsky",
                 "2022",
                 "historical journalism", comment_4)


print(book_1.__str__())
print(book_2.__str__())
print(book_3.__str__())

