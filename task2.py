"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""


from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate(self):
        print('calculate the consumption of fabric')


class Coat(Clothes):

    def __init__(self, size):
        self.V = size

    def calculate(self):
        return self.size/6.5 + 0.5

    @property
    def size(self):
        return self.V

    @size.setter
    def set_size(self, size):
        self.V = size


class Costume(ABC):
    def __init__(self, height):
        self.H = height

    def calculate(self):
        return self.H * 2 + 0.3

    @property
    def height(self):
        return self.H

    @height.setter
    def set_height(self, height):
        self.H = height


coat = Coat(15)
size = 53
costume = Costume(9)
height = 10
print(costume.calculate())
print(coat.calculate())
