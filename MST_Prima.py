import polska
from math import inf

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


class Adjacency_list:

    def __init__(self):
        self.dict = {}
        self.vertices = []
        self.data = []

    def insertVertex(self, vertex, color=None, brightness=None):
        if vertex not in self.vertices:
            self.data.append((vertex, color, brightness))
            self.vertices.append(vertex)
            self.dict[self.getVertexIdx(vertex)] = []


    def insertEdge(self, vertex1, vertex2, weight):
        if vertex1 not in self.vertices:
            self.insertVertex(vertex1)

        if vertex2 not in self.vertices:
            self.insertVertex(vertex2)

        self.dict[self.getVertexIdx(vertex1)].append(((self.getVertexIdx(vertex2)),weight))
        self.dict[self.getVertexIdx(vertex2)].append(((self.getVertexIdx(vertex1)),weight))


    def deleteVertex(self, vertex):
        i = self.getVertexIdx(vertex)
        self.vertices.pop(i)
        self.data.pop(i)

        temp_list = {}
        for key,value in self.dict.items():
            # print(value)
            if key <= i:
                temp = []
                for element in value:
                    # print(element)
                    if element[0] < i:
                        temp.append(element)
                    if element[0] > i:
                        temp.append((element[0]-1,element[1]))
                temp_list[key] = temp

            if key > i:
                temp = []
                for element in value:
                    if element[0] < i:
                        temp.append(element)
                    if element[0] > i:
                        temp.append((element[0]-1,element[1]))

                temp_list[key-1] = temp
        self.dict = temp_list


    def deleteEdge(self, vertex1, vertex2):
        indeks = self.getVertexIdx(vertex2)
        self.dict[self.getVertexIdx(vertex1)].remove(self.getVertexIdx(vertex2))
        self.dict[self.getVertexIdx(vertex2)].remove(self.getVertexIdx(vertex1))


    def getVertexIdx(self, vertex):
        for i, value in enumerate(self.vertices):
            if value == vertex:
                return i

    def getVertex(self, vertex_idx):
        x = self.vertices[vertex_idx]
        return x

    def neighbours(self, vertex_idx):
        neighbours = []
        for x in self.dict[vertex_idx]:
            neighbours.append(x)
        if neighbours == []:
            return "Brak sąsiadów"
        else:
            return neighbours

    def order(self):
        return len(self.dict)

    def size(self):
        size = 0
        for i in self.dict.values():
            for j in i:
                if j != 0:
                    size += 1
        return int(size/2)

    def edges(self):
        temp_edges = []

        for key, value in self.dict.items():
            for i in value:
                if i != 0:
                    temp_edges.append((self.getVertex(key), self.getVertex(i)))

        return temp_edges

    def MST(self, start=0):
        A = Adjacency_list()
        suma = 0

        parent = [-1 for _ in range(len(self.vertices))]
        distance = [inf for _ in range(len(self.vertices))]
        intree = [0 for _ in range(len(self.vertices))]

        for i in self.vertices:
            A.insertVertex(i)

        v = start
        while intree[v] == 0:
            intree[v] = 1
            for index, value in enumerate(self.neighbours(v)):
                if value[1] < distance[value[0]] and intree[value[0]] == 0:
                    parent[value[0]] = v
                    distance[value[0]] = value[1]


            temp_dist = inf
            for x in range(len(self.vertices)):
                if intree[x] == 0 and distance[x] < temp_dist:
                    temp_dist = distance[x]
                    v = x

            if temp_dist != inf:
                vertex1 = self.getVertex(parent[v])
                vertex2 = self.getVertex(v)
                A.insertEdge(vertex1, vertex2, temp_dist)

                suma += temp_dist

        return A, suma

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), w, end=";")
        print()
    print("-------------------")


def main():
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)]

    adjlist = Adjacency_list()

    for (i, j, w) in graf:

        adjlist.insertVertex(i)
        adjlist.insertEdge(i, j, w)

    mst,distance = adjlist.MST(0)
    printGraph(mst)
    print('Długość drzewa rozpinającego : ',distance)
main()


