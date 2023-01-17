from copy import deepcopy
import numpy as np

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if type(self) is type(other):
            return self.key == other
        else:
            return False

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, edge):
        self.edge = edge


class Adjacency_matrix:

    def __init__(self):
        self.vertices = []
        self.dict = {}
        self.matrix = [[]]

    def insertVertex(self, vertex):
        self.vertices.append(vertex.key)
        self.dict[vertex.key] = len(self.vertices) - 1
        temp_matrix = []

        if self.matrix != [[]]:
            for row in self.matrix:
                row.insert(self.dict[vertex.key], 0)
                temp_matrix.append(row)
            temp_matrix.append([0] * (len(self.matrix) + 1))
            self.matrix = temp_matrix
        else:
            self.matrix = [[0]]

    def insertEdge(self, vertex1, vertex2, edge=1):
        if vertex1 not in self.dict:
            self.insertVertex(Vertex(vertex1))

        if vertex2 not in self.dict:
            self.insertVertex(Vertex(vertex2))

        self.matrix[self.dict[vertex1]][self.dict[vertex2]] = edge
        self.matrix[self.dict[vertex2]][self.dict[vertex1]] = edge

    def deleteVertex(self, vertex):
        vertex = Vertex(vertex)
        i = self.dict[vertex.key]
        for key in self.dict:
            if self.dict[key] >= i:
                self.dict[key] = self.dict[key] - 1

        self.dict.pop(vertex.key)
        self.vertices.remove(vertex.key)
        for j in self.matrix:
            j.pop(i)

        self.matrix.pop(i)

    def deleteEdge(self, vertex1, vertex2):
        self.matrix[self.dict[vertex1]][self.dict[vertex2]] = 0
        self.matrix[self.dict[vertex2]][self.dict[vertex1]] = 0

    def getVertexIdx(self, vertex):
        return self.dict[vertex]

    def getVertex(self, vertex_idx):
        return self.vertices[vertex_idx]

    def neighbours(self, vertex_idx):
        neighbours = []
        for j in range(len(self.matrix[vertex_idx])):
            if self.matrix[vertex_idx][j] != 0:
                neighbours.append(j)
        if neighbours == []:
            return "Brak sąsiadów"
        else:
            return neighbours

    def order(self):
        return len(self.matrix)

    def size(self):
        size = 0
        for i in self.matrix:
            for j in i:
                if j != 0:
                    size += 1
        return int(size/2)

    def edges(self):
        temp_edges = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != 0:
                    temp_edges.append((self.vertices[i], self.vertices[j]))

        return temp_edges


def M0(P,G,M):
    G_matrix = G.matrix
    P_matrix = P.matrix
    M_0 = M.copy()
    for i in range(M.shape[0]):
        deg_vi = P_matrix[i].count(1) # zliczam jedynki czyli sprawdzam stopień
        for j in range(M.shape[1]):
            deg_vj = G_matrix[j].count(1)
            if deg_vi <= deg_vj:
                M_0[i][j] = 1
            else:
                M_0[i][j] = 0
    return M_0

def Prune(P, G, M):
    change = True
    while change:
        change = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i][j] == 1:
                    find = False
                    for x in P.neighbours(i):
                        for y in G.neighbours(j):
                            if M[x][y] == 1:
                                find = True
                                break
                        if find:
                            break
                    else:
                        M[i][j] = 0
                        change = True

    return M


def ullman1(used_columns, current_row, G, P, M, counter = 0):
    G_matrix = G.matrix
    P_matrix = P.matrix
    temp_list = []

    if current_row == M.shape[0]:
        temp_matrix = M @ (M @ G_matrix).T
        if np.all(P_matrix == temp_matrix):
            temp_list.append(M.copy())
        return temp_list,counter

    M_prim = deepcopy(M)

    for col in range(M.shape[1]):
        if col not in used_columns:
            M_prim[current_row, :] = 0
            M_prim[current_row, col] = 1
            used_columns.append(col)
            counter += 1
            temp_list, counter = ullman1(used_columns, current_row + 1, G, P, M_prim, counter)
            used_columns.remove(col)
    return temp_list, counter

def ullman2(used_columns, current_row, G, P, M, counter=0):

    G_matrix = G.matrix
    P_matrix = P.matrix
    temp_list = []

    if current_row == M.shape[0]:
        temp_matrix = M @ (M @ G_matrix).T
        if np.all(P_matrix == temp_matrix):
            temp_list.append(M.copy())
        return temp_list, counter

    M_prim = deepcopy(M)

    for col in range(M.shape[1]):
        if col not in used_columns and M[current_row][col]:

            M_prim[current_row, :] = 0
            M_prim[current_row, col] = 1
            used_columns.append(col)
            counter += 1
            temp_list, counter = ullman2(used_columns, current_row + 1, G, P, M_prim, counter)
            used_columns.remove(col)
    return temp_list, counter

def ullman3(used_columns, current_row, G, P, M, counter = 0):

    G_matrix = G.matrix
    P_matrix = P.matrix
    temp_list = []

    if current_row == M.shape[0]:
        temp_matrix = M @ (M @ G_matrix).T
        if np.all(P_matrix == temp_matrix):
            temp_list.append(M.copy())
        return temp_list, counter

    M_prim = deepcopy(M)
    M = Prune(P, G, M)

    for col in range(M.shape[1]):
        if col not in used_columns and M[current_row][col]:
            M_prim[current_row, :] = 0
            M_prim[current_row, col] = 1
            used_columns.append(col)
            counter += 1
            temp_list, counter = ullman3(used_columns, current_row + 1, G, P, M_prim, counter)
            used_columns.remove(col)
    return temp_list, counter


def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    adjmatrix_G = Adjacency_matrix()
    adjmatrix_P = Adjacency_matrix()

    for i,j,w in graph_G:
        adjmatrix_G.insertEdge(i,j,w)

    for i,j,w in graph_P:
        adjmatrix_P.insertEdge(i, j, w)


    rows = adjmatrix_P.order()
    cols = adjmatrix_G.order()

    M = np.zeros((rows, cols), dtype=int)
    result1,counter1 = ullman1([], 0, adjmatrix_G, adjmatrix_P, M)
    print(result1)
    print('liczba wywołań rekurencyjnych:',counter1)

    result2, counter2 = ullman2([], 0, adjmatrix_G, adjmatrix_P, M0(adjmatrix_P,adjmatrix_G,M))
    print(result2)
    print('liczba wywołań rekurencyjnych:', counter2)

    result3, counter3 = ullman3([],0, adjmatrix_G, adjmatrix_P, M0(adjmatrix_P,adjmatrix_G,M))
    print(result3)
    print('liczba wywołań rekurencyjnych:', counter3)
main()


