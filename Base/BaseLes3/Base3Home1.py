# Создайте класс, описывающий автомобиль. Какие атрибуты и методы должны быть
# полностью инкапсулированы? Доступ к таким атрибутам и изменение данных
# реализуйте через специальные методы (get, set).
class Car:
    def __init__(self, mod, col, yer, price):
        self.mod = mod
        self.col = col
        self.yer = yer
        self.price = price

    @property
    def __print(self):
        return f"Model avto: {self.mod}\nColor: {self.col}\nYear: {self.yer}\n"

    def print(self):
        print(self.__print)


avto = Car("toyota", "white", 1995, 20000)
avto.print()