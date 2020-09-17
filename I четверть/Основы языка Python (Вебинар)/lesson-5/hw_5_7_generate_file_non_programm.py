# Задание # 7
#
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

from random import randint

list_of_companies = ['Ромашка', 'Рога и копыта', 'Лютик', 'МММ', 'Хопер', 'Мойдодыр', 'Стртап плюс',
                     'Новая стратегия', 'Лекс', 'Гранд тур', 'Стратосфера', 'Космос-Энергия', 'Бомж лтд']

list_of_org_forms = ('ООО', 'ПАО')

file_name = 'lesson_5_task_7_list_of_companies.txt'

with open(file_name, 'w', encoding='utf-8') as file_obj:
    for el in list_of_companies:
        revenue = randint(90000, 100000)
        cost = randint(70000, 120000)
        form_index = randint(0, 1)
        print(f'{el} {list_of_org_forms[form_index]} {revenue} {cost}', file=file_obj)
