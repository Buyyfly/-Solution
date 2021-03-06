# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
# метода.
# Например: 20м*5000м*25кг*5см = 12500


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def raschet(self):
        return self._length * self._width * 25 * 5  # Согласно заданию вводим 2 атрибута, остальные просто возьмем из
        # примера


try:
    ch = Road(int(input('Введите длину: ')), int(input('Введите ширину: ')))
    print(ch.raschet())
except ValueError as e:
    print('Не корректный ввод.')
