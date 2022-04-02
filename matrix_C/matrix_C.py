#skończone
from typing import Union,List

class Matrix:
    def __init__(self,matrix: Union[tuple, List[list]],matrix_fill: int = 0):
        if isinstance(matrix, tuple):
            if matrix[0] > 0 and matrix[1] > 0:
                self.matrix = [[matrix_fill for _ in range(matrix[1])] for _ in range(matrix[0])]
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

def main():
    m1 = [[1, 0, 2], [-1, 3, 1]]
    m2 = (2,3)
    m3 = [[3, 1], [2, 1], [1, 0]]


    a = Matrix(m1)
    b = Matrix(m2,1)
    c = Matrix(m3)

    print(transpose(a),'\n')
    print(a+b,'\n')
    print(a*c,'\n')
main()


