class DijkstraNode:
    """a node in a graph for the dijkstra algorithm"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class DijkstraEdge:
    """an edge between two nodes in a graph for the dijkstra algorithm"""

    def __init__(self, start: DijkstraNode, end: DijkstraNode, weight: int):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return f"{self.start}-- {self.weight} -->{self.end}"


def dijkstra(nodes: list[DijkstraNode], edges: list[DijkstraEdge], source: DijkstraNode) -> dict[DijkstraNode, int]:
    """computes min-distance from a source to all other nodes  in a directed graph with weighted edges
    :param nodes: a list of nodes
    :param edges: a list of weighted edges
    :param source: the node to start from
    :return: a dictionary with the min-distance for every node
    """

    distances = {}
    undiscovered = nodes.copy()
    for node in nodes:
        distances[node] = float("+inf")
    distances[source] = 0

    while undiscovered:
        min_distance_node = None
        for node in undiscovered:
            if min_distance_node is None or distances[node] < distances[min_distance_node]:
                min_distance_node = node

        undiscovered.remove(min_distance_node)

        for edge in edges:
            if edge.start == min_distance_node and edge.end in undiscovered:
                new_distance = distances[min_distance_node] + edge.weight

                if new_distance < distances[edge.end]:
                    distances[edge.end] = new_distance

    return distances
