def palindrom(s):
    if len(s) <= 1:
        return print("Введена фраза являється паліндромом")
    if s[0] != s[-1]:
        return print("Введена фраза не паліндром")
    return palindrom(s[1:-1])


pal = input("Введіть фразу паліндром: \n")
palindrom(pal)