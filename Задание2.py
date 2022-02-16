
with open('задание_2.txt') as f_obj:
    line = 0
    for i in f_obj:
        line += 1
        flag = 0
        word = 0
    for a in i:
        if a != ' ' and flag == 0:
            word += 1
            flag = 1
        elif a == ' ':
            flag = 0
    print(i,len(i),'симв.',word,'слов(а)')

print(line,'стр.')
