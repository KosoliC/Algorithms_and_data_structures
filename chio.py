#skończone
from matrix_C import Matrix #importuje klase macierzy

from typing import Union,List

class Matrix:
    def __init__(self,matrix: Union[tuple, List[list]],matrix_fill: int = 0):
        if isinstance(matrix, tuple):
            if matrix[0] > 0 and matrix[1] > 0:
                self.matrix = [[matrix_fill for _ in range(matrix[0])] for _ in range(matrix[1])]
            else:
                raise ValueError("The number of rows and columns must be positive")

        else:
            self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            temp = Matrix([[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))])
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    temp[i][j] = (self.matrix[i][j]+other.matrix[i][j])
            return temp
        else:
            raise ValueError("The dimensions of the Matrix must be the same")

    def __mul__(self, other):
        if len(self.matrix) == len(other.matrix[0]) and len(self.matrix[0]) == len(other.matrix):
            temp = Matrix([[0 for _ in range(len(self.matrix))] for _ in range(len(other.matrix[0]))])
            for i in range(len(other.matrix[0])):
                for j in range(len(self.matrix)):
                    value = 0
                    for k in range(len(self.matrix[0])):
                        value = value + (self.matrix[j][k]*other.matrix[k][i])
                    temp[j][i] = value
            return temp
        else:
            raise ValueError("Matrix dimensions are incorrect")


    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        temp = []
        for i in self.matrix:
            temp.append(str(i))
        return '\n'.join(temp)

    def __len__(self):
        return len(self.matrix)


def transpose(transposed_matrix: Matrix) -> Matrix:
    temp = [[0 for _ in range(len(transposed_matrix))] for _ in range(len(transposed_matrix[0]))]
    for i in range(len(transposed_matrix)):
        for j in range(len(transposed_matrix[0])):
            temp[j][i] = transposed_matrix[i][j]
    return Matrix(temp)

def chio(input_matrix: Matrix, swapped = False) -> int: #argumentu swapped używam do zmiany znaku wyznacznika,
    dim = len(input_matrix)                             #jeżeli zamieniam wiersze w macierzy
    multiplier = []

    if dim == 2:
        return input_matrix[0][0]*input_matrix[1][1]-input_matrix[0][1]*input_matrix[1][0]

    if input_matrix[0][0] == 0: #zamiana pierwszego wiersza z elementem zerowym na pierwszym miejscu
        for k in range(dim):
            if input_matrix[k][0] != 0:
                bad_row = input_matrix[0]
                good_row = input_matrix[k]
                input_matrix.matrix[0] = good_row
                input_matrix.matrix[k] = bad_row
                swapped = True
                return chio(input_matrix,swapped)

            elif k == (dim - 1) and input_matrix[k][0] == 0:
                return 0

    else:
        reduced_matrix = Matrix((dim - 1,dim - 1))
        for i in range(dim - 1):
            for j in range(dim - 1):
                temp_matrix = Matrix([[input_matrix[0][0], input_matrix[0][j + 1]], [input_matrix[i + 1][0], input_matrix[i + 1][j + 1]]])
                reduced_matrix[i][j] = chio(temp_matrix)

        multiplier.append(chio(reduced_matrix,swapped))

        if swapped:
            return (-1/(input_matrix[0][0]**(dim - 2)) * sum(multiplier))

        if not swapped:
            return (1 / (input_matrix[0][0] ** (dim - 2)) * sum(multiplier))


d1 = [
    [5 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
]

d2 = [
    [0, 1, 1, 2, 3],
    [4, 2, 1, 7, 3],
    [2, 1, 2, 4, 7],
    [9, 1, 0, 7, 0],
    [1, 4, 7, 2, 2]
]

A = Matrix(d1)
B = Matrix(d2)

print(chio(A))
print(chio(B))

