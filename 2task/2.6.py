# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (
# характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

sp = int(input('Введите кол-во позиций: '))
structure = dict(Наименование='', Цена='', Количество='', Ед='')

il = 1
ls = list()
while il <= sp:
    for i in structure:
        structure[i] = input(f'Позиция №{il}. Введите параметр {i}: ')
    kor = (il, structure)
    ls.append(kor)
    il += 1
print(ls)

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

out = dict()
for i in structure:
    v_out = list()
    for el in ls:
        v_out.append(el[1][i])
    out[i] = v_out

print(f'--//--//--\n{out}')


# 2е решения для ввода данных где не известно на старте сколько будет позиций
structure = dict(Наименование='', Цена='', Количество='', Ед='')
if1 = True
il = 1
ls = list()
while if1:
    for i in structure:
        structure[i] = input(f'Позиция №{il}. Введите параметр {i}: ')
    kor = (il, structure)
    ls.append(kor)
    il += 1
    prov = False
    while not prov:
        otv = input('Добавить еще товар? (y/n): ')
        if otv == 'n':
            if1 = False
            break
        elif otv != 'y':
            print('Не вернный ввод.')
        else:
            prov = True

print(ls)