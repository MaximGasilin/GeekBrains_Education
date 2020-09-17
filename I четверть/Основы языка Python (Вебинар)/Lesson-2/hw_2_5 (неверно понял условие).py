'''
Задание # 5 (переврал условие)
Реализовать структуру « Рейтинг », представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3 , 2.
Пользователь ввел число 8. Результат: 8 , 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1 .
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

# Для первого способа понадосится прикольная функция reduce, а для этого нужно подключить модуль functools
from functools import reduce

my_list_templite = [7, 5, 3, 3, 2]
my_list_templite.sort()
my_list = my_list_templite


print(f'Исходый список: {my_list}')

print('Введите пожалуйста натуральное число (для выхода просто нажмите Enter)')
while True:
    str_var = input('(Для выхода просто нажмите Enter) -->')
    if str_var == '':
        break

    # Проверки на корректность введенной информации
    try:
        int_var = int(str_var)
    except ValueError:
        int_var = 0

    if int_var < 1:
        print('С точки зрения математики то что Вы ввели не является натуральным числом. Попробуйте еще раз. У вас получится...')
        continue

    # Cобственно, алгоритм решения самой задачи

    # Первый способ. С помощью метода Reduce
    my_list = my_list_templite.copy()

    my_list = [x for x in my_list if x <= int_var] + [int_var] + [x for x in my_list if x > int_var]

    print(f'{my_list} - первым способом')

    # Второй способ. С помощью методов списков
    my_list = my_list_templite.copy()

    my_list = [1] + my_list
    target_pos = reduce(lambda x, y: x + (0, 1)[y <= int_var], my_list)
    my_list.insert(target_pos, int_var)
    my_list.pop(0)

    print(f'{my_list} - вторым способом')

    # трктий способ
    my_list = my_list_templite.copy()

    # Далее получим список вида [False, False, False, False, TRUE, True, True] Перед TRUE и нужно вставить значение
    bin_list = list(map(lambda x: x > int_var, my_list))
    try:
        target_pos = bin_list.index(True)
    except ValueError:
        target_pos = len(my_list)
    my_list.insert(target_pos, int_var)

    print(f'{my_list} - третьим способом')
    print('\n')

    my_list_templite = my_list