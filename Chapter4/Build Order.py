from typing import List, Tuple
from collections import defaultdict


class Graph:
    def topsort(self, projects: List[str], dependencies: List[Tuple[str,str]]):
        visited, stack = set(), []
        adj_list = self._create_graph(dependencies)
        for node in projects:
            if node not in visited:
                self._topsort_util(node, visited, stack, adj_list)
        return stack

    def _create_graph(self, arr: List[Tuple[str, str]]):
        graph = defaultdict(list)
        for entry in arr:
            graph[ord(entry[0]) - ord('a')].append(entry[1])
        return graph

    def _topsort_util(self, node: str, visited, stack, adj_list):
        visited.add(node)
        for nb in adj_list[ord(node) - ord('a')]:
            if nb not in visited:
                self._topsort_util(nb, visited, stack, adj_list)
        stack.insert(0, node)


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    g = Graph()
    # print(g.topsort(projects, dependencies))

    assert g.topsort(projects, dependencies) == ['f', 'e', 'b', 'a', 'd', 'c'], "Incorrect Code"
