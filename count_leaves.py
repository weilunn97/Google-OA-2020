from typing import List, Set


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def buildTree(levels: List[List[int]]) -> (TreeNode, List[TreeNode]):
    levels = [[TreeNode(v) if v else None for v in level] for level in levels]
    leaves = set()

    for i in range(len(levels) - 1):
        for j in range(len(levels[i])):
            c = levels[i][j]
            if c:
                c.left = levels[i + 1][2 * j]
                c.right = levels[i + 1][2 * j + 1]
                if not c.left and not c.right: leaves.add(c)
    for leaf in levels[-1]:
        if leaf: leaves.add(leaf)
    return levels[0][0], leaves


def markParent(root: TreeNode, parent: TreeNode = None):
    if not root:
        return

    root.parent = parent
    markParent(root.left, root)
    markParent(root.right, root)


def count_leaves(k: int, leaves: Set) -> int:
    """
    Time  : O(N LOG N)
    Space : O(N), WHERE N = NUMBER OF NODES IN THE TREE
    """
    count = [0]
    visLeaves = set()
    while leaves:
        l = leaves.pop()
        visLeaves.add(l)
        dfs(l, leaves, k, count, set(), l, visLeaves)
    return count[0]


def dfs(curr: TreeNode, leaves: Set[TreeNode], k: int, count: List[int], vis: Set, start: TreeNode,
        visLeaves: Set[TreeNode]) -> int:
    if k < 0 or not curr or curr in vis:
        return

    vis.add(curr)
    dfs(curr.left, leaves, k - 1, count, vis, start, visLeaves)
    dfs(curr.right, leaves, k - 1, count, vis, start, visLeaves)
    dfs(curr.parent, leaves, k - 1, count, vis, start, visLeaves)
    count[0] += int(curr in leaves and curr != start and curr not in visLeaves)
    vis.remove(curr)


if __name__ == "__main__":
    k = int(input())
    n = int(input())

    # O(N)
    levels = [[int(num) if num != "-1" else None for num in input().split(" ")] for _ in range(n + 1)]

    # O(N)
    root, leaves = buildTree(levels)

    # O(N)
    markParent(root)

    # O(N LOG N)
    print(count_leaves(k, leaves))
