from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def build_tree(levels: List[List[int]]) -> (TreeNode, List[TreeNode]):
    print(levels)
    levels = [[TreeNode(v) if v else None for v in level] for level in levels]

    for i in range(len(levels) - 1):
        for j in range(len(levels[i])):
            c = levels[i][j]
            if c:
                c.left = levels[i + 1][2 * j]
                c.right = levels[i + 1][2 * j + 1]
    return levels[0][0]


def same_valued_subtree(root: TreeNode, last_val: int = None) -> int:
    """
    Time  : O(N)
    Space : O(N), WHERE N = NUMBER OF NODES IN THE TREE
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return int(root.val == last_val or last_val is None) + \
           same_valued_subtree(root.left, root.val) + \
           same_valued_subtree(root.right, root.val)


if __name__ == "__main__":
    n = int(input())
    if n == -1:
        print(-1)
    elif n == 0:
        print(1)
    else:
        # O(N)
        levels = [[int(num) if num != "-1" else None for num in input().split(" ")] for _ in range(n + 1)]

        # O(N)
        root = build_tree(levels)

        # O(N)
        print(same_valued_subtree(root))
