"""Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа."""


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            raise ValueError()

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        try:
            return Cell(self.quantity//other.quantity)
        except ZeroDivisionError as e:
            print(e)

    def make_order(self, cells_in_row):
        res = ''
        temp = self.quantity
        while temp/cells_in_row > 1:
            res = res + cells_in_row * '*' + '\n'
            temp = temp - cells_in_row
        return res + temp * '*'


cell1 = Cell(5)
cell2 = Cell(4)
new_cell1 = cell1 + cell2
new_cell2 = cell1 - cell2
new_cell3 = cell1 * cell2
new_cell4 = cell1 / cell2
print(new_cell1.make_order(2))
