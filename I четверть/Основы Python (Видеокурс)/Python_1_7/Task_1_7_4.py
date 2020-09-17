# Задание # 4
#
# Написать функцию которая принимает на вход число от 1 до 100. Если число равно 13,
# функция поднимает исключительную ситуации ValueError иначе возвращает введенное число, возведенное в квадрат.
# Далее написать основной код программы. Пользователь вводит число.
# Введенное число передаем параметром в написанную функцию и печатаем результат, который вернула функция.
# Обработать возможность возникновения исключительной ситуации, которая поднимается внутри функции.


def processing_value(source):
    if source == 13:
        raise Exception('Это страшное число!')
    else:
        return source * source


def processing_value(source):
    if source == 13:
        raise ValueError('Это страшное число!')
    else:
        return source * source


while True:
    try:
        src = int(input('Введите число: '))
    except ValueError:
        break

    try:
        print(processing_value(src))
    except Exception as e:
        print(e)


