from collections import defaultdict
from typing import List


def min_dist_to_furthest_node(n: int, edges: List[List[int]]) -> int:
    """
    Time  : O(N)
    Space : O(N),
    """
    # CREATE THE GRAPH
    g = create(edges)

    # GET IN-DEG AND THOSE WITH IN-DEG = 1
    idg, idg1 = get_deg(n, edges)

    # COUNT THE DISTANCE
    d = 0

    # KEEP PLUCKING THE LEAVES
    while len(idg1) > 1:
        num_leaves = len(idg1)
        idg1_new = set()
        for _ in range(num_leaves):
            removed = idg1.pop()
            for nb in g.get(removed, []):
                idg[nb] -= 1
                if idg[nb] == 1: idg1_new.add(nb)
        d += 1
        idg1 = idg1_new

    return d


def create(edges):
    g = defaultdict(list)
    for s, e in edges:
        g[s].append(e)
        g[e].append(s)
    return g


def get_deg(n, edges):
    idg = [0] * (n + 1)
    for s, e in edges:
        idg[s] += 1
        idg[e] += 1
    idg1 = set([i for i in range(1, n + 1) if idg[i] == 1])
    return idg, idg1


if __name__ == "__main__":
    print(min_dist_to_furthest_node(6, [[1, 4], [2, 3], [3, 4], [4, 5], [5, 6]]) == 2)
    print(min_dist_to_furthest_node(6, [[1, 3], [4, 5], [5, 6], [3, 2], [3, 4]]) == 2)
    print(min_dist_to_furthest_node(2, [[1, 2]]) == 1)
    print(min_dist_to_furthest_node(10, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 5)
    print(min_dist_to_furthest_node(10, [[7, 8], [7, 9], [4, 5], [1, 3], [3, 4], [6, 7], [4, 6], [2, 3], [9, 10]]) == 3)
