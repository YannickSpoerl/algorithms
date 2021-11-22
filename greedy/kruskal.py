from typing import Optional


class KruskalNode:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class KruskalEdge:

    def __init__(self, node1: KruskalNode, node2: KruskalNode, weight: int):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __repr__(self):
        return f"{self.node1}-- {self.weight} --{self.node2}"


class UnionFind:

    def __init__(self):
        self.sets = []

    def create(self, node: KruskalNode):
        s = set()
        s.add(node)
        self.sets.append(s)

    def find(self, node: KruskalNode) -> Optional[set[KruskalNode]]:
        for s in self.sets:
            if node in s:
                return s
        return None

    def merge(self, node1: KruskalNode, node2: KruskalNode):
        set1 = None
        for s in self.sets:
            if node1 in s:
                set1 = s
        for s in self.sets:
            if node2 in s:
                set1.update(s)
                self.sets.remove(s)


def kruskal(nodes: list[KruskalNode], edges: list[KruskalEdge]) -> list[KruskalEdge]:
    union_find = UnionFind()
    minimum_spanning_tree = []
    for node in nodes:
        union_find.create(node)

    edges.sort(key=lambda edge: edge.weight)

    for e in edges:
        if union_find.find(e.node1) != union_find.find(e.node2):
            minimum_spanning_tree.append(e)
            union_find.merge(e.node1, e.node2)

    return minimum_spanning_tree
