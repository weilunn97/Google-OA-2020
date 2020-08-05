from collections import defaultdict
from typing import List


def delayed_projects(dep: List[List[str]], delayed: List[str]) -> List[str]:
    """
    Time  : O(N + L)
    Space : O(1), WHERE N = NUMBER OF PROJECTS, L = len(dep)
    """

    # CONSTRUCT THE GRAPH
    g = defaultdict(list)

    for d in dep:
        g[d[1]].append(d[0])

    # KEEP TRACK OF VISITED NODES
    vis = set()

    # KEEP TRACK OF THE IMPACTED PROJECTS
    impacted = []

    # START A DFS FOR EACH IMPACT PROJ
    for delay in delayed:
        dfs(g, delay, vis, impacted)

    return sorted(impacted)


def dfs(g, delay, vis, impacted):
    if delay in vis:
        return
    vis.add(delay)
    impacted.append(delay)
    for nb in g.get(delay, []):
        dfs(g, nb, vis, impacted)


if __name__ == "__main__":
    print(delayed_projects([['B', 'A'], ['C', 'B']], ['B']) == ['B', 'C'])
    print(delayed_projects([['P', 'Q'], ['P', 'S'], ['Q', 'R'], ['R', 'T'], ['S', 'T']], ['Q', 'S']) == ['P', 'Q', 'S'])
    print(delayed_projects([['B', 'A'], ['C', 'B'], ['C', 'E'], ['D', 'C'], ['D', 'F'], ['E', 'A'], ['F', 'E'],
                            ['G', 'F']], ['B', 'F']) == ['B', 'C', 'D', 'F', 'G'])
