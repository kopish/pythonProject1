'''
Поиск в XML с помощью XPath
Начиная с версии 2.7 ElementTree имеет лучшую поддержку XPath запросов. XPath - это синтаксис, позволяющий вам перемещаться по XML, как SQL используется для поиска в базе данных. Как find и findall функции поддержки XPath. Xml ниже будет использоваться для этого примера

Поиск всех книг:
'''
import xml.etree.cElementTree as ET

tree = ET.parse('data/example2.xml')
tree.findall("Books/Book")

# Поиск книги с названием «Цвет магии»:
tree.find("Books/Book[Title='The Colour of Magic']")
# всегда используйте '' в правой стороне сравнения

# Поиск книги с id = 5:
tree.find("Books/Book[@id='5']")
# поиск с xml атрибутами должен иметь '@' перед именем

# Поиск второй книги:
tree.find("Books/Book[2]")
# индексы начинаются с 1, не с 0

# Поиск последней книги:
tree.find("Books/Book[last()]")
# 'last' единственная xpath функция позволенная в ElementTree

# Поиск всех авторов:
tree.findall(".//Author")
# поиск с // должен использовать родственный путь