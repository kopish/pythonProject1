login = 'Qwerty'
password = 'Admin'
for i in range(3):
    if input('Введите логин: ') == login and input('Введите пароль: ') == password:
        print('Вы успешно вошли в систему с', i+1, 'попытки')
        break
