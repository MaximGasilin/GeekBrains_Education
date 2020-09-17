# Задание # 4
#
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4

from random import randint
import re


mapping_int_to_word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                       9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                       15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                       30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
                       100: 'hundred', 0: ''}

file_name = 'lesson_5_task_4_int_list.txt'
count_of_lines = 5

with open(file_name, 'w', encoding='utf-8') as file_obj:
    for el in range(count_of_lines):
        # rand_int = randint(1, 100)
        rand_int = randint(1, 9)
        if rand_int < 21 or rand_int == 100:
            # rand_str = mapping_int_to_word[rand_int] # Choose this code, if you want generate numbers from 1 to 100
            rand_str = mapping_int_to_word[rand_int]
        else:
            rand_ten, rand_digit = divmod(rand_int, 10)
            rand_str = f'{mapping_int_to_word[rand_ten * 10]} {mapping_int_to_word[rand_digit]}'
        print(f'{rand_str.capitalize()} - {rand_int}', file=file_obj)
