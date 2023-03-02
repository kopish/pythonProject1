def get_ticket_price():
   price = 2000
   number = int(input('Номер заказа:'))
   if number % 1000 == 0:
       price *= 0.8
   return price


def get_total_price():
   total = 0
   while input('Купить билет? (off - завершить)') != 'off':
       current_price = get_ticket_price()
       print('Цена за билет:', current_price)
       total += current_price
   print('Итого к оплате:', total)
