# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехела'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        return f'Поворот на {direction}'

    def show_speed(self):
        return f'speed = {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости на {self.speed - 60}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости на {self.speed - 40}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


car = Car(0, 'green', 'test')
print(car.go())
car = TownCar(int(input('Введите скорость: ')), 'green', 'test')
print(car.show_speed())
print(car.stop())
