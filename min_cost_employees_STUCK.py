from collections import defaultdict
from typing import List


def min_hire_employees(hire: int, sal: int, fire: int, nums: List[int]) -> int:
    """
    Time  : O(N^2)
    Space : O(N)
    """

    # SETUP DP
    dp = [2 ** 64] * len(nums)
    dp[0] = nums[0] * (hire + sal)

    # FILL THE CELLS
    for i in range(1, len(dp)):
        print()
        for j in range(i - 1, -1, -1):

            # CASE 1 - HIRING MORE WORKERS
            if nums[j] < nums[i]:
                numHired = nums[i] - nums[j]
                extraCost = numHired * (hire + sal * (i - j))
                dp[i] = min(dp[i], dp[j] + extraCost)
                print(f"{nums[j]}, {nums[i]} | HIRE {numHired} | EXTRA {extraCost}")

            # CASE 2 - FIRING EXISTING WORKERS FROM PREVIOUS MONTH
            elif nums[j] > nums[i]:
                numFired = nums[j] - nums[i]
                extraCost = numFired * (fire - sal * (i - j))
                dp[i] = min(dp[i], dp[j] + extraCost)
                print(f"{nums[j]}, {nums[i]} | FIRE {numFired} | EXTRA {extraCost}")

            # CASE 3 - NO CHANGE FROM PREVIOUS MONTH
            else:
                dp[i] = min(dp[i], dp[j])

            print(dp)

    print(dp, sum(dp))
    return sum(dp)


def solver(hire: int, sal: int, fire: int, nums: List[int]) -> int:
    dp = {0: 0}
    for req in nums:
        tmp = defaultdict(lambda: float('inf'))
        for key in dp:
            if key >= req:
                for i in range(req, key + 1):
                    tmp[i] = min(tmp[i], dp[key] + i * sal + (key - i) * fire)
            else:
                tmp[req] = min(tmp[req], dp[key] + req * sal + (req - key) * hire)
        dp = tmp
    print()
    print(dp)
    print(min(dp.values()))
    return min(dp.values())


if __name__ == "__main__":
    print(min_hire_employees(5, 10, 5, [3, 5, 2, 6, 1]) == solver(5, 10, 5, [3, 5, 2, 6, 1]))
