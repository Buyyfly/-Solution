from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def sum(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, size):
        self.__size = size

    def sum(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self.__height = height

    def sum(self):
        return 2 * self.__height + 0.3

a = Coat(30)
print(a.sum())
b = Costume(50)
print(b.sum())
