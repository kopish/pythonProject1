def fibonacci_sequence():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second


def fibonacci(limit):
    generator = fibonacci_sequence()
    for _ in range(limit):
        yield next(generator)


def nth_fibonacci(number):
    result = None
    for current in fibonacci(number):
        result = current
    return result


print(nth_fibonacci(3))
