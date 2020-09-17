# Задание # 4
#
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, i s_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
# вызвать методы экземпляров).

from random import randint


class Car:
    def __init__(self, color, name, is_police=False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = randint(10, 100)
        print(f'{self.name} ({self.color}) начал движение')

    def stop(self):
        self.speed = 0
        print(f'{self.name} ({self.color}) остановился')

    def turn(self, direction):
        print(f'{self.name} ({self.color}) изменил направление на {direction}')

    def show_speed(self):
        print(f'{self.name} ({self.color}) движется со скоростью {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение!')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, color, name):
        super().__init__(color, name, True)


if __name__ == '__main__':

    car_1 = SportCar('red', 'Ferrari')
    car_2 = WorkCar('yellow', 'Ford-taxi')
    car_3 = TownCar('white', 'Mitsubishi')
    car_4 = PoliceCar('BlackAndWhite', 'Lada-police')

    car_1.go()
    car_1.show_speed()
    car_1.turn('на право')
    car_1.turn('на лево')
    car_1.stop()
    car_1.show_speed()
    print()

    car_2.go()
    car_2.show_speed()
    car_2.turn('на право')
    car_2.turn('на лево')
    car_2.turn('на лево')
    car_2.stop()
    car_2.show_speed()
    print()

    car_3.go()
    car_3.show_speed()
    car_3.turn('на право')
    car_3.turn('на право')
    car_3.stop()
    car_3.show_speed()
    print()

    car_4.go()
    car_4.show_speed()
    car_4.turn('на право')
    car_4.turn('на лево')
    car_4.turn('на право')
    car_4.turn('на лево')
    car_4.stop()
    car_4.show_speed()
