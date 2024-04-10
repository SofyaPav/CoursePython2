# TODO Напишите функцию find_common_participants
def func(str_1, str_2):
    final_list = []
    list_1 = str_1.split('|')
    list_2 = str_2.split('|')
    for i in list_1:
        if i in list_2:
            final_list.append(i)
    return(final_list)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(func(participants_first_group, participants_second_group))# TODO Провеьте работу функции с разделителем отличным от запятой
