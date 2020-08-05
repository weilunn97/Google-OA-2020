from typing import List


def fill_matrix(n: int) -> List[List[int]]:
    """
    Time  : O()
    Space : O(),
    """
    # EDGE CASE
    if n == 1:
        return [[1]]

    # CREATE THE GRID
    grid = [[None for _ in range(n)] for _ in range(n)]

    # PLACEMENT ALWAYS BEGINS WITH 1 AT [n//2, n - 1]
    grid[n // 2][n - 1] = 1

    # KEEP TRACK OF VISITED CELLS
    i, j = n // 2, n - 1

    # LOOP TILL WE'VE FILLED ALL
    for num in range(2, n ** 2 + 1):
        try:
            i, j = getNextCoord(i, j, n, grid)
        except ValueError:
            return None
        grid[i][j] = num

    # for row in grid:
    #     print(row)
    return grid


def getNextCoord(i: int, j: int, n: int, grid: List[List[int]]) -> (int, int):
    # GO UP AND RIGHT, WITH WRAP-AROUND
    ni = (i - 1) % n
    nj = (j + 1) % n

    # CHECK IF WE'VE VISITED THIS ALREADY
    if grid[ni][nj] is not None:
        # GO LEFT
        ni = i
        nj = j - 1

    # CHECK IF OOB
    if nj < 0:
        raise ValueError(f"Cannot form magic square of size {n}")

    return ni, nj


if __name__ == "__main__":
    print(fill_matrix(1) == [[1]])
    print(fill_matrix(2) is None)
    print(fill_matrix(3) == [[2, 7, 6],
                             [9, 5, 1],
                             [4, 3, 8]])
    print(fill_matrix(4) is None)
    print(fill_matrix(5) == [[9, 3, 22, 16, 15],
                             [2, 21, 20, 14, 8],
                             [25, 19, 13, 7, 1],
                             [18, 12, 6, 5, 24],
                             [11, 10, 4, 23, 17]])
    print(fill_matrix(6) is None)
    print(fill_matrix(7) == [[20, 12, 4, 45, 37, 29, 28],
                             [11, 3, 44, 36, 35, 27, 19],
                             [2, 43, 42, 34, 26, 18, 10],
                             [49, 41, 33, 25, 17, 9, 1],
                             [40, 32, 24, 16, 8, 7, 48],
                             [31, 23, 15, 14, 6, 47, 39],
                             [22, 21, 13, 5, 46, 38, 30]])
