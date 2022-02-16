
my_dict = {}
with open('задание_6.txt') as my_file:
    content = my_file.readlines()
    subject = ()
    for line in content:
        subject, lecture, lab, practice = line.split()
        my_dict[subject] = int(lecture) + int(lab) + int(practice)
    print(f'Общее количество часов по предмету - \n {my_dict}')


