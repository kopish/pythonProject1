# Используя ссылки в конце данного урока, ознакомьтесь с таким средством
# инкапсуляции как свойства. Ознакомьтесь с декоратором property в Python.
# Создайте класс, описывающий температуру и позволяющий задавать и получать
# температуру по шкале Цельсия и Фаренгейта, причём данные могут быть заданы в
# одной шкале, а получены в другой.
class Celsius:
    def __init__(self, temperatur=0):
        self.temperatur = temperatur

    def faren(self):
        return (self.temperatur * 1.8) + 32

    @property
    def temperatur(self):
        return self._temperature

    @temperatur.setter
    def temperatur(self, value):
        if value < -273.15:
            raise ValueError("Температура не може опускатись нижче -273.15")
        self._temperature = value


human = Celsius(37)
print(human.temperatur)
print(human.faren())

