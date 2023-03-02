login = 'Qwerty'
password = 'Admin'
user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')
while (login != user_login) or (password != user_password):
    print('Неверно введён логин или пароль! Повторите попытку ввода данных.')
    user_login = input('Введите логин: ')
    user_password = input('Введите пароль: ')
print('Вы успешно вошли в систему!')
