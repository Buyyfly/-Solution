# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open('2.txt', 'r', encoding='UTF-8')

i = 0
for el in file:
    s = el[:-1].split(' ')
    i += 1
    print(f'В строке №{i} кол-во слов: {len(s)}')
print(f'Количество строк в файле: {i}:')
file.close()