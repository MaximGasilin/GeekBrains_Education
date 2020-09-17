'''
# 4
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
try:
    entering_int_var = int(input("Введите пожалуйста целое положительное число: "))
except ValueError:
    print('Число введено неверно. Будет заменено на 0.')
    entering_int_var = 0

if entering_int_var < 0:
    print('Число введено неверно. Будет заменено на 0.')
    entering_int_var = 0

max_figure = 0

while entering_int_var > 0 and max_figure < 9:
    current_figure = entering_int_var % 10
    entering_int_var = entering_int_var // 10
#    print(f"цифра: {current_figure}, число: {entering_int_var}") отладка алгоритма

    max_figure = max(current_figure, max_figure)

print(f"Максимальная цифра: {max_figure}")

