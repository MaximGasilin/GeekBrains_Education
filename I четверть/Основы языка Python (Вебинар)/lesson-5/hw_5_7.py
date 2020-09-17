# Задание # 6
#
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.

import json


def is_org_form_exist(form_name):
    tuple_of_org_forms = ('ООО', 'ПАО')
    return tuple_of_org_forms.count(form_name)


def cat_companies_finance(file_object):
    # Генератор, который считыват строки и рассчитывает финансовый результат

    for line in file_object:
        list_line = line.split()
        quantity = len(list_line)

        try:
            cost = float(list_line[quantity-1])
        except ValueError:
            cost = 0

        try:
            revenue = float(list_line[quantity-2])
        except ValueError:
            revenue = 0

        if is_org_form_exist(list_line[quantity - 3]) > 0:
            cur_index = quantity - 3
        else:
            cur_index = quantity - 2

        cur_company = ' '.join(list_line[:cur_index])

        yield cur_company, revenue, cost


if __name__ == '__main__':

    # file_name = 'lesson_5_task_7_list_of_companies.txt'
    file_name = input(f'Введите имя файла, из которого нужно считать данные: ')
    new_file_name = file_name.replace('.txt', '.json')
    new_file_name = (new_file_name, f'{file_name}.json')[new_file_name == file_name]
    print(new_file_name)

    final_dict = {}
    total_income = 0
    total_quantity = 0

    # Чтение файла и суммирование всех чисел из него происходит с помощью генератора
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        for el in cat_companies_finance(file_obj):
            income = el[1] - el[2]
            final_dict[el[0]] = income
            total_income += income if income > 0 else 0
            total_quantity += 1 if income > 0 else 0
            # print(el[0], income, total_income, total_quantity)

    # print(f'{final_dict}')
    final_list = [final_dict, {"average_profit": total_income / total_quantity if total_quantity != 0 else 1}]
    # print(f'{final_list}')

    with open(new_file_name, 'w', encoding='utf-8') as file_obj:
        json.dump(final_list, file_obj)
