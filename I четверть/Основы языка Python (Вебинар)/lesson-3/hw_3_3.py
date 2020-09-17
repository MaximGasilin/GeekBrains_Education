'''
Задание # 3

Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
'''

def f_max_2_from_3(var_1, var_2, var_3):
    return var_1 + var_2 + var_3 - min(var_1, var_2, var_3)

my_vars = []

for count in range(3):
    try:
        var = float(input(f'Введите число # {count+1}: '))
    except ValueError:
        print('Должно быть число! По умолчанию подставлена 1')
        var = 1

    my_vars.append(var)

print(f'{f_max_2_from_3(my_vars[0], my_vars[1], my_vars[2])}')
