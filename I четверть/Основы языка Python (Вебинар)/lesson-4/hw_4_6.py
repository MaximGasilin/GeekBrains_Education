# Задание # 6
#
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


# Скрипт а). Вынесен в отдельную функцию
def script_a(begin=3, end=10):
    for el in count(begin):
        if el > end:
            break
        else:
            yield el


# Скрипт б). Вынесен в отдельную функцию
def script_b(value_list=None, quantity=5):
    if value_list is None:
        value_list = []
    counter = 1
    for el in cycle(value_list):
        if counter > quantity:
            break
        counter += 1
        yield el


if __name__ == '__main__':

    iter_a = script_a(16, 25)
    print(iter_a)
    for i in iter_a:
        print(i)
    print("Iteration 'A' done.")

    iter_b = script_b(['N', 'a', 't', 'a', 's', 'a'], 15)
    print(iter_b)
    for i in iter_b:
        print(i)
    print("Iteration 'B' done.")
