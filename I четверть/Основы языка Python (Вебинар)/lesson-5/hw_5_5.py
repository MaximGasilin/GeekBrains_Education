# Задание # 5
#
# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


def cat_numbers(file_object):
    # Генератор, который считыват "слова" разделенные пробелами и, преобразовав их в числа, передает во внешний код.

    str_var = ''
    eof = False
    while not eof:
        symbol = file_object.read(1)

        if symbol == '':
            symbol = ' '
            eof = True
            if str_var == '':
                break

        if symbol != ' ':
            str_var = str_var + symbol
        else:
            try:
                current_number = float(str_var)
            except ValueError:
                current_number = 0

            str_var = ''

            yield current_number


if __name__ == '__main__':

    # file_name = 'lesson_5_task_5_temporary_file.txt'
    file_name = input(f'Введите имя файла, в котором будут записаны числа: ')

    quantity = randint(10, 100)
    numbers_sum = 0
    numbers_count = 0

    # Программное создание и запись файла с числами
    with open(file_name, 'w', encoding='utf-8') as file_obj:
        for el in range(quantity):
            print(f'{randint(1000, 350000)/100}', file=file_obj, end=' ')

    # Чтение файла и суммирование всех чисел из него происходит с помощью генератора
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        for curr_number in cat_numbers(file_obj):
            numbers_sum += curr_number
            numbers_count += 1
            print(f'{numbers_count}) {curr_number}. А сумма стала равной:  {numbers_sum}')

    print()
    print(f'Сумма всех ({numbers_count} штук(-и, -а)) равна {numbers_sum}')

