import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.visited = False
        self.neighbors = []


class Graph:
    def __init__(self):
        self.nodes = set()

    def get_all_nodes(self):
        return list(self.nodes)

    def add_edge(self, start, end):
        if start not in self.nodes:
            self.nodes.add(start)
        if end not in self.nodes:
            self.nodes.add(end)
        # Directed Graph -> 'from' start 'to' end and not vice versa
        start.neighbors.append(end)


def bfs(graph: Graph, start: Node, end: Node) -> bool:
    if start == end:
        return True

    # Updating for every new execution
    for node in graph.get_all_nodes():
        node.visited = False

    queue = collections.deque()
    queue.append(start)
    start.visited = True
    while queue:
        curr_node = queue.popleft()
        for nb in curr_node.neighbors:
            if not nb.visited:
                if nb == end:
                    return True
                nb.visited = True
                queue.append(nb)
    return False


if __name__ == "__main__":
    test_graph = Graph()
    a, b, c, d, e, f = Node("a"), Node("b"), Node("c"), Node("d"), Node("e"), Node("f"),

    test_graph.add_edge(a, b)
    test_graph.add_edge(a, c)
    test_graph.add_edge(c, a)
    test_graph.add_edge(c, d)
    test_graph.add_edge(a, e)
    test_graph.add_edge(f, d)

    assert bfs(test_graph, a, b) is True, "No Path exists!"
    assert bfs(test_graph, a, c) is True, "No Path exists!"
    assert bfs(test_graph, a, d) is True, "No Path exists!"
    assert bfs(test_graph, b, d) is True, "No Path exists!"
