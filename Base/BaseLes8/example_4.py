string = input('Введите строку: ').lower()
string1 = string.upper()
string2 = string.title()
rez = ''
if string == 'admin':
    rez = 'Ok'
else:
    rez = 'bad input'
print(rez)

print(string)
print(string1)
print(string2)
