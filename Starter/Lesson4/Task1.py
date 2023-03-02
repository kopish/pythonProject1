x = 0

while x < 30:
    x += 1

    if 10 < x < 21:  # пропускаем число 5
        continue

    print('Текущее число равно', x)