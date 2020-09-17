'''
Задание # 3

Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
'''

def f_my_power(base, power):
    base__power = 1
    for count in range(power*(-1)):
        base__power *= base
    return 1 / base__power


try:
    var_1 = float(input('Введите действительное положительное: '))
except ValueError:
    print('Должно быть число! По умолчанию подставлена 1')
    var_1 = 1

try:
    var_2 = int(input('Введите целое отрицательное число: '))
    if var_2 > 0:
        print('Число должно быть отрицательным. Поставим минус за Вас')
        var_2 = 0 - var_2
    elif var_2 == 0:
        print('0 не подходит. Подставим -1')
        var_2 = -1
except ValueError:
    print('целое отрицательное число. А вы ввели что-то друге. Подставим вместо Вас -1')
    var_2 = -1


print(f'Результат работы моей функции: {f_my_power(var_1, var_2)}')
print(f'Результат работы системной функции python: {var_1**var_2}. Для визуальной проверки результата')
