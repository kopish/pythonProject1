amount_five = 0
amount_four = 0
count = 0
# amount
a = int(input('Введите оценку (0 - стоп): '))
while a != 0:
    if a == 5:
        amount_five += 1
    elif a == 4:
        amount_four += 1
    else:
        print('Качество обучения желает быть лучше!')
    count += 1
    a = int(input('Введите оценку (0 - стоп): '))
print('Качество обучения: ', round(((amount_five + amount_four) / count * 100), 2), "%")
