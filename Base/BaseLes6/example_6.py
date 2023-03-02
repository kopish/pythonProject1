# Создание бесконечной последовательности
def all_even():
    n = 0
    while True:
        yield n
        n += 2


print(all_even())
"""while True:
    print(next(all_even()))"""
