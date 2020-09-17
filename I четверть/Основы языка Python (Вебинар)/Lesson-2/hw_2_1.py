'''
Задача #1
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

my_list = [10, 29878546547780, 25.33, 'Строка', None, [12, None, 'abc'], False, complex(5, 6), b'text', (1, 'cde', None), {'1' : 'a', '2' : 'b'}, set([15, False, 'xyz']), bytearray(b'some text')]
print('Созданный список:', my_list, end = '\n\n')

'''
# Объединятются в кортежи элементы 3-х списков
# 1) Список человеческих названий типов. Вытащенный из словаря my_list_type_names для элементов списка my_list
# 2) Просто список описаний типов для элементов списка my_list
# 3) Сами элементы списка  my_list
# А затем это все печатается с помощью функции list(map(....
'''

my_list_type_names = {None : "пустое значение", str : "строка", int : "целое число",
    float : "число с плавающей точкой", complex : "комплексное число",
    bool : "булевая переменная",  bytes : "битовое значение",
    list : "список", set :  "множество", tuple :  "кортеж", dict :  "словарь"}

list(map(print, list(zip(list(map(lambda x: (my_list_type_names.get((type(x), None)[x is None]), 'ерунда какя-то')[my_list_type_names.get((type(x), None)[x is None]) is None], my_list)), list(map(type, my_list)), my_list))))

'''
Понимаю, что выглядит нечитаемо, но, на мой взгляд (хотя я могу ошибаться) это как раз решение в духе стиля Python 
для тех, ктопока не знает, что такое - функция.

Чтобы было понятно, что я разобрался с заданием, вот еще один пример решения:

# Первый вариант.
list(map(print, list(zip(list(map(type, my_list)), my_list))))

или вот

# Второй вариант. Со вставками человеческого языка.
count = 0
for el in my_list:
    type_custom_name = 'ерунда какя-то'
    if el is None:
        type_custom_name = "пустое значение"
    elif type(el) is str:
        type_custom_name = "строка"
    elif type(el) is int:
        type_custom_name = "целое число"
    elif type(el) is float:
        type_custom_name = "число с плавающей точкой"
    elif type(el) is complex:
        type_custom_name = "комплексное число"
    elif type(el) is bool:
        type_custom_name = "булевая переменная"
    elif type(el) is bytes:
        type_custom_name = "битовое значение"
    elif type(el) is list:
        type_custom_name = "список"
    elif type(el) is set:
        type_custom_name = "множество"
    elif type(el) is tuple:
        type_custom_name = "кортеж"
    elif type(el) is dict:
        type_custom_name = "словарь"

    print(f'{count}) {type_custom_name}: {el}')
    count += 1
'''