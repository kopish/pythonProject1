'''
Реализуйте итератор колоды карт (52 штуки) CardDeck. Каждая карта представлена в виде строки типа «2 Пик». При
вызове функции next() будет представлена следующая карта. По окончании перебора всех элементов возникнет ошибка
StopIteration.
'''

'''Чтобы реализовать протокол итератора требуется внедрить 2 метода: __iter__() и __next__(). Для понимания того,
 что коллекция иссякла, не стоить забывать и про ее длину (52).'''


class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']

    def __len__(self):
        return self.length

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            suit = self.__SUITS[self.index // len(self.__RANKS)]
            rank = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            return f'{rank} {suit}'

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))
