def worker_max_efficiency(workers):
    maximum = 0
    for worker in workers:
        if workers[worker]['эффективность'] > maximum:
            maximum = workers[worker]['эффективность']
    return maximum


def worker_min_efficiency(workers):
    minimum = 150
    for worker in workers:
        if workers[worker]['эффективность'] < minimum:
            minimum = workers[worker]['эффективность']
    return minimum


workers = {
    'Смирнов': {
        'должность': 'менеджер по продажам',
        'эффективность': 86
    },
    'Колягина': {
        'должность': 'менеджер по продажам',
        'эффективность': 69
    },
    'Костин': {
        'должность': 'менеджер по продажам',
        'эффективность': 78
    },
    'Щербаков': {
        'должность': 'менеджер по продажам',
        'эффективность': 91
    },
    'Борисова': {
        'должность': 'менеджер по продажам',
        'эффективность': 99
    }
}


print('Лучший результат:', worker_max_efficiency(workers))
print('Худший результат:', worker_min_efficiency(workers))
