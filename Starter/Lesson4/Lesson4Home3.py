# Создайте любую переменную строку и поместите туда любой текст. Сделайте так, чтобы все
# нечетные по порядку слева на право символы стали “_”, а все символы, местоположение
# которых четное и которые равны “r” - стали “a”. Например “Ham is tasty” => “_b_ _s_t_s_y”.
word = "Good evening, we are from Ukraine !!!"
new_word = ""
cont = 0
for ch in word:
    if cont == len(word):
        break
    if cont % 2:
        new_word += '_'
    elif ch == "r":
        new_word += "a"
    else:
        new_word += ch
    cont += 1
print(new_word)
