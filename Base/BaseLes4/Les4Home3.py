# Опишите класс сотрудника, который включает в себя такие поля, как имя, фамил
# ия, отдел и год поступления на работу. Конструктор должен генерировать исклю
# чение, если заданы неправильные данные. Введите список работников с клавиату
# ры. Выведите всех сотрудников, которые были приняты после заданного года.
class Worker:
    def __init__(self, name, surname, department, year):
        self.name = name
        self.surname = surname
        self.department = department
        self.year = year

    def __str__(self):
        return f"Сотрудник: {self.name} - " \
               f"Фамилия: {self.surname} - " \
               f"Отдел: {self.department} - " \
               f"Год поступления: {self.year}"

    # def set_list(self):
    #     my_list.append(self.name,
    #                    self.surname,
    #                    self.department,
    #                    self.year)
    #
    # def get_list(self):
    #     return my_list


my_list = []


def list():
    while True:
        try:
            n = int(input("1 - Добавить сотрудника \n"
                          "2 - Посмотреть список струдников \n"
                          "3 - Посмотреть сотрудника нужного года \n"
                          "4 - Выйти из програмы \nВведите номер: "))
            if n == 1:
                name = input("Введите имя сотрудника: ")
                surname = input("Введите фамилию сотрудника: ")
                department = int(input("Введите номер отдела сотрудника:"))
                year = int(input("Введите год принятия на работу: "))
                worker = Worker(name, surname, department, year)
                print(worker, sep=", ")
                my_list.append(worker)
            elif n == 2:
                for list in my_list:
                    print(list)
            elif n == 3:
                try:
                    check = int(input("Введите год сотрудника, "
                                      "которого нужно посмотреть "
                                      "в формате хххх: "))
                    if worker in my_list:
                        if worker.year == check:
                            print(worker)
                        else:
                            print("Не верный год")
                except UnboundLocalError:
                    print("Список пуст\n")
            elif n == 4:
                break
        except ValueError:
            print("Введите правильное значение!")


if __name__ == "__main__":
    list()
