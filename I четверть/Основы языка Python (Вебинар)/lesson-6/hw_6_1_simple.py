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

from time import sleep


class TrafficLight:

    def __init__(self):
        __color = None

    def running(self, loop_count):
        while loop_count > 0:
            self.__color = 'red'
            print("\033[91m {}\033[00m" .format(self.__color))

            sleep(7)
            self.__color = 'yellow'
            print("\033[93m {}\033[00m" .format(self.__color))

            sleep(2)
            self.__color = 'green'
            print("\033[92m {}\033[00m" .format(self.__color))

            sleep(7)
            loop_count -= 1
        else:
            self.__color = None
            print(f'{self.__color}')


if __name__ == '__main__':

    trafficLight_1 = TrafficLight()
    trafficLight_1.running(2)
