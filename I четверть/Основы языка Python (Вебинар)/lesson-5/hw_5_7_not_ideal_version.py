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


list_of_org_forms = ('ООО', 'ПАО')


def caе_companies_finance(file_object):
    # Генератор, который считыват троки и рассчитывает финансовый результат

    global list_of_org_forms

    digits = '0123456789'

    for line in file_object:
        # Сперва пытаемся выделить название фирмы
        cur_index = -1
        for org_forms in list_of_org_formes:
            cur_index = max(cur_index, line.find(org_forms))
            if cur_index > -1:
                break
        if cur_index == -1:
            for cur_digit in digits:
                cur_index = max(cur_index, line.find(cur_digit))
                if cur_index > -1:
                    break

        cur_company = line[:cur_index].strip(' ')

        # Затем считываем значение выручки и расходов
        cur_number = ''
        read_revenue = True
        revenue = 0
        cost = 0

        for cur_symbol in line[cur_index+1:]:
            if digits.find(cur_symbol) > -1:
                cur_number = cur_number + cur_symbol
            elif len(cur_number) > 0:
                if read_revenue:
                    revenue = int(cur_number)
                    read_revenue = False
                else:
                    cost = int(cur_number)
                cur_number = ''
        else:
            if len(cur_number) > 0:
                if read_revenue:
                    revenue = int(cur_number)
                else:
                    cost = int(cur_number)

        yield cur_company, revenue, cost


if __name__ == '__main__':

    file_name = 'lesson_5_task_7_list_of_companies.txt'
    new_ile_name = 'lesson_5_task_7_finance_result_of_companies.json'

    final_dict = {}
    total_income = 0
    total_quntity = 0

    # Чтение файла и суммирование всех чисел из него происходит с помощью генератора
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        for el in caе_companies_finance(file_obj):
            income = el[1] - el[2]
            final_dict[el[0]] = income
            total_income += income if income > 0 else 0
            total_quntity += 1 if income > 0 else 0
            print(el[0], income, total_income, total_quntity)

    print(f'{final_dict}')
    final_list = [final_dict, {"average_profit": total_income / total_quntity if total_quntity != 0 else 1}]
    print(f'{final_list}')

    with open(new_ile_name, 'w', encoding='utf-8') as file_obj:
        json.dump(final_list, file_obj)
