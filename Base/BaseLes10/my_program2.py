import sale

answer = input('Желаете посетить чемпионат мира по футболу? (да/нет)').lower()
if answer == 'да':
    sale.get_total_price()
else:
    print('Жаль!')
