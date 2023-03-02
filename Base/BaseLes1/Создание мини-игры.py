class Hero:
    # конструктор класса
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print("\nПоприветствуем нашего героя - >", self.name)
        print("Уровень здоровья:", self.health)
        print("Класс брони:", self.armor)
        print("Сила удара:", self.power)
        print("Оружие:", self.weapon)

    def strike(self, enemy):
        print("-> УДАР!" + self.name + " атакует " + enemy.name + ' c силой ' + str(self.power) + ', используя '
              + self.weapon + '\n')
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name + ' покачнулся(-ась).\nКласс брони упал до ' + str(enemy.armor) + ', а уровень здоровья до '
              + str(enemy.health) + '\n')
        

khight = Hero('Крусайдер', 80, 30, 25, "меч")
rascal = Hero('Эльф', 26, 15, 10, "лук")

khight.print_info()
rascal.print_info()

khight.strike(rascal)
rascal.strike(khight)
