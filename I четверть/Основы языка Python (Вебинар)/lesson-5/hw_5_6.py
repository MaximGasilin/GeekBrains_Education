# Задание # 6
#
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def cat_education_plan(file_object):
    # Генератор, который считыват троки и рассчитывает общее количество часов

    digits = '0123456789'

    for line in file_object:
        cur_index = line.find(':')
        cur_subject = line[:cur_index]

        cur_number = ''
        sum_hours = 0
        for cur_symbol in line[cur_index+1:]:
            if digits.find(cur_symbol) > -1:
                cur_number = cur_number + cur_symbol
            elif len(cur_number) > 0:
                sum_hours += int(cur_number)
                cur_number = ''
        else:
            if len(cur_number) > 0:
                sum_hours += int(cur_number)

        yield cur_subject, sum_hours


if __name__ == '__main__':

    # file_name = 'lesson_5_task_6_education_plan.txt'
    file_name = input(f'Введите имя файла, из которого нужно считать данные: ')
    final_dict = {}

    # Чтение файла и суммирование всех чисел из него происходит с помощью генератора
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        for el in cat_education_plan(file_obj):
            final_dict[el[0]] = el[1]

    print(f'{final_dict}')
