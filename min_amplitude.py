from collections import deque
from typing import List


def min_amp(arr: List[int]) -> int:
    """
    Time  : O(N), as counting sort is used.
    Space : O(MAX(ARR)), for the intermediate count array in counting sort
    """
    if len(arr) <= 3:
        return 0

    arr = countingSort(arr)
    arr = deque(arr)

    for _ in range(3):
        mid = arr[len(arr) // 2]
        if mid - arr[0] <= arr[-1] - mid:
            arr.pop()
        else:
            arr.popleft()

    return arr[-1] - arr[0]


def countingSort(arr):
    # OFFSET SUCH THAT MIN(ARR) >= 0
    minNum = min(arr)
    if minNum < 0:
        arr = [a - minNum for a in arr]

    # CREATE COUNT OF EACH NUMBER IN ARR
    count = [0] * (max(arr) + 1)
    for a in arr:
        count[a] += 1

    # PREFIX SUM AND RIGHT SHIFT BY 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    count = [0] + count[:-1]

    # SETUP RESULT ARRAY
    res = [None] * len(arr)

    # FILL IT UP
    for a in arr:
        res[count[a]] = a
        count[a] += 1

    # REVERSE OFFSET
    if minNum < 0:
        res = [r + minNum for r in res]

    return res


if __name__ == "__main__":
    print(min_amp([-1, 3, -1, 8, 5, 4]) == 2)
    print(min_amp([10, 10, 3, 4, 10]) == 0)
