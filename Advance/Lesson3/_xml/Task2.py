# Изменение файла XML
import xml.etree.ElementTree as ET

tree = ET.parse('data/example.xml')
root = tree.getroot()
# Получение первого ребенка родительского корня element
element = root[0]

# Элементом объекта  можно управлять, изменяя его поля, добавляя и изменяя атрибуты, добавляя и удаляя дочерние элементы
# Установка артрибута xml элементу
element.set('attribute_name', 'attribute_value')
element.text = "string_text"

# Для удаления элемента, используйте метод Element.remove()
root.remove(element)
# Метод ElementTree.write(), используется для вывода объекта XML в файлы XML.
tree.write('data/example.xml')
ET.dump(tree)
