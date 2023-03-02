# класс кар модель машини, цвет, год впуска, класс наследник апдейт,
# принт вивод с изменениями, в апдейте стоимость
class Car:
    def __init__(self, mod, col, yer):
        self.mod = mod
        self.col = col
        self.yer = yer


class Car_Upd(Car):
    def fors(self, mod, col, yer, price):
        super().__init__(self, mod, col, yer)
        self.price = price

    def __print(self):
        return f"Model avto {self.mod}\n " \
               f"color {self.col}\n year {self.yer}\n"

    # @staticmethod
    def get_print(self):
        return self.__print()
        # print(self.__print)

    # def update(self, mod, col, yer, price):


avto = Car_Upd("toyota", "white", 1995)
print(avto.get_print())

