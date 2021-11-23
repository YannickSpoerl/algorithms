class CheckBipartitenessNode:
    """node in graph to check bipartiteness of"""

    def __init__(self, name: str):
        self.name = name


class CheckBipartitenessEdge:
    """edge in graph to check bipartiteness of"""

    def __init__(self, node1: CheckBipartitenessNode, node2: CheckBipartitenessNode):
        self.node1 = node1
        self.node2 = node2


def check_bipartiteness(nodes: list[CheckBipartitenessNode], edges: list[CheckBipartitenessEdge]) -> bool:
    """given a undirected unweighted graph, check if graph is bipartite
    :param nodes: the list of nodes of the graph
    :param edges: the list of edges of the graph
    """
    colors = {}
    discovered = set()
    queue = [nodes[0]]
    colors[nodes[0]] = 0
    while queue:
        current_node = queue.pop()
        for edge in edges:
            other_node = None
            if edge.node1 == current_node:
                other_node = edge.node2
            elif edge.node2 == current_node:
                other_node = edge.node1

            if other_node:
                if other_node in colors and colors[other_node] == colors[current_node]:
                    return False
                if colors[current_node] == 1:
                    colors[other_node] = 0
                else:
                    colors[other_node] = 1

                if other_node not in discovered:
                    queue.append(other_node)
                discovered.add(current_node)
    return True
