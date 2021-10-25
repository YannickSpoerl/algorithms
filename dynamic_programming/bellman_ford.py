class BellmanFordNode:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class BellmanFordEdge:

    def __init__(self, start: BellmanFordNode, end: BellmanFordNode, weight: int):
        self.start = start
        self.end = end
        self.weight = weight


def bellman_ford(start: BellmanFordNode, nodes: list[BellmanFordNode],
                 edges: list[BellmanFordEdge]) -> dict[BellmanFordNode, int]:
    distances = []
    for i in range(0, len(nodes) + 1):
        distances.append({})
        for node in nodes:
            if i == 0 and node == start:
                distances[i][node] = 0
                continue
            elif i == 0 and node != start:
                distances[i][node] = float("+inf")
                continue

            new_distance = distances[i - 1][node]
            for edge in edges:
                if edge.end == node:
                    updated_distance = distances[i - 1][edge.start] + edge.weight
                    if updated_distance < new_distance:
                        new_distance = updated_distance

            distances[i][node] = new_distance

    for node in nodes:
        if distances[len(nodes)][node] != distances[len(nodes) - 1][node]:
            raise Exception("Negative cycle detected")

    return distances[len(nodes)]
