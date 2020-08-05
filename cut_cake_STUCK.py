from typing import List


def cut_cake(cake: List[List[int]], pieces: int) -> int:
    """
    Time  : O()
    Space : O(),
    """
    return bt(cake, pieces, [0], set(), "")


def bt(cake: List[List[int]], pieces: int, ways: List[int], vis: set, path: str):
    # BASE CASE
    if pieces == 0:
        return 1


    curr_ways = 0

    # VERTICAL CUT
    for j in range(1, len(cake[0])):
        if valid(cake, True, j):
            curr_ways += bt(cake, pieces, )

    # HORIZONTAL CUT


def valid(cake: List[List[int]], vertical: bool, idx: int):
    # VERTICAL CUT
    if vertical:
        return any([cake[i][j] for j in range(idx) for i in range(len(cake))]) and \
               any([cake[i][j] for j in range(idx, len(cake[0])) for i in range(len(cake))])

    # HORIZONTAL CUT
    else:
        return any([cake[i][j] for j in range(len(cake[0])) for i in range(idx)]) and \
               any([cake[i][j] for j in range(len(cake[0])) for i in range(idx, len(cake))])


if __name__ == "__main__":
    print(cut_cake([[1, 1], [1, 1]], 3) == 2)
    print(cut_cake([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 3) == 2)
    print(cut_cake([[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]], 4) == 1)
    print(cut_cake([[0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]], 2) == 3)
    print(cut_cake([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 2) == 3)
    print(cut_cake([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 4) == 8)
    print(cut_cake([[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]], 4) == 8)
    print(cut_cake([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], 5) == 126)
    print(cut_cake([[1 for _ in range(10)] for _ in range(10)], 4) == 14076)
