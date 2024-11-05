# TODO Напишите функцию find_common_participants

def find_common_participants (participants_first_group,participants_second_group , separator=','):
    spisok1 = set(participants_first_group.split(separator))
    spisok2 = set(participants_second_group.split(separator))

    spisok = list(spisok1.intersection(spisok2))
    spisok.sort()
    return spisok

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
end_spisok = find_common_participants(participants_first_group,participants_second_group, separator='|')
# TODO Провеьте работу функции с разделителем отличным от запятой
print (end_spisok)