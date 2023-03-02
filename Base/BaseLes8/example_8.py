# Все эти примеры создают одинаковые словари
a = dict(one=[1, 5], two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e)

print(a)
print(b)
print(c)
print(d)
print(e)

print(a.keys())
print(a.values())
print(len(c))
e['three'] = 5

print(e)

q = dict()
print(q)


# Использование включений словарей (аналогично списковым включениям)
print({string: string.upper() for string in ('one', 'two', 'three')})
