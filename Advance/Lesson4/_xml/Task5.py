'''
Открытие и чтение с помощью ElementTree
Импортируйте объект ElementTree, откройте соответствующий XML-файл и получите корневой тег:
'''
import xml.etree.ElementTree as ET

tree = ET.parse("data/example1.xml")
root = tree.getroot()

# Есть несколько способов поиска по дереву. Сначала по итерации:
for child in root:
    print(child.tag, child.attrib)

# В противном случае вы можете ссылаться на определенные места, такие как список:
# print(root[0][1].text)
# Для поиска конкретных тегов по имени, используйте .find или .findall:
print(root.findall("myTag"))
print(root[0].find("myOtherTag"))