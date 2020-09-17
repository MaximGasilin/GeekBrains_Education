# Задание # 3
#
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

# file_name = 'lesson_5_task_3_salary_list.txt'
file_name = input('Введите пожалуйста файл из которого нужно прочитать данные: ')

loser_limit = 20000

losers_count = 0
total_count = 0
losers_sum = 0
total_sum = 0

with open(file_name, 'r', encoding='utf-8') as file_obj:
    for line_in_file in file_obj:
        line_to_list = line_in_file.split()
        try:
            current_salary = float(line_to_list[1])
        except ValueError:
            current_salary = 0

        if current_salary < loser_limit:
            print(f'{line_to_list[0]} '
                  f'{("", f" - зарплата не определена, считаем, что меньше {loser_limit}")[current_salary == 0]}')
            losers_sum += current_salary
            losers_count += 1
        total_sum += current_salary
        total_count += 1

print(f'В файле {file_name} средняя зарплата = '
      f'{total_sum / (total_count, 1)[total_count == 0]} ({total_sum} / {total_count})')
print(f'В файле {file_name} средняя зарплата меньше '
      f'{loser_limit} = {losers_sum / (losers_count, 1)[losers_count == 0]} ({losers_sum} / {losers_count})')
