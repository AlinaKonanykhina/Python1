
def my_sum():
    try:
        with open('задание_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            numb = line.split()
            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
my_sum()
