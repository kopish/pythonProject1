def analyse(phrase):
    phrase = phrase.lower()
    res = phrase.find('расп')
    if res != -1:
        print_schedule()

    res = phrase.find('тренер')
    if res != -1:
        print_trainer_info()

    res1 = phrase.find('оплат')
    res2 = phrase.find('деньг')
    if res1 != -1 or res2 != -1:
        calc_money()


def print_schedule():
    print('Расписание тренировок:')
    print('ПН 15:00 - общая силовая тренировка\nСР 15:00 - бассейн\nПТ 17:00 - бассейн')


def print_trainer_info():
    print('Главный тренер: Борисов Иван Сергеевич, 8800231344')
    print('Тренер по плаванию: Светлова Ирина Олеговна, 88002313234')


def calc_money():
    trainings = int(input('Сколько тренировок вы посетили?'))
    print('К оплате:', trainings * 1500)
