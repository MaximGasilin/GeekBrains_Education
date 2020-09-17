# Задание # 2
#
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

# file_name = 'lesson_5_task_2_text.txt'
file_name = input('Введите пожалуйста файл из которого нужно прочитать данные: ')

lines_count = 0
words_count = 0

with open(file_name, 'r', encoding='utf-8') as file_obj:
    for line_in_file in file_obj:
        lines_count += 1
        words_count += len(line_in_file.split())

print(f'В файле {file_name} насчитывается {lines_count} строк(-и, -а) и {words_count} слов(-ово) и знаков пунктуации.')
