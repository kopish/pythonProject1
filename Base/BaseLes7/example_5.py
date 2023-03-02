# Реализация поддержки операции
class Container(object):
    def __contains__(self, element):
        return element == 3


container = Container()
print(3 in container)
print(5 in container)
