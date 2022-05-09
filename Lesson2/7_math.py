# импротируем модуль math
import math

x = 3.265
# целое число, ближайшее целое снизу, ближайшее целое сверху
print(math.trunc(x), math.floor(x), math.ceil(x))

# константа пи
print(math.pi)
# число Эйлера
print(math.e)

# math.sin – синус
y = math.sin(math.pi / 4)
print(round(y, 2))

# math.sqrt – квадратный корень
y = 1 / math.sqrt(2)
print(round(y, 2))
