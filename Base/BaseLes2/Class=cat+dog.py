# кот, собака, имя, голос вивод
class Animal:
    def __init__(self, animal, name, color, age):
        self.animal = animal
        self.name = name
        self.color = color
        self.age = age

    def voice(self):
        print(f"Це {self.animal}, на ім'я {self.name}, віком {self.age}, "
              f"{self.color}.")


class Cat(Animal):
    def voise(self):
        super().voice()
        print("Meow")


class Dog(Animal):
    def voise(self):
        super().voice()
        print("Wuf")


dog = Dog("dog", "Dark", "black", 12)
cat = Cat("cat", "Light", "white", 3)

dog.voise()
cat.voise()