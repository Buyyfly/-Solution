# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

# 1ое решение c использование проверки вводимого значения > 12

string = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима', ]
try:
    a = int(input('Введите номер месяца года: '))
    if a > 12 or a == 0:
        print(f'В году находятся месяцы от 1 до 12. Месеца под номером {a} не существует.')
    else:
        print(f'Месяц под номером "{a}" относится к веремени года: {string[a - 1]}')
except ValueError as error:
    print('Введенное значение не относится к типу int.')

# 2ое решение с использование проверки на ошибку IndexError

try:
    a = int(input('Введите номер месяца года: '))
    try:
        print(f'Месяц под номером "{a}" относится к веремени года: {string[a - 1]} ' if a > 0
              else f'В году находятся месяцы от 1 до 12. Месеца под номером {a} не существует.')
    except IndexError:
        print(f'В году находятся месяцы от 1 до 12. Месяца под номером {a} не существует.')
except ValueError as error:
    print('Введенное значение не относится к типу int.')

# 3е решение с использование зациленного ввода, пока введное значение не будет удоволетворять условие.
# Функцию можно не использовать, выполнять ввод прямо в цикле.

def vvod(a):
    try:
        a = int(input('Введите номер месяца года: '))
    except ValueError:
        print('Введенное значение не относится к типу int.')
    return a


a = None
while not isinstance(a, int):
    a = vvod(a)
    if isinstance(a, int) and (a > 12 or a == 0):
        print(f'В году находятся месяца от 1 до 12. Месяца под номером {a} не существует.')
        a = None

print(f'Месяц под номером "{a}" относится к веремени года: {string[a - 1]}')

# 4е решение через dict

dictionary = {1: 'Зима', 2: 'Зима', 12: 'Зима',
              3: 'Весна', 4: 'Весна', 5: 'Весна',
              6: 'Лето', 7: 'Лето', 8: 'Лето',
              9: 'Осень', 10: 'Осень', 11: 'Осень', }

try:
    # так как в задании указаны только целые числа введем проверку
    a = int(input('Введите номер месяца года: '))
    # Не будем проверять что числа сооветствуют от 1 до 12, а проверил что введенное значение существует в
    # ключах dictionary
    if dictionary.get(a) is None:
        print(f'В году находятся месяцы от 1 до 12. Месяца под номером {a} не существует.')
    else:
        print(f'Месяц под номером "{a}" относится к веремени года: {dictionary.get(a)}')
except ValueError as error:
    print('Введенное значение не относится к типу int.')



