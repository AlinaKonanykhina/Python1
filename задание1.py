import sys

my_list = []
while True:
    line = input("Введите текст : ")
    if line == '':
        sys.exit(0)
    else:
        newline = line + '\n'
        my_list.append(newline)
    with open("задание_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)
