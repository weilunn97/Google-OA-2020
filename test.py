from collections import defaultdict


def solve(n, edges):
    g = create(edges)
    paths = []

    # FOR EACH NODE IN THE GRAPH, START A DFS
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            dfs(g, i, j, "", paths, set())

    # print(f"Paths : {paths}")
    if not paths: return 0
    return sum([int(p) for p in paths]) % (10 ** 9 + 7)


def create(edges):
    g = defaultdict(dict)

    for e in edges:
        g[e[0]][e[1]] = e[2]
        g[e[1]][e[0]] = e[2]

    return g


def dfs(g, start, end, path, paths, vis):
    if start == end:
        paths.append(path)
        return
    if start in vis:
        return
    vis.add(start)

    for nb, w in g.get(start, dict()).items():
        dfs(g, nb, end, f"{path}{w}", paths, vis)


N = int(input())
edges = []

for i in range(N - 1):
    edges.append([int(n) for n in input().split(" ")])

print(solve(N, edges))
