# создать класс, имя, возраст, цвет, вывести на экран 3 обьекта
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def tiger(self):
        print("Name animal:", self.name)
        print("Age animal:", self.age)
        print("Color animal:", self.color)


tiger_2 = Animal("Arl", 25, "blue")
tiger_3 = Animal("David", 38, "black")
tiger_1 = Animal("Alf", 19, "yellow")
tiger_1.tiger()
tiger_2.tiger()
tiger_3.tiger()
