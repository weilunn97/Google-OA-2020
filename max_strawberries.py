from typing import List


def max_strawberries(arr: List[int], num: int) -> int:
    """
    Time  : O(MN)
    Space : O(MN), where M = len(arr) and N = num
    """
    # DP[I][J] = MAX STRAWBERRIES GIVEN ARR[:I+1] AND NUM = J
    nrows, ncols = len(arr) + 1, num + 1
    dp = [[0 for _ in range(ncols)] for _ in range(nrows)]

    # ROW 1
    for j in range(1, ncols):
        dp[1][j] = arr[0] + dp[0][j - arr[0]] if arr[0] <= j else 0

    # OTHER CELLS
    for i in range(2, nrows):
        for j in range(1, ncols):
            take = arr[i - 1] + dp[i - 2][j - arr[i - 1]] if arr[i - 1] <= j else 0
            leave = dp[i - 1][j]
            dp[i][j] = max(take, leave)

    return dp[-1][-1]


if __name__ == "__main__":
    print(max_strawberries([5, 1, 2, 3, 4], 10) == 9)
    print(max_strawberries([10, 50, 10], 100) == 50)
    print(max_strawberries([10, 150, 10], 160) == 150)
    print(max_strawberries([50, 10, 20, 30, 40], 100) == 90)
    print(max_strawberries([50, 10, 60, 20, 30, 90], 120) == 120)
