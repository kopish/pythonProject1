# Создайте 2 класса – языка, например, английский и испанский. У обоих классов
# должен быть метод greeting(). Оба создают разные приветствия. Создайте два
# соответствующих объекта из двух классов выше и вызовите действия этих двух
# объектов в одной функции (функция hello_friend).
class English:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hello {self.name}, have a nice day!"


class Spanish:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hi my friend {self.name}!"


def hello_friend(a, b):
    print(a.greeting())
    print(b.greeting())


alex = English("Alex")
yana = Spanish("Yana")
hello_friend(alex, yana)

