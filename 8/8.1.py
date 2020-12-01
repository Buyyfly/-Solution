# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

from time import strptime


class Data:
    ls = []

    def __init__(self, ls):
        Data.ls = ls.split('-')

    @classmethod
    def f_class(cls):
        try:
            print([int(i) for i in cls.ls])
        except ValueError:
            print('Введена не корректная дата')

    @staticmethod
    def stat(vvod):
        try:
            ch = strptime(vvod, '%d-%m-%Y')
            print(f'День:{ch.tm_mday} месяц:{ch.tm_mon} год:{ch.tm_year}')
        except ValueError:
            print('Введена не корректная дата')


v = input('Введите дату в формате "день-месяц-год"\n')
m = Data(v)
m.f_class()
Data.stat(v)
