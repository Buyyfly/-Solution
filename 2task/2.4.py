# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Введите строку: ')

s = string.split()
n = 1
for i in s:
    print(f'№{n} - {i[:10]}')
    n += 1

# OR
for i, word in enumerate(s, 1):
    print(f'№{i} - {word[:10]}')