'''
Задание 1
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии,
годе издания и жанре. Создайте несколько разных книг. Определите для него операции проверки
 на равенство и неравенство, методы __repr__ и __str__.
Задание 2
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться
отзывы к ней.
'''
import datetime


class Comment:

    def __init__(self, user, book, comment):
        self.user = user
        self.book = book
        self.date = datetime.date.today()
        self.comment = comment

    def __str__(self):
        return '%s writes about %s : %s. %s.' % (self.user, self.book,
                                                 self.comment, self.date)


com1 = Comment('Hater', 'White Fang', 'Very bad book')
com2 = Comment('Lover', 'White Fang', 'Good')
com3 = Comment('Djodjo', 'Harry Potter', 'I do not understand that language')


class Book:
    """
    Class that describes a book.
    """
    def __init__(self, author, name, year, edition, genre, *comments):
        self.author = author
        self.name = name
        self.year = year
        self.edition = edition
        self.genre = genre
        self.comments = comments

    def print_comments(self):
        comments = ''
        for n, c in enumerate(self.comments, start=1):
            comments += '%d.%s\n' % (n, str(c))
        return comments

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name

    def __repr__(self):
        return '%s_%s_%d' % ('_'.join(self.author.split(' ')), '_'.join(self.name.split(' ')), self.year)

    def __str__(self):
        return '%s - %s(%d).%s edition.\nComments:\n%s ' % (self.author, self.name, self.year,
                                                            self.num(self.edition), self.print_comments())

    def num(self,number):
        num_dict ={
            '1': 'st',
            '2': 'nd',
            '3': 'rd',
            '4': 'th'
        }
        last_digit = str(number)[-1:]
        last_2_digits = str(number)[-2:]
        if 20 >= int(last_2_digits) >= 4 :
            return '%s-%s' % (number, num_dict['4'])
        elif int(last_digit) >= 4:
            return '%s-%s' % (number, num_dict['4'])
        else:
            return '%s-%s' % (number, num_dict[last_digit])


book1 = Book("Jack London", "White Fang", 1892, 122, "Classic", com1, com2, com3)
book2 = Book("Jack Jordan", "Yellow Fang", 1992, 5, "Comedy", com2)
book3 = Book("Jack London", "White Fang", 1998, 4, "Classic")
book4 = Book("Victor Gugo", "Les Miserables", 1843, 67, "Classic", com1, com1, com3)

print(book1)
print(book2)
print(book3)
print(book4)