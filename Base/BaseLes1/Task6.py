class Car:
    def __init__(self, model, color, price):
        self.color = color
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.model}: {self.color}, {self.price}$."


class CarShop:
    my_list0 = []

    def print_info(self, value):
        self.value = value
        self.my_list0.append(self.value)


car1 = Car("Audi", "black", 1000)
car2 = Car("BMW", "black", 2000)
c1 = CarShop()
c1.print_info(car1)

print(car1)
print(car2)
print(c1)