# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def proverka(perem):
    if perem < 10:
        return '0' + str(perem)
    return perem


def out(a, b, c):
    print('{}:{}:{}'.format(a, b, c))


sec = int(input('Введите кол-во секунд:'))
minute = hour = '00'

if sec > 60:
    minute = int(sec / 60)
    sec = sec % 60
    if minute > 59:
        hour = int(minute / 60)
        hour = proverka(hour)
        minute = minute % 60
        sec = proverka(sec)
        minute = proverka(minute)
        out(hour, minute, sec)
    else:
        minute = proverka(minute)
        sec = proverka(sec)
        out(hour, minute, sec)
else:
    sec = proverka(sec)
    out(hour, minute, sec)

s = int(input('Введите кол-во секунд:'))
m = s // 60
s = s % 60
h = m // 60
m = m % 60

print(f'{h:02d}:{m:02d}:{s:02d}')
