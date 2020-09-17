# Задание # 5
#
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'Началась рисование тонкими чернилами.')


class Pencil(Stationery):
    def draw(self):
        print(f'Запустилось черчение карандашом.')


class Handle(Stationery):
    def draw(self):
        print(f'На холсте отражается жирная линия маркером.')


if __name__ == '__main__':

    instrument_1 = Stationery('Неопределнный инструмент')
    instrument_2 = Pen('Ручка')
    instrument_3 = Pencil('Карандаш')
    instrument_4 = Handle('Маркер')

    for el in (instrument_1, instrument_2, instrument_3, instrument_4):
        print(el.__dict__)
        el.draw()
        print()
