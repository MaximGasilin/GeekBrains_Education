'''
Задание # 5

Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет
добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких
чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого
завершить программу.
'''

def f_convert_str(str_var):
    try:
        var_f = float(str_var)
    except ValueError:
        var_f = None

    return var_f

def f_processing_entering_string(str_var):
    result = 0
    stop_flag = False

    list_var = str_var.split()
    for var in list_var:
        convert_var = f_convert_str(var)
        if convert_var == None:
            stop_flag = True
            break
        result += convert_var

    return result, stop_flag

summ_itogo = 0

print('Прошу вводить несколько чисел, разделенных пробелами. Enter - окончание ввода')
print('Ввод любого текста, не являющегося числом остановит выполнение программы')

stop_flag = False
while not stop_flag:
    str_var = input('-->>')
    current_sum, stop_flag = f_processing_entering_string(str_var)

    summ_itogo += current_sum

    print(f'Текущий результат суммирования всех введенных чисел: {summ_itogo}')