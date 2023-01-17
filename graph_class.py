#skończone
import polska

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


class Adjacency_list:

    def __init__(self):
        self.list = {}
        self.dict = []

    def insertVertex(self, vertex):
        self.dict.append(vertex)
        self.list[self.getVertexIdx(vertex)] = []

    def insertEdge(self, vertex1, vertex2):
        if vertex1 not in self.dict:
            self.insertVertex(Vertex(vertex1))

        if vertex2 not in self.dict:
            self.insertVertex(Vertex(vertex2))

        self.list[self.getVertexIdx(vertex1)].append(self.getVertexIdx(vertex2))
        # self.list[self.getVertexIdx(vertex2)].append(self.getVertexIdx(vertex1))

    def deleteVertex(self, vertex):
        i = self.getVertexIdx(vertex)
        self.dict.pop(i)

        temp_list = {}
        for key,value in self.list.items():
            if key <= i:
                temp = []
                for element in value:
                    if element < i:
                        temp.append(element)
                    if element > i:
                        temp.append(element-1)
                temp_list[key] = temp

            if key > i:
                temp = []
                for element in value:
                    if element < i:
                        temp.append(element)
                    if element > i:
                        temp.append(element-1)

                temp_list[key-1] = temp
        self.list = temp_list


    def deleteEdge(self, vertex1, vertex2):
        self.list[self.getVertexIdx(vertex1)].remove(self.getVertexIdx(vertex2))
        self.list[self.getVertexIdx(vertex2)].remove(self.getVertexIdx(vertex1))

    def getVertexIdx(self, vertex):
        for i, value in enumerate(self.dict):
            if value == vertex:
                return i

    def getVertex(self, vertex_idx):
        return self.dict[vertex_idx]

    def neighbours(self, vertex_idx):
        neighbours = []
        for x in self.list[vertex_idx]:
            neighbours.append(self.dict[x])
        if neighbours == []:
            return "Brak sąsiadów"
        else:
            return neighbours

    def order(self):
        return len(self.list)

    def size(self):
        size = 0
        for i in self.list.values():
            for j in i:
                if j != 0:
                    size += 1
        return int(size/2)

    def edges(self):
        temp_edges = []

        for key, value in self.list.items():
            for i in value:
                if i != 0:
                    temp_edges.append((self.getVertex(key), self.getVertex(i)))

        return temp_edges


def test1():
    graph = Adjacency_matrix()

    for first_letter in polska.polska:
        graph.insertVertex(Vertex(first_letter[2]))

    for element in polska.graf:
        graph.insertEdge(element[0],element[1])

    graph.deleteVertex('K')
    graph.deleteEdge('W', 'E')
    polska.draw_map(graph.edges())

def test2():
    graph = Adjacency_list()

    for first_letter in polska.polska:
        graph.insertVertex(first_letter[2])

    for element in polska.graf:
        graph.insertEdge(element[0],element[1])

    graph.deleteVertex('K')
    graph.deleteEdge('W', 'E')
    polska.draw_map(graph.edges())

def main():
    variable = input('Wybierz reprezentację grafu : macierz/lista :')
    if variable == 'macierz':
        test1()
    if variable == 'lista':
        test2()
    else:
        print("Złe wejście")
        main()
main()