a = 'Hello'
b = 'world'
import datetime

if __name__ == '__main__':
    result = 145584
    today = datetime.datetime.now()
    print(today)
    print(f'{today:%d-%m-%Y  %H:%M}')

    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print(f'{coord:latitude, longitude}')
    # 'Coordinates: 37.24N, -115.81W'