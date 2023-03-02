# Создать уникальный список с двух
def function_list(list_1, list_2):
    my_list = []
    for element in list_1:
        if element not in list_2:
            if element not in my_list:
                my_list.append(element)
    for element in list_2:
        if element not in list_1:
            if element not in my_list:
                my_list.append(element)
    return my_list


my_list_1 = [14, 12, 5, 3, 8, 9, 5, 5]
my_list_2 = [15, 3, 5, 8, 9, 40, 20]
print(function_list(my_list_1, my_list_2))
