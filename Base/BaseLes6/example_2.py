def fibonacci_generator(count):
    value_1, value_2 = 0, 1

    for _ in range(count):
        value_1, value_2 = value_2, value_1 + value_2
        yield value_1


fibonacci_iterator = fibonacci_generator(10)
fibonacci_iterator = fibonacci_generator(15)

for number in fibonacci_iterator:
    print(number)
