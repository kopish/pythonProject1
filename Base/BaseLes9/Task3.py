try:
    file = open('test.txt', encoding='utf-8')
    # //////
finally:
    file.close() # Безопасное закрытие файла
