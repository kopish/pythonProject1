# Вывод построчно 10 символов и сохранение в отдельный файл
text = ""
with open('quotes.txt', 'r', encoding="UTF-8") as file:
    for line in file:
        text += file.read(10) + "\n"

with open('quotes2.txt', 'w', encoding="UTF-8") as file2:
    file2.writelines(text)