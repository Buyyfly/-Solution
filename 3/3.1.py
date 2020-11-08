# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def calculate(chas, deli):
    try:
        return chas / deli
    except ZeroDivisionError:
        print('Делить на 0 нельзя')


# Сразу поеясним какой ввод что означает и введем првоверку на тип
try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    print(f'Частное: {calculate(a, b)}') if calculate(a, b) is not None else ''
except ValueError:
    print("Ошибка ввода")
