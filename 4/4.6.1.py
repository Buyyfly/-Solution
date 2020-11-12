# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
# условие его завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
# прекращено

# Решение А
from itertools import count
from sys import argv
# Запросим у пользователя 2 параметра.
# 1 число с которого начинается вывод;
# 2 кол-во выводимых чисел от первого параметра (включая его)
script_name, ch, i = argv
try:
    ch = int(ch)
    for el in count(ch):
        if el > ch + (int(i) - 1):
            break
        else:
            print(el)
    print(f'Завершение работы. Программа вывела {i} чисел.')
except ValueError:
    print("Не корректный ввод параметра, число должно быть целым.")

