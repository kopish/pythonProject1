# Создайте иерархию классов транспортных средств. В общем классе опишите общие
# для всех транспортных средств поля, в наследниках – специфичные для них.
# Создайте несколько экземпляров. Выведите информацию о каждом транспортном
# средстве.

class Avto:
    def __init__(self, mod, col, yer, price):
        self.mod = mod
        self.col = col
        self.yer = yer
        self.price = price

    def __str__(self):
        return f"Model avto: {self.mod};" \
               f" color: {self.col}; year: {self.yer}; " \
               f"price: {self.price}$\n"


class Car(Avto):
    def __init__(self, mod, col, yer, price, engine, fuel):
        self.engine = engine
        self.fuel = fuel
        super().__init__(mod, col, yer, price)

    def __str__(self):
        return f"Model avto: {self.mod};" \
               f" color: {self.col}; year: {self.yer}; " \
               f"price: {self.price}$, engine: {self.engine}; " \
               f"fuel: {self.fuel}"


class Mustang(Car):
    def __init__(self, mod, col, yer, price, engine, fuel, armchaire):
        self.armchaire = armchaire
        super().__init__(mod, col, yer, price, engine, fuel)

    def __str__(self):
        return f"Model avto: {self.mod};" \
               f" color: {self.col}; year: {self.yer}; " \
               f"price: {self.price}$, engine: {self.engine}; " \
               f"fuel: {self.fuel}, armchair: {self.armchaire}"

car1 = Car("BMW X5", "white", 2018, 44000, 2.8, "diesel")
car2 = Car("Citroen", "white", 2010, 10000, 3.0, "bensin")
car3 = Car("Volvo", "white", 2005, 8000, 2.8, "diesel")
car4 = Car("Toyota", "white", 1995, 25965, "electric", "electric")
car5 = Mustang("Ford", "blue", 2015, 68000, 5.5, "benzin", "skin")
car1.__str__()
car2.__str__()
car3.__str__()
car4.__str__()
car5.__str__()
print(car1)
print(car2)
print(car3)
print(car4)
print(car5)