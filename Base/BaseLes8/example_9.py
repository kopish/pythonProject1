def function(**kwargs):
    print(kwargs)


function(arg1='value1', arg2='value2')

# Аналогично можно и распаковывать любые отображения
# в именованные параметры при вызове функции.

options = {
    'sep': ', ',
    'end': ';\n'
}

print('value1', 'value2', **options)
