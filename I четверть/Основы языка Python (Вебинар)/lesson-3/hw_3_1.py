'''
Задание # 1

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
'''

def f_division(dividend, divider):
    try:
        result = dividend / divider
    except:
        result = None
    return result

try:
    var_1 = float(input('Первое число (делимое): '))
except ValueError:
    print('Должно быть число! По умолчанию подставлена 1')
    var_1 = 1

try:
    var_2 = float(input('Второе число (делитель): '))
except ValueError:
    print('Должно быть число! По умолчанию подставлена 1')
    var_2 = 1

print(f'{f_division(var_1, var_2)}')
