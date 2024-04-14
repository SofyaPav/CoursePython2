# TODO Напишите функцию find_common_participants

def find_common_participants(str_1, str_2, sep=','):
    final_list = []
    list_1 = str_1.split(sep)
    list_2 = str_2.split(sep)
    for i in list_1:
        if i in list_2:
            final_list.append(i)
    final_list.sort()
    return final_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_first_group = participants_first_group.replace('|', ',')
participants_second_group = "Петров|Сидоров|Смирнов"
participants_second_group = participants_second_group.replace('|', ',')
print(find_common_participants(participants_first_group, participants_second_group, ','))# TODO Провеьте работу функции с разделителем отличным от запятой
