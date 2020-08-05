from collections import defaultdict
from typing import List


def min_dist_to_furthest_node(n: int, edges: List[List[int]]) -> int:
    """
    Time  : O(N)
    Space : O(N),
    """

    # SETUP THE GRAPH
    g = defaultdict(list)

    # SETUP A SET OF NODES WITH IN-DEGREE = 0
    id0 = set([i for i in range(1, n + 1)])

    # COUNT THE IN-DEGREE OF EACH NODE
    id = [0] * (n + 1)

    # TRACK THE DIST
    dist = 0

    for e in edges:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])
        id[e[0]] += 1
        id[e[1]] += 1
        if id[e[0]] > 1 and e[0] in id0: id0.remove(e[0])
        if id[e[1]] > 1 and e[1] in id0: id0.remove(e[1])

    # LOOP TILL WE ONLY HAVE 0 - 1 NODE WITH ID = 0
    while len(id0) > 1:

        # TRACK THE NEW ID0
        new_id0 = set()

        # REMOVE ALL LEAVES AND THEIR EDGES
        for leaf in id0:
            for nb in g.get(leaf):
                id[nb] -= 1
                if id[nb] == 1: new_id0.add(nb)

        id0 = new_id0
        dist += 1

    return dist


if __name__ == "__main__":
    print(min_dist_to_furthest_node(6, [[1, 4], [2, 3], [3, 4], [4, 5], [5, 6]]) == 2)
    print(min_dist_to_furthest_node(6, [[1, 3], [4, 5], [5, 6], [3, 2], [3, 4]]) == 2)
    print(min_dist_to_furthest_node(2, [[1, 2]]) == 1)
    print(min_dist_to_furthest_node(10, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == 5)
    print(min_dist_to_furthest_node(10, [[7, 8], [7, 9], [4, 5], [1, 3], [3, 4], [6, 7], [4, 6], [2, 3], [9, 10]]) == 3)
