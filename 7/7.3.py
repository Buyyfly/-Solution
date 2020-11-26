class Cell:
    def __init__(self, ch_cell):
        self.ch_cell = ch_cell

    def __add__(self, other):
        return Cell(self.ch_cell + other.ch_cell)

    def __sub__(self, other):
        a = self.ch_cell - other.ch_cell
        return Cell(a) if a >= 0 else None

    def __mul__(self, other):
        return Cell(self.ch_cell * other.ch_cell)

    def __truediv__(self, other):
        return Cell(self.ch_cell // other.ch_cell)

    def make_order(self):
        ls = ['*' for el in range(self.ch_cell)]
        return '\n'.join([''.join(ls[i:i + 5]) for i in range(0, len(ls), 5)])


a1 = Cell(10)
print(a1.make_order())
a2 = Cell(16)
print(a2.make_order())
a3 = a1 + a2
print(a3.make_order())
a4 = a1 - a2
if a4 is not None:
    print(a4.make_order())
else:
    print('Значение отрицательно')

a5 = a1 * a2
print(a5.make_order())
a6 = a1 / a2
print(a6.make_order())