'''
# 1
Поработайте с переменными, создайте несколько, выведите на экран, запросите у
пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

int_var = 5
float_var = 3.1415926575987
str_var = 'Hello world!'
bool_var = True
list_var = [2, 2.4, 'Hello']
tuple_var = [9, 9.7, 'Hasta la Vista']
dict_var = {"name": "Вася", "age": 15, "sex": "male", "cool": True}

print(int_var, float_var, str_var, bool_var, list_var, tuple_var, dict_var, sep='\n===\n')

try:
    entering_int_var = int(input("Введите пожалуйста любое целое число: "))
except ValueError:
    entering_int_var = "Совсем не то, что Вас просили"
print(f"Вы указали '{entering_int_var}'")

try:
    entering_float_var = float(input("Введите пожалуйста любое дробное число: "))
except ValueError:
    entering_float_var = "Совсем не то, что Вас просили"
print(f"Вы указали '{entering_float_var}'")

entering_name = input("Введите пожалуйста свое имя: ")
print(f"Вы указали '{entering_name}'")
