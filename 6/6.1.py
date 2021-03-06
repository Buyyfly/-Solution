# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.


from itertools import cycle
from time import sleep


class TrafficLight:
    __color = 'red'
    __all_time = 0

    def running(self):
        for i in cycle([('red', 7), ('yellow', 2), ('green', 4), ('yellow', 2)]):  # Добавим в конец еще желтый как у
            # настроящего светофора
            self.__color = i[0]
            print(self.__color)
            sleep(i[1])
            self.__all_time += i[1]
            # Сделаем проверку чтобы программа завершалась после 60 секунд выполнения.
            # Согласно данным она должна 4 раза вывести значения.
            if self.__all_time >= 60:
                break


a = TrafficLight()
a.running()
