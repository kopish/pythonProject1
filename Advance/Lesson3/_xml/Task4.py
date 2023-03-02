'''
Открытие и чтение больших файлов XML с помощью iterparse (инкрементальный анализ)

Иногда мы не хотим загружать весь XML-файл, чтобы получить необходимую нам информацию. В этих случаях полезно
постепенно загружать соответствующие разделы и затем удалять их, когда мы закончим. С помощью функции iterparse вы
можете редактировать дерево элементов, которое хранится при разборе XML.

Импортируйте объект ElementTree:
'''
import xml.etree.ElementTree as ET
'''
# Откройте файл .xml и переберите все элементы:

for event, elem in ET.iterparse("data/example.xml"):
#    ...  сделайте что-нибудь ...

# Кроме того, мы можем искать только определенные события, такие как начальный / конечный теги или пространства имен. 
# Если эта опция не указана (как указано выше), возвращаются только события «end»:

events=("start", "end", "start-ns", "end-ns")
for event, elem in ET.iterparse("data/example.xml", events=events):
    ... do something ...
'''

for event, elem in ET.iterparse("data/example.xml", events=("start", "end")):
    if elem.tag == "record_tag" and event == "end":
        print(elem.text)
        elem.clear()
# Выводим содержимое файла
ET.dump(elem)
