'''
# 3
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''
try:
    entering_int_var = int(input("Введите пожалуйста любую цифру от 0 до 9: "))
except ValueError:
    print('Число введено неверно. Будет заменено на 0.')
    entering_int_var = 0

if entering_int_var < 0 or entering_int_var > 9:
    print('Число введено неверно. Будет заменено на 0.')
    entering_int_var = 0

result = 3 * entering_int_var + 2 * entering_int_var * 10 +  entering_int_var * 100

print(f"Вычисление формулы n+nn+nnn: {result}")