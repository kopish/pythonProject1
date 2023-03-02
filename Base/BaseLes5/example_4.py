class Fibonacci:

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.count = 0
        self.last_numbers = (0, 1)

        return self

    def __next__(self):
        last_number, current_number = self.last_numbers
        last_number, current_number = current_number, last_number + current_number

        self.last_numbers = last_number, current_number
        self.count += 1

        if self.count > self.max:
            raise StopIteration

        return last_number


fibo = Fibonacci(10)

for number in fibo:
    print(number)