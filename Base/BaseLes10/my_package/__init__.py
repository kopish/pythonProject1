# Особенность этого файла в том, что он исполняемый
# Будет исполняться, когда будет импортироваться пакет, т.е. 1 раз!!
print('__init__ my_package')

# Внутри данного файла модули тоже можно импортировать
# from .my_module1 import *
# from .my_module2 import *

from . import my_module1, my_module2

__all__ = ['my_module1', 'my_module2']

# . текущий каталог
# .. каталог, который выше