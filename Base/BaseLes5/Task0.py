# Использование итераторов дважды

numbers = [1, 2, 3, 4, 5]

squared_numbers = (number ** 2 for number in numbers)

print(list(squared_numbers))

print(list(squared_numbers))
