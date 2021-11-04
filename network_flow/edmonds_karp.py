from typing import Optional


class EdmondsKarpNode:

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class EdmondsKarpEdge:

    def __init__(self, start: EdmondsKarpNode, end: EdmondsKarpNode, capacity: int):
        self.start = start
        self.end = end
        self.capacity = capacity

    def __repr__(self):
        return f"{self.start} -- ({self.capacity}) --> {self.end} "


def edmonds_karp(source: EdmondsKarpNode, sink: EdmondsKarpNode, edges: list[EdmondsKarpEdge]) -> int:
    max_flow = 0

    shortest_path = find_path(source, sink, edges)
    while shortest_path:
        bottleneck = float("+inf")
        for edge in shortest_path:
            if edge.capacity < bottleneck:
                bottleneck = edge.capacity

        for shortest_path_edge in shortest_path:
            found_reverse_edge = False
            for old_edge in edges:
                if old_edge == shortest_path_edge:
                    new_capacity = old_edge.capacity - bottleneck
                    if new_capacity == 0:
                        edges.remove(old_edge)
                    else:
                        old_edge.capacity = new_capacity
                if old_edge.start == shortest_path_edge.end and old_edge.end == shortest_path_edge.start:
                    old_edge.capacity += bottleneck
                    found_reverse_edge = True
            if not found_reverse_edge:
                edges.append(EdmondsKarpEdge(shortest_path_edge.end, shortest_path_edge.start, bottleneck))

        max_flow += bottleneck
        shortest_path = find_path(source, sink, edges)

    return max_flow


def find_path(source: EdmondsKarpNode, sink: EdmondsKarpNode, edges: list[EdmondsKarpEdge]) \
        -> Optional[list[EdmondsKarpEdge]]:
    pred = {source: None}
    queue = [source]
    discovered = [source]

    while queue:
        current_node = queue.pop(0)
        for edge in edges:
            if edge.start == current_node and edge.end not in discovered:
                pred[edge.end] = edge
                discovered.append(edge.end)
                queue.append(edge.end)

                if edge.end == sink:
                    path = []
                    cur_pred = pred[sink]
                    while cur_pred is not None:
                        path.insert(0, cur_pred)
                        cur_pred = pred[cur_pred.start]
                    return path
    return None
