# Задание # 3
#
# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


if __name__ == '__main__':

    position_1 = Position('Stephen', 'King', 'writer', {'wage': 100000, 'bonus': 1000000})
    position_2 = Position('Elton', 'John', 'singer', {'wage': 150000, 'bonus': 1500000})
    position_3 = Position('Karl', 'Marks', 'Philosopher', {'wage': 2000, 'bonus': 1000})

    for el in (position_1, position_2, position_3):
        print(el.__dict__)
        print(el.get_full_name())
        print(el.get_total_income())
