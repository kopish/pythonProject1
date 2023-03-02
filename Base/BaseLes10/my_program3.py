from analyser import *

request = input('Чем я могу вам помочь?')
while request != 'off':
    analyse(request)
    request = input('Чем я ещё могу вам помочь? (off - завершить)')
