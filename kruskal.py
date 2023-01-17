#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Dict, Tuple
import graf_mst

class Vertex:
    def __init__(self, id_: str):
        self.id = id_

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Edge:
    def __init__(self, ver1: Vertex, ver2: Vertex, weight: int = 1):
        self.ver1 = ver1
        self.ver2 = ver2
        self.weight = weight

    def __eq__(self, other):
        return self.ver1 == other.ver1 and self.ver2 == other.ver2

    def __hash__(self):
        return hash(self.ver2)

    def get_weight(self):
        return self.weight


class AdjacencyList:
    def __init__(self, id_dict: Dict = None, vertex_list: List[List[Edge]] = None):
        if vertex_list is None:
            vertex_list = []
        if id_dict is None:
            id_dict = {}
        self.id_dict = id_dict
        self.vertex_list = vertex_list

    def insertVertex(self, ver_id: str):
        new_idx = self.order()
        self.vertex_list.append([])
        self.id_dict[ver_id] = new_idx
        return

    def insertEdge(self, ver1_id: str, ver2_id: str, weight: int = 1):
        if ver1_id not in self.id_dict:
            self.insertVertex(ver1_id)
        if ver2_id not in self.id_dict:
            self.insertVertex(ver2_id)
        idx1 = self.getVertexIdx(ver1_id)
        # idx2 = self.getVertexIdx(ver2_id)
        self.vertex_list[idx1].append(Edge(Vertex(ver1_id), Vertex(ver2_id), weight))
        return

    def deleteVertex(self, ver_id: str):
        # Delete vertex from adjacency list
        self.vertex_list.pop(self.getVertexIdx(ver_id))
        for idx, neighbours in enumerate(self.vertex_list):
            neighbours2 = [edge.ver2.id for edge in neighbours]
            if ver_id in neighbours2:
                self.deleteEdge(self.getVertex(idx), ver_id)
        deleted = False
        for ver in self.id_dict:
            if not deleted:
                if ver == ver_id:
                    deleted = True
            else:
                self.id_dict[ver] -= 1
        self.id_dict.pop(ver_id)
        return

    def deleteEdge(self, ver1_id: str, ver2_id: str):
        idx1 = self.getVertexIdx(ver1_id)
        # idx2 = self.getVertexIdx(ver2_id)
        self.vertex_list[idx1].remove(Edge(Vertex(ver1_id), Vertex(ver2_id)))
        return

    def getVertexIdx(self, ver_id: str):
        if ver_id in self.id_dict:
            return self.id_dict[ver_id]
        else:
            raise ValueError('Invalid vertex id')

    def getVertex(self, idx: int):
        for ver in self.id_dict:
            if self.getVertexIdx(ver) == idx:
                return ver
        else:
            raise ValueError('Invalid index')

    def neighbours(self, idx: int):
        neighbours = self.vertex_list[idx]
        return [self.getVertexIdx(edge.ver2.id) for edge in neighbours]

    def order(self):
        return len(self.vertex_list)

    def size(self):
        return len(self.edges())

    def edges(self):
        # [(X, Y), ...]
        visited = []
        edges = []
        for ver in self.id_dict.values():
            for edge in self.vertex_list[ver]:
                if edge.ver2.id not in visited:
                    edges.append((edge.ver1.id, edge.ver2.id, edge.weight))
            visited.append(ver)
        return edges

    def vertexes(self):
        return list(self.id_dict.keys())

    def get_weight(self, ver_idx1, ver_idx2):
        for edge in self.vertex_list[ver_idx1]:
            if self.getVertexIdx(edge.ver2.id) == ver_idx2:
                return edge.get_weight()
        else:
            return None


class UnionFind:
    def __init__(self, vertexes):
        n = max(vertexes) + 1
        self.parent: List[int] = [0] * n
        for i in vertexes:
            self.parent[i] = i
        self.size: List[int] = [1] * n
        self.n = n

    def __repr__(self):
        return str(self.parent)

    def find(self, v):
        if self.parent[v] == v:
            return v
        else:
            return self.find(self.parent[v])

    def same_components(self, s1, s2):
        if self.find(s1) == self.find(s2):
            return True
        else:
            return False

    def union_sets(self, s1, s2):
        if not self.same_components(s1, s2):
            p1, p2 = self.find(s1), self.find(s2)
            if self.size[p1] >= self.size[p2]:
                self.parent[p2] = p1
                self.size[p2] += 1
            else:
                self.parent[p1] = p2
                self.size[p1] += 1
        else:
            return

def convert2int(letter: str):
    # Tylko duże litery, ale żeby zaczynało się od zera
    return ord(letter) - 65

def convert2str(digit: int):
    return chr(digit + 65)

def third_elem(tup: Tuple):
    return tup[2]

def kruskal(edges: List[Tuple]):
    graph = AdjacencyList()
    for edge in edges:
        graph.insertEdge(edge[0], edge[1], edge[2])
    edges2 = graph.edges()
    edges2.sort(key=third_elem, reverse=True)
    vertexes = graph.vertexes()
    if isinstance(vertexes[0], str):
        for i in range(len(vertexes)):
            vertexes[i] = convert2int(vertexes[i])
    union_find = UnionFind(vertexes)
    while edges2:
        edge = edges2.pop()
        ver1, ver2 = edge[0], edge[1]
        if isinstance(ver1, str) and isinstance(ver2, str):
            ver1, ver2 = convert2int(ver1), convert2int(ver2)
        if not union_find.same_components(ver1, ver2):
            print(convert2str(ver1), convert2str(ver2))
            union_find.union_sets(ver1, ver2)
    return union_find

def printGraph(g):
    n = g.order()
    print("------GRAPH------", n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end=" -> ")
        nbrs = g.neighbours(i)
        for j in nbrs:
            print(g.getVertex(j), g.get_weight(i, j), end=";")
        print()
    print("-------------------")

def main():
    vertexes = graf_mst.graf
    print("Dodane krawędzie:")
    print(kruskal(vertexes))


main()
