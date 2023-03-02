class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


# user = User(name="Alex")
# user.name = "Bob"
# print(user.name)

class Worker:
    RIGHTS = "Equal"

    def __init__(self, working_class):
        self.__salary_map = {
            "A": 100,
            "B": 200,
            "C": 500
        }
        self.__salary = self.__get_salary(working_class)

    def __get_salary(self, working_class):
        return self.__salary_map.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


class User2:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


w1 = Worker("A")
print(w1.salary)
