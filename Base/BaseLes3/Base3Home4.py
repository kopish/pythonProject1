# Опишите два класса Base и его наследника Child с методами method(), который
# выводит на консоль фразы соответственно "Hello from Base"и"Hello fromChild".
class Base:
    def method(self):
        print("Hello from Base")


class Child(Base):
    def method(self):
        print("Hello from Child")


a = Child()
a.method()
b = Base()
b.method()


