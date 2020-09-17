'''
Задание # 2

Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.
'''

def f_concatinate_and_print(par_name, par_surname, par_age, par_place, par_email, par_phone):
    print(f'{par_name} {par_surname}, {par_age} года рождения, проживает в городе {par_place}, e-mail: {par_email},'
          f' phone: {par_phone}.')

var_name  = input('Имя: ')
var_surname  = input('Фамилия: ')
var_age   = input('Год рождения: ')
var_place = input('Город проживания: ')
var_email = input('e-mail: ')
var_phone = input('Телефон: ')

f_concatinate_and_print(par_email = var_email, par_phone = var_phone, par_name = var_name, par_surname = var_surname,
                    par_age = var_age, par_place = var_place)

