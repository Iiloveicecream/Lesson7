"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
 который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица."""


class Matrix:
    def __init__(self, list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        for i in list_of_lists:
            if columns != len(i):
                raise ValueError('All columns should have same length')
        self.matrix = list_of_lists
        self.i = len(list_of_lists)
        self.j = len(list_of_lists[0])

    def __str__(self):
        a = ''
        for i in self.matrix:
            a = a + str(i) + '\n'
        return a

    def __add__(self, other):
        if self.i == other.i & \
                self.j == other.j:
            new = Matrix(self.i * [self.j * [0]])
            print(new)
            print(self)
            for i in range(0, self.i):
                for j in range(0, self.j):
                    new.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return new
        else:
            raise ValueError('matrices should have same amount of rows and columns')


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[4, 3], [2, 1]])
matrix = matrix1 + matrix2
print(matrix)
