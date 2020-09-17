'''
Задание # 5
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

my_list = [7, 5, 3, 3, 2]
my_list.sort(reverse = True)

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

    my_list = [x for x in my_list if x >= int_var] + [int_var] + [x for x in my_list if x < int_var]

    print(f'{my_list}')

    # Подготовка к следующиему шагу ввода и обработки информации
    print('\n')

'''
Не мог не описать другие варианты, которые я попробовал, проверил, проработал. 
Но не стал включать в основной код по просьбе преподавателя.

А они все мне показались интересными. Поэтому напишу их в комментарии.
Чтобы доказать, что в теме разобрался.
И, кстати говоря, получил очень-очень-очень много удовольствия.

# Второй вариант

    from functools import reduce
    my_list = [1] + my_list
    target_pos = reduce(lambda x, y: x + (0, 1)[y >= int_var], my_list)
    my_list.insert(target_pos, int_var)
    my_list.pop(0)

# Третий вариант

    # Получим список вида [False, False, False, False, TRUE, True, True] Перед TRUE и нужно вставить значение
    bin_list = list(map(lambda x: x < int_var, my_list))
    try:
        target_pos = bin_list.index(True)
    except ValueError:
        target_pos = len(my_list)
    my_list.insert(target_pos, int_var)
'''