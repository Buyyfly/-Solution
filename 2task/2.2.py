# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

try:
    quantity = int(input('Введите кол-во элементов списка: '))
    s = list()
    i = 0
    while i < quantity:
        s.append(input(f'Введите значение {i + 1} элемента списка: '))
        i += 1

    i = 0
    for el in range(int(len(s) / 2)):
        s[i], s[i + 1] = s[i + 1], s[i]
        i += 2
    print(s)

except ValueError as error:
    print('Введенное значение не относится к типу int.')




