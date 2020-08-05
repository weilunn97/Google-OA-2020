from typing import List


def treasure_hunt(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    return bt(grid, 0, 0, 0, n - 1, 0, 0, m, n)


def bt(grid, i1, j1, i2, j2, coins1, coins2, m, n):
    # BASE CASE - OOB OR MEET
    if min(i1, j1, i2, j2) < 0 or max(i1, i2) >= m or max(j1, j2) >= n or (i1 == i2 and j1 == j2):
        return 0

    print(f"R1 : [{i1},{j1}] | {coins1} coins")
    print(f"R2 : [{i2},{j2}] | {coins2} coins")

    # BASE CASE - BOTH REACH TARGET
    if i1 == i2 == m - 1 and j1 == 0 and j2 == n - 1:
        print(f"TARGET HIT!!")
        return coins1 + coins2 + grid[i1][j1] + grid[i2][j2]

    # ROBOTS ATTACK
    coin1, coin2 = grid[i1][j1], grid[i2][j2]

    return max(
        bt(grid, i1 + 1, j1 - 1, i2 + 1, j2 - 1, coins1 + coin1, coins2 + coin2, m, n),
        bt(grid, i1 + 1, j1 - 1, i2 + 1, j2 + 1, coins1 + coin1, coins2 + coin2, m, n),
        bt(grid, i1 + 1, j1 - 1, i2 + 1, j2, coins1 + coin1, coins2 + coin2, m, n),

        bt(grid, i1 + 1, j1 + 1, i2 + 1, j2 - 1, coins1 + coin1, coins2 + coin2, m, n),
        bt(grid, i1 + 1, j1 + 1, i2 + 1, j2 + 1, coins1 + coin1, coins2 + coin2, m, n),
        bt(grid, i1 + 1, j1 + 1, i2 + 1, j2, coins1 + coin1, coins2 + coin2, m, n),

        bt(grid, i1 + 1, j1, i2 + 1, j2 - 1, coins1 + coin1, coins2 + coin2, m, n),
        bt(grid, i1 + 1, j1, i2 + 1, j2 + 1, coins1 + coin1, coins2 + coin2, m, n),
        bt(grid, i1 + 1, j1, i2 + 1, j2, coins1 + coin1, coins2 + coin2, m, n),
    )


if __name__ == "__main__":
    m, n = input().split(" ")
    m, n = int(m), int(n)
    if n < 2:
        print(-1)
    else:
        nums = [int(n) for n in input().split(" ")]
        grid = [nums[i: i + n] for i in range(0, len(nums), n)]
        print(treasure_hunt(grid))
