# Задание # 2
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class MyZeroDevException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':

    try:
        dividend = float(input('Введите делимое: '))
        divider = float(input('Введите делитель: '))
        if divider == 0:
            raise MyZeroDevException('Ошибка! Исключение! В качестве делитля был указан 0.')
        print(dividend / divider)
    except MyZeroDevException as mzde:
        print(mzde)
    except ValueError as ve:
        print(ve)
    except Exception as ex:
        print(ex)
    finally:
        print('Программа завершает свое выполнение. До новых встреч.')
