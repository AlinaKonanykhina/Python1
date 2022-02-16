# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
user_number = int(input('Введите целое число: '))
my_list = [8, 7, 7, 5, 4, 4, 3]
a = my_list.count(user_number)
for i in my_list:
    if a > 0:
        el = my_list.index(user_number)
        my_list.insert(el + a,user_number)
        break
    else:
        if user_number > i:
            b = my_list.index(i)
            my_list.insert(b,user_number)
        elif my_list[ len(my_list)-1] > user_number:
            my_list.append(user_number)

print(my_list)