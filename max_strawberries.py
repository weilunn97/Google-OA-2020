from typing import List


def max_strawberries(arr: List[int], num: int) -> int:
    """
    Time  : O(MN)
    Space : O(MN), where M = len(arr) and N = num
    """
    nrows, ncols = len(arr) + 1, num + 1

    # LET DP[I][J] = MAX STRAWBERRIES GIVEN ARR[:I] AND NUM = J
    dp = [[0 for _ in range(ncols)] for _ in range(nrows)]

    # GET THE MAXIMUM
    max_straw = 0

    # FILL ROW 1
    for j in range(1, ncols):
        dp[1][j] = arr[0] if arr[0] <= j else 0
        max_straw = max(max_straw, dp[1][j])

    # FILL OTHER CELLS
    for i in range(2, nrows):
        for j in range(1, ncols):
            # PICK IT IFF THERE'S SPACE
            pick = dp[i - 2][j - arr[i - 1]] + arr[i - 1] if arr[i - 1] <= j else 0
            leave = dp[i - 1][j]
            dp[i][j] = max(pick, leave)
            max_straw = max(max_straw, dp[i][j])

    return max_straw


if __name__ == "__main__":
    print(max_strawberries([5, 1, 2, 3, 4], 10) == 9)
    print(max_strawberries([10, 50, 10], 100) == 50)
    print(max_strawberries([10, 150, 10], 160) == 150)
    print(max_strawberries([50, 10, 20, 30, 40], 100) == 90)
    print(max_strawberries([50, 10, 60, 20, 30, 90], 120) == 120)
