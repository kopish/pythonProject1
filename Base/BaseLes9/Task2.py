try:
    file = open('test1.txt', encoding='utf-8')
    # //////
finally:
    file.close()
    # Безопасное закрытие файла
