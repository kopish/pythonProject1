# Создайте иерархию классов с использованием множественного наследования.
# Выведите на экран порядок разрешения методов для каждого из классов.
# Объясните, почему линеаризации данных классов выглядят именно так.
class First:
    def __init__(self, obj1):
        self.obj1 = obj1

    def print(self):
        return str(self.obj1)


class Second(First):
    def print1(self, obj2):
        self.obj2 = obj2
        print(self.obj1, self.obj2)


class Third(Second, First):
    def print2(self, obj3):
        self.obj3 = obj3
        print(self.obj1, self.obj2 + obj3)


a = Third("Hello")
print(a.print())
a.print1("world")
a.print2("!!!")

# Каждый следующий (дочерний) класс унаследует объекты предыдущих
