# Задание #2
#
# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма) . Это могут быть обычные числа: V и H , соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5) , для костюма (2*H + 0.3) .
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property .

from abc import ABC, abstractmethod
from functools import reduce


class Clothes(ABC):
    c_name = ''
    c_type = ''

    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return f'{self.c_type}: {self.c_name}'


class Coat(Clothes):
    def __init__(self, name, size=0):
        self.c_name = name
        self.c_size = size
        self.c_type = 'Пальто'

    @property
    def consumption(self):
        return self.c_size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height=0):
        self.c_name = name
        self.c_height = height
        self.c_type = 'Костюм'

    @property
    def consumption(self):
        return self.c_height * 2 + 0.3


list_of_clothes = []

list_of_clothes.append(Coat("№ 1", 50))
list_of_clothes.append(Coat("№ 2", 52))
list_of_clothes.append(Coat("№ 3", 48))
list_of_clothes.append(Coat("№ 4", 54))

list_of_clothes.append(Suit("№ 1", 1))
list_of_clothes.append(Suit("№ 2", 1.2))
list_of_clothes.append(Suit("№ 3", 0.8))
list_of_clothes.append(Suit("№ 4", 0.9))

list(map(print, list_of_clothes))
fabric_value = reduce(lambda x, y: x + y.consumption, list_of_clothes, 0)  # Обращение к consumption как к атрибуту.

print(f'Общее количество ткани, требуемое для пошива одежды из списака: {fabric_value}')