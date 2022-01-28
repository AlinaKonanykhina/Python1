#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

user_str = input("Введите строку: ")
my_str = []
num = 1
for i in range(user_str.count(' ') + 1):
    my_str = user_str.split()
    if len(str(my_str)) <= 10:
        print(f" {num} {my_str [i]}")
        num += 1
    else:
        print(f" {num} {my_str [i] [0:10]}")
        num += 1