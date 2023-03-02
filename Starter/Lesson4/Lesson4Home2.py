# В предложении “Hello world” заменить все буквы “o” на “a” , а буквы “l” на “e”.
word = "Hello World"
new_word = ""

for ch in word:
    if ch == "o":
        new_word += "a"
    elif ch == "l":
        new_word += "e"
    else:
        new_word += ch
print(new_word)
