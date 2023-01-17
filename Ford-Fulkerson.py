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
    def __init__(self, vertex1, vertex2, capacity, isResidual):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.capacity = capacity
        self.isResidual = isResidual
        self.flow = 0
        self.residual = capacity

    def __str__(self):
        return f'Edge({self.capacity},{self.flow},{self.residual},{self.isResidual})'


class Adjacency_list:

    def __init__(self):
        self.dict = {}
        self.vertices = []

    def insertVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.dict[self.getVertexIdx(vertex)] = []
        else:
            pass


    def insertEdge(self, edge):

        if edge.vertex1 not in self.vertices:
            self.insertVertex(edge.vertex1)

        if edge.vertex2 not in self.vertices:
            self.insertVertex(edge.vertex2)

        self.dict[self.getVertexIdx(edge.vertex1)].append(edge)

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
        # indeks = self.getVertexIdx(vertex2)
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
        if isinstance(vertex_idx,str):
            vertex_idx = self.getVertexIdx(vertex_idx)
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

def bfs(G, s):
    s = G.getVertexIdx(s)
    parent = [None for _ in range(G.order())]
    queue = []
    visited_top = list()

    queue.append(s)
    visited_top.append(s)
    while queue:
        m = queue.pop(0)

        for x in G.neighbours(m):
            if G.getVertexIdx(x.vertex2) not in visited_top and x.residual > 0:
                visited_top.append(G.getVertexIdx(x.vertex2))
                queue.append(G.getVertexIdx(x.vertex2))
                parent[G.getVertexIdx(x.vertex2)] = m

    return parent

def minimal_capacity(G,start,end,parents):

    minimal_capacity = inf
    start_index = G.getVertexIdx(start)
    end_index = G.getVertexIdx(end)
    actual = end_index

    if parents[actual] is None:
        minimal_capacity = 0
        return minimal_capacity

    while actual != start_index:
        parent = parents[actual]
        neighbours = G.neighbours(parent)
        real_edge = None
        for i in neighbours:
            if G.getVertexIdx(i.vertex2) == actual and i.isResidual == False:
                real_edge = i
                break

        if real_edge:
            if real_edge.residual < minimal_capacity:
                minimal_capacity = real_edge.residual

        actual = parent

    return minimal_capacity


def augmentation(G, start,end,parents,minimal_capacity):
    start_index = G.getVertexIdx(start)
    end_index = G.getVertexIdx(end)
    actual = end_index

    while actual != start_index:
        parent = parents[actual]
        neighbours = G.neighbours(parent)
        for i in neighbours:
            if G.getVertexIdx(i.vertex2) == actual and i.isResidual == False:
                i.flow += minimal_capacity
                i.residual -= minimal_capacity

            elif G.getVertexIdx(i.vertex2) == actual and i.isResidual == True:
                i.residual += minimal_capacity

        actual = parent


def Ford_Fulkerson(G,start,end):
    start_index = G.getVertexIdx(start)
    end_index = G.getVertexIdx(end)
    actual = end_index
    sum_flow = 0
    parents = bfs(G,start)


    while actual != start_index:
        parent = parents[actual]
        actual = parent
        if actual is None:
            raise ValueError('Nie istnieje ścieżka z wierzchołka początkowego do końcowego')

    min_cap = minimal_capacity(G, start, end, parents)

    while min_cap > 0:
        sum_flow += min_cap
        augmentation(G,start,end,parents,min_cap)
        parents = bfs(G, start)
        min_cap = minimal_capacity(G,start,end,parents)

    return sum_flow

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for i in nbrs:
            print(g.getVertexIdx(i.vertex1), g.getVertexIdx(i.vertex2), end=";")
        print()
    print("-------------------")



def test_0():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    adjlist_0 = Adjacency_list()

    for (i, j, w) in graf_0:
        edge_capacity = Edge(i,j,w,False)
        edge_residual = Edge(j,i,0, True)
        adjlist_0.insertEdge(edge_capacity)
        adjlist_0.insertEdge(edge_residual)


    sum_flow = Ford_Fulkerson(adjlist_0,'s', 't')
    printGraph(adjlist_0)
    return sum_flow


def test_1():
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9),
              ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    adjlist_1 = Adjacency_list()

    for (i, j, w) in graf_1:
        edge_capacity = Edge(i, j, w, False)
        edge_residual = Edge(j, i, 0, True)
        adjlist_1.insertEdge(edge_capacity)
        adjlist_1.insertEdge(edge_residual)

    sum_flow = Ford_Fulkerson(adjlist_1, 's', 't')
    printGraph(adjlist_1)
    return sum_flow

def test_2():
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    adjlist_2 = Adjacency_list()

    for (i, j, w) in graf_2:
        edge_capacity = Edge(i, j, w, False)
        edge_residual = Edge(j, i, 0, True)
        adjlist_2.insertEdge(edge_capacity)
        adjlist_2.insertEdge(edge_residual)

    sum_flow = Ford_Fulkerson(adjlist_2, 's', 't')
    printGraph(adjlist_2)
    return sum_flow


def test_3():
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7),
              ('d', 'c', 4)]
    adjlist_3 = Adjacency_list()

    for (i, j, w) in graf_3:
        edge_capacity = Edge(i, j, w, False)
        edge_residual = Edge(j, i, 0, True)
        adjlist_3.insertEdge(edge_capacity)
        adjlist_3.insertEdge(edge_residual)

    sum_flow = Ford_Fulkerson(adjlist_3, 's', 't')
    printGraph(adjlist_3)
    return sum_flow

def main():

    suma_0 = test_0()
    print('Suma przepływów dla graf_0 :', suma_0, '\n\n')
    suma_1 = test_1()
    print('Suma przepływów dla graf_1 :', suma_1, '\n\n')
    suma_2 = test_2()
    print('Suma przepływów dla graf_2 :', suma_2, '\n\n')
    suma_3 = test_3()
    print('Suma przepływów dla graf_3 :', suma_3, '\n\n')

main()
