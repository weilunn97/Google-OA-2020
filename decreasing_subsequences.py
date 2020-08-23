from bisect import bisect_right
from typing import List


def decreasing_subsequences(arr: List[int]) -> int:
    res = []
    for i in range(len(arr)):
        pos = bisect_right(res, arr[i])
        if pos == len(res):
            res.append(arr[i])
        else:
            res[pos] = arr[i]

    return len(res)


if __name__ == "__main__":
    print(decreasing_subsequences([]) == 0)
    print(decreasing_subsequences([5]) == 1)
    print(decreasing_subsequences([5, 2, 4, 3, 1, 6]) == 3)
    print(decreasing_subsequences([2, 9, 12, 13, 4, 7, 6, 5, 10]) == 4)
    print(decreasing_subsequences([1, 1, 1]) == 3)
    print(decreasing_subsequences([5, 7, 1, 5, 2, 7]) == 3)
    print(decreasing_subsequences([5, 7, 7, 5, 5, 3, 1, 5]) == 4)
