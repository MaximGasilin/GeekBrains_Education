# Задание #1
#
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__() ),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — с истема некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
#  31 22                3  5 32                3 5 8 3
#  37 43                2  4  6                8 3 7 1
#  51 86               -1 64 -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
#
# Специально сохранил понравившиеся мне реализации формирования печатной строки матрицы. Чтобы не потерять.
# matrix_string = ''
# for el in self.matrix:
#     # matrix_string = matrix_string + reduce(lambda x, y: x + f'{str(y):>{max_l + 2}}', el, '') + '\n'
#     matrix_string = matrix_string + ''.join(map(lambda x: f'{str(x):>{max_l + 2}}', el)) + '\n'


from copy import deepcopy
from functools import reduce


class Matrix:

    def __init__(self, list_of_lists):
        self.rows = len(list_of_lists)
        self.cols = reduce(lambda x, y: max(x, len(y)), list_of_lists, 0)
        self.matrix = deepcopy(list_of_lists)
        for el in self.matrix:
            if len(el) < self.cols:
                # Если в строке вдруг меньше элементов, чем в максимальной, то добавим нулей.
                for i in range(0, self.cols - len(el)):
                    el.append(0)

    def __str__(self):
        # Сперва вычислим максимальную длину числа, чтобы матрица выводилась красисво
        # Это значение можно хранить в памяти и вычислять при изменениях, но я не нашел для себя
        # однозначного ответа, что придется делать чаще - печать или изменение?
        max_l = 0
        for el in self.matrix:
            max_l = reduce(lambda x, y: max(x, len(str(y))), el, max_l)

        # Двойной map внутри join. Внутренний - по строки. А внешний по основному списку.
        return ''.join(map(lambda elem: ''.join(map(lambda x: f'{str(x):>{max_l + 2}}', elem)) + '\n', self.matrix))

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Матрицы можно складывать только с матрицей!')
        elif self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Матрицы разных размерностей. Сложение не возможно!')
        new_list_of_list = []
        for r_count in range(0, self.rows):
            new_row = []
            new_list_of_list.append(new_row)
            for c_count in range(0, self.cols):
                new_row.append(self.matrix[r_count][c_count] + other.matrix[r_count][c_count])
        return Matrix(new_list_of_list)


if __name__ == '__main__':

    matrix_1 = Matrix([[2, 0, 4], [5, 6, 7], [33, 18]])
    print(matrix_1)
    matrix_2 = Matrix([[10, 10, 10], [20, 20, 20], [30, 30, 30]])
    print(matrix_2)

    matrix_3 = matrix_1 + matrix_2
    print(matrix_3)
