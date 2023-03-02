my_list = [1, 3, 6, 10, 15]

a = (x ** 2 for x in my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
next(a)

print()

print(sum(x ** 2 for x in my_list))
print(max(x ** 2 for x in my_list))
