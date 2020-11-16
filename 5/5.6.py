# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.

file = open('6.txt', 'r', encoding='UTF=8')
s = {}
for string in file:
    spl = string.split()
    name = spl[0].replace(':', '')
    s[name] = spl[1:]

end = {}
for i, el in s.items():
    # Заполняем с проверкой на то что есть цифры isdigit().
    end[i] = sum([int(ie.split('(')[0]) for ie in el if ie.split('(')[0].isdigit()])
print(end)
file.close()