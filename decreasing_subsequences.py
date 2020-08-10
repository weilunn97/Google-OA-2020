from bisect import bisect_right
from typing import List


def decreasing_subsequences(arr: List[int]) -> int:
    """
    Time : O(N log N)
    Space : O(N)
    """
    buckets = []
    for a in arr:
        pos = bisect_right(buckets, a)
        if pos == len(buckets):
            buckets.append(a)
        else:
            buckets[pos] = a
    return len(buckets)


if __name__ == "__main__":
    print(decreasing_subsequences([]) == 0)
    print(decreasing_subsequences([5]) == 1)
    print(decreasing_subsequences([5, 2, 4, 3, 1, 6]) == 3)
    print(decreasing_subsequences([2, 9, 12, 13, 4, 7, 6, 5, 10]) == 4)
    print(decreasing_subsequences([1, 1, 1]) == 3)
