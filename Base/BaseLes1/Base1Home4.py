# Создайте класс, описывающий автомобиль. Создайте класс автосалона,
# содержащий в себе список автомобилей, доступных для продажи,
# и функцию продажи заданного автомобиля.
class Car:
    def __init__(self, mod, col, yer, price):
        self.mod = mod
        self.col = col
        self.yer = yer
        self.price = price

    def __str__(self):
        return f"Model avto: {self.mod};" \
               f" color: {self.col}; year: {self.yer}; " \
               f"price: {self.price}$\n"


class CarShowroom:
    my_list = []

    def fors(self, value):
        self.value = value
        self.my_list.append(self.value)


car1 = Car("BMW X5", "white", 2018, 44000)
car2 = Car("Citroen", "white", 2010, 10000)
car3 = Car("Volvo", "white", 2005, 8000)
car4 = Car("Toyota", "white", 1995, 25965)
c1 = CarShowroom()
c1.fors(car3)
print(car1, car2, car3, car4)
print(c1)


