# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, ch):
        self.ch = ch

    def __add__(self, other):
        return f'z = {self.ch + other.ch}'

    def __mul__(self, other):
        return f'z = {self.ch * other.ch}'

    def __str__(self):
        return f'z = {self.ch}'


a = ComplexNum(complex(2, 3))
b = ComplexNum(complex(-1, 1))
print(a + b)
print(a * b)