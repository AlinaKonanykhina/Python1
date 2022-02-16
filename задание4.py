
dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_list = []
with open('задание_4.txt', 'r+') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_list.append(dict[i[0]] + i[1])
    print(new_list)

with open('задание_4_.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_list)


















# dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# new_file = []
# with open('', 'r') as file:
#     for i in file:
#         i = i.split(' ', 1)
#         new_file.append(dict[i[0]] + ' ' + i[1])
#     print(new_file)
#
# with open('задание_4.txt', 'w') as file_2:
#     file_2.writelines(new_file)