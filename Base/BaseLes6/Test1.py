a = (i ** 10 for i in range(1, 5))

print(next(a))
print(next(a))
print(next(a))
print(next(a))
# вылет исключения StopIteration
# next(a)
