# Задание # 4
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

mapping_eng_to_rus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                      'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'eleven': 'одиннадцать',
                      'twelve': 'двенадцать', 'thirteen': 'тринадцать', 'fourteen': 'четырнадцать',
                      'fifteen': 'пятнадцать', 'sixteen': 'шестнадцать', 'seventeen': 'семнадцать',
                      'eighteen': 'восемнадцать', 'nineteen': 'девятнадцать', 'twenty': 'двадцать',
                      'thirty': 'тридцать', 'forty': 'сорок', 'fifty': 'пятьдесят', 'sixty': 'шестьдесят',
                      'seventy': 'семдесят', 'eighty': 'восемдесят', 'ninety': 'девяносто', 'hundred': 'сто'}


def replace_eng_to_rus(str_var):

    # Я посчитал, что в данном случае использование глобальнй переменной оправданно. Незачем ее заводить каждый раз.
    global mapping_eng_to_rus

    str_list = str_var.lower().split()
    str_list = list(map(lambda el: (mapping_eng_to_rus.get(el), el)[mapping_eng_to_rus.get(el) is None], str_list))

    return ' '.join(str_list).capitalize()


# file_name = 'lesson_5_task_4_int_list.txt'
file_name = input(f'Введите имя файла, из которого нужно считать данные: ')
new_file_name = file_name.replace('.', '_rus.')
new_file_name = (new_file_name, f'{file_name}_rus')[new_file_name == file_name]

with open(file_name, 'r', encoding='utf-8') as file_obj:
    with open(new_file_name, 'w', encoding='utf-8') as new_file_obj:
        for line_in_file in file_obj:
            new_line = replace_eng_to_rus(line_in_file)
            print(f'{new_line}', file=new_file_obj)
