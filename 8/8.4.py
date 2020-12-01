# 8.4-8.6
class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)


class Equipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return [self.name, self.price, self.quantity]


class Printer(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f'{self.name} - {self.price} - {self.quantity}'


class Scaner(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f'{self.name} - {self.price} - {self.quantity}'


class Xerox(Equipment):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f'{self.name} - {self.price} - {self.quantity}'


sklad = Sklad()
while True:
    a = input('Введите параматры новой позиции через пробел.')
    if a == 's':
        break
    a = a.split()
    if len(a) != 4:
        print('error')
    else:
        try:
            if a[0] == '1':
                sklad.add_to(Scaner(a[1], int(a[2]), int(a[3])))
            elif a[0] == '2':
                sklad.add_to(Printer(a[1], int(a[2]), int(a[3])))
            elif a[0] == '3':
                sklad.add_to(Xerox(a[1], int(a[2]), int(a[3])))
            else:
                print('Такой модели не существует')
        except ValueError:
            print('Ошибка ввода')

print(sklad._dict)



