class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def say_hello(self):
        print(f'Hello, I am {self.name}, age {self.age}, my color {self.color}')

cat = Animal(name='Graysi', age=6, color='gray')
dog = Animal(name='Hit', age=8, color='black')
fish = Animal(name='Bork', age=2, color='green')

cat.say_hello()
dog.say_hello()
fish.say_hello()