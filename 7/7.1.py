class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        sr = ''
        for el in self.param:
            sr += f'{" ".join([str(i) for i in el])}\n'
        return sr

    def __add__(self, other):
        new_arr = [[] for ch in range(len(self.param))]
        for i in range(len(self.param)):
            for e in range(len(self.param[i])):
                new_arr[i].append(self.param[i][e] + other.param[i][e])
        return Matrix(new_arr)


a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[3, 5], [2, 4], [6, 1]])
print(a)
c = a + b
print(c)
