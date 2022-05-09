# логические операции

print('And:')
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print()

print('Or:')
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print()

print('Not:')
print(not False)
print(not True)
print()


# логические выражения
a = True
b = False
c = True
f = a and not b or c or (a and (b or c))
print(f)
