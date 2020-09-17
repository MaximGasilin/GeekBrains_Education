# Задание # 1
#
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
# типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

from calendar import monthrange


class MyDate():
    src_value = ''
    dd = 0
    mm = 0
    yyyy = 0

    def __init__(self, src_value):
        self.src_value = src_value

    @classmethod
    def parsing_src(cls):
        temp_list = cls.src_value.split('-')
        try:
            cls.dd = int(temp_list[0])
            cls.mm = int(temp_list[1])
            cls.yyyy = int(temp_list[2])
        except ValueError:
            print('Дата задана неверно!')
        # print(cls.dd, cls.mm, cls.yyyy)

    @staticmethod
    def maximum_days_in_month_count(m, y):
        result = 28 + ((m + m // 8) % 2) + 2 % m + (
                1 + (1 - (y % 4 + 2) % (y % 4 + 1)) * ((y % 100 + 2) % (y % 100 + 1)) + (
                1 - (y % 400 + 2) % (y % 400 + 1))) // m + 1 // m - (((1 - (y % 4 + 2) % (y % 4 + 1)) * (
                (y % 100 + 2) % (y % 100 + 1)) + (1 - (y % 400 + 2) % (y % 400 + 1))) // m)
        return result

    @staticmethod
    def validate_date(dd, mm, yyyy):
        if not (1 <= mm <= 12):
            print(f'Расчет по формуле: Значение месяца указано неверно. Значение должно быть от 1 до 12')
            return None

        dd_value = MyDate.maximum_days_in_month_count(mm, yyyy)
        '''
        Расчет количества дней в месяце производится по ужасной на вид формуле
        описанной в функции maximum_days_in_month_count. Не смотря на громздкость
        этот метод мне нравится больше всех. Т.к. выдает творческое начало и
        алалитически-математический подход.
        '''

        if not (1 <= dd <= dd_value):
            print(f'Расчет по формуле: Число указано неверно. Значение должно быть от 1 до {dd_value}')
            return None

        print('Расчет по формуле: Дата задана корректно!')

    @staticmethod
    def validate_date_2(dd, mm, yyyy):
        if not (1 <= mm <= 12):
            print(f'Через модуль calendar: Значение месяца указано неверно. Значение должно быть от 1 до 12')
            return None

        '''
        Расчет количества дней в месяце производится по встроенной в
        модуль calendar функции monthrange. Хоть это и круто, эффективно и
        наглядно. Но как оно реализовано внутри - не понятно. Потенциальные
        риски. Хоть и минимальные, конечно.
        '''
        if not (1 <= dd <= monthrange(yyyy, mm)[1]):
            print(
                f'Через модуль calendar:Число указано неверно. Значение должно быть от 1 до {monthrange(yyyy, mm)[1]}')
            return None

        print('Через модуль calendar: Дата задана корректно!')

    @staticmethod
    def validate_date_3(dd, mm, yyyy):
        if not (1 <= mm <= 12):
            print(f'Расчет через if..else: Значение месяца указано неверно. Значение должно быть от 1 до 12')
            return None

        '''
        Расчет количества дней в месяце производится с помощью оператора
        if..else. Не очень эстетично, но дешево, надежно, практично...
        '''
        if mm in (1, 3, 5, 7, 8, 10, 12):
            date_max_value = 31
        elif mm in (4, 6, 9, 11):
            date_max_value = 30
        elif mm == 2 and yyyy % 400 == 0:
            date_max_value = 29
        elif mm == 2 and yyyy % 100 == 0:
            date_max_value = 28
        elif mm == 2 and yyyy % 4 == 0:
            date_max_value = 29
        elif mm == 2:
            date_max_value = 28
        else:
            date_max_value = 0

        if not (1 <= dd <= date_max_value):
            print(f'Расчет через if..else: Число указано неверно. Значение должно быть от 1 до {date_max_value}')
            return None

        print('Расчет через if..else: Дата задана корректно!')


if __name__ == '__main__':
    print('-' * 60)

    MyDate.src_value = '29-2-2000'
    print(MyDate.src_value)
    MyDate.parsing_src()
    MyDate.validate_date(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_2(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_3(MyDate.dd, MyDate.mm, MyDate.yyyy)
    print()

    MyDate.src_value = '29-2-2100'
    print(MyDate.src_value)
    MyDate.parsing_src()
    MyDate.validate_date(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_2(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_3(MyDate.dd, MyDate.mm, MyDate.yyyy)
    print()

    MyDate.src_value = '17-04-1979'
    print(MyDate.src_value)
    MyDate.parsing_src()
    MyDate.validate_date(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_2(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_3(MyDate.dd, MyDate.mm, MyDate.yyyy)
    print()

    MyDate.src_value = '27-05-2020'
    print(MyDate.src_value)
    MyDate.parsing_src()
    MyDate.validate_date(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_2(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_3(MyDate.dd, MyDate.mm, MyDate.yyyy)
    print()

    MyDate.src_value = '25-12-2012'
    print(MyDate.src_value)
    MyDate.parsing_src()
    MyDate.validate_date(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_2(MyDate.dd, MyDate.mm, MyDate.yyyy)
    MyDate.validate_date_3(MyDate.dd, MyDate.mm, MyDate.yyyy)
    print()

    MyDate.src_value = '25-12-Двадцатого'
    print(MyDate.src_value)
    MyDate.parsing_src()
    print()
