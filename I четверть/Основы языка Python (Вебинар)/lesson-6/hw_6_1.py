# Задание # 1
#
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
#                                                                                              красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

# Для решения задачи с контролем понадобилось добавить в класс:
# переменные:
# 1) Последовательность переключени
# 2) Текущий индекс в последовательности
#
# Фунции:
# 1) __get_next_switching_characteristics - определить следующие характеристики переключения: цвет, время включения
# 2) __switch_and_control - получает характеристики следующего включения. Запускает переключение и контролирует
# корректность этого переключения. Так же передает в процедуру running информацию о том, сколько времени не переключать.
# 3) __switch_color - собсвенно переключение светофора.
#
# В функцию переключения пришлось включить возможность ошибки. Специально, чтобы спровоцировать ошибочные действия.

from time import sleep
from random import randint
from datetime import datetime
from itertools import cycle


class TrafficLight:
    '''
    Концепция реализации следующая:
    1. Метод running() в классе запускает процесс переключения световфора
    2. Метод __switch_and_control() - определяет, какой цвет должен быть следующим, и после включения цвета
        проверяет, что включившийся совпадает с тем, что должен был включиться.
    3. Метод __switch_color() - осуществляет переключение на указанный цвет. При этом внутри есть специальный код,
        который по псевдослучайному числу переключает на желтый цвет. Типа сбой в механизме...
    '''
    def __init__(self):
        self.__color = None
        self.__color_mapping = {'red': 1, 'green': 2, 'yellow': 3}
        self.__get_next_switching_characteristics = cycle([('red', 7), ('yellow', 2), ('green', 7)])

    def __switch_color(self, next_color):
        now = datetime.now()
        self.__color = next_color if randint(1, 30) != 13 else 'yellow'  # Имитация ошибки переключения
        print(f'{now.strftime("%H:%M:%S")}:\033[9{self.__color_mapping.get(self.__color)}m {self.__color}\033[00m')

    def __switch_and_control(self):
        next_switch_char = next(self.__get_next_switching_characteristics)
        self.__switch_color(next_switch_char[0])
        if self.__color != next_switch_char[0]:
            self.__color = None
            now = datetime.now()
            print(f'{now.strftime("%H:%M:%S")}:Внимание, произошло не корректное переключение.')
            result = None
        else:
            result = next_switch_char[1]
        return result

    def running(self):
        while True:
            pause_length = self.__switch_and_control()
            if pause_length is None:
                break
            else:
                sleep(pause_length)
        else:
            print(f'{self.__color}')


if __name__ == '__main__':

    trafficLight_1 = TrafficLight()
    trafficLight_1.running()

# Чтобы доказать, что я реализовал этот же класс, но в простом варианте, привожу реализацию
# from time import sleep
# 
#
# class TrafficLight:
#
#     def __init__(self):
#         __color = None
#
#     def running(self, loop_count):
#         while loop_count > 0:
#             self.__color = 'red'
#             print("\033[91m {}\033[00m" .format(self.__color))
#
#             sleep(7)
#             self.__color = 'yellow'
#             print("\033[93m {}\033[00m" .format(self.__color))
#
#             sleep(2)
#             self.__color = 'green'
#             print("\033[92m {}\033[00m" .format(self.__color))
#
#             sleep(7)
#             loop_count -= 1
#         else:
#             self.__color = None
#             print(f'{self.__color}')
#
#
# if __name__ == '__main__':
#
#     trafficLight_1 = TrafficLight()
#     trafficLight_1.running(2)
