# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
# элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

a = [1, 1.03, 'test', None, 'text', ]
for i in a:
    print(f'{i} - {type(i)}')