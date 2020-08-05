from typing import List


def relative_sort(x: List[int], y: List[int]) -> int:
    """
    Time  : O(X + Y)
    Space : O(1)
    """

    # COUNT THE SWAPS
    swaps = 0
    n = len(x)

    # SETUP A POINTER
    for i in range(n - 1):
        if x[i] >= x[i + 1] or y[i] >= y[i + 1]:
            x[i], y[i] = y[i], x[i]
            swaps += 1
            if x[i] >= x[i + 1] or y[i] >= y[i + 1]:
                return -1

    print(swaps)
    return swaps


if __name__ == "__main__":
    print(relative_sort([1,4,4,9], [2,3,5,10]) == 1)
