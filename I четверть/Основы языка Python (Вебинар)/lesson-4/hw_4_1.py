
# Задание # 1
#
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv, exit


def f_salary_count(p_production, p_bid, p_award):
    return p_production * p_bid + p_award


script_name, param_1, param_2, param_3 = None, None, None, None
try:
    script_name, param_1, param_2, param_3 = argv
except ValueError:
    print('Неверно заполнены аргументы скрипта')
    exit()

try:
    production = float(param_1)
except ValueError:
    print('Неверно задана выработка (параметр ё). Будет 0')
    production = 0

try:
    bid = float(param_2)
except ValueError:
    print('Неверно задана часовая ставка (параметр 2). Будет 0')
    bid = 0

try:
    award = float(param_3)
except ValueError:
    print('Неверно задана премия (параметр 3). Будет 0')
    award = 0

print(f'{f_salary_count(production, bid, award):.2f}')
