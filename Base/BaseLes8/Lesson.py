# Вывести уникальные слова
a = "Капитан Пит «Мэверик» Митчел (Том Круз) по-прежнему совершает боевые " \
    "вылеты. Он так же искусен в небе, однако отказывается от повышений " \
    "по службе. Боевик «Топ Ган: Мэверик» является прямым продолжением " \
    "фильма «Самый лучший стрелок», вышедшего на экраны в 1986 году." \
    " Режиссером на этот раз стал Джозеф Косински («Обливион»). (Том Круз)" \
    "Тони Скотт, режиссер первого фильма, покончил жизнь самоубийством в" \
    " 2012 году за день до запланированной встречи с исполнителем главной " \
    "роли Томом Крузом. Это обусловило задержку реализации проекта. О начале" \
    " работы над продолжением объявили в 2017 году. Основные съемки начались" \
    " весной 2018-го и длились год. Сначала релиз ленты был запланирован на" \
    " лето 2019 года, однако из-за сложных визуальных эффектов премьеру " \
    "перенесли на 2020 год. К выполнению своей роли вернулся Том Круз. " \
    "Однако, его партнершу по первому фильму Келли МакГиллис не пригласили." \
    " В новом фильме любовным интересом Меверика станет героиня Дженнифер " \
    "Коннелли."


def get_unique_strings(a):
    list_of_unique_string = []
    unique_string = set(a)

    for number in unique_string:
        list_of_unique_string.append(number)

    return list_of_unique_string


print(get_unique_strings(a))

