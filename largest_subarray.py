from typing import List


def largest_subarray(arr: List[int], k: int) -> List[int]:
    """
    Time  : O(N), 1 pass to get maximum index, another to slice the array
    Space : O(1)
    """

    # FIND THE INDEX OF THE MAXIMUM ELEMENT - O(N)
    maxNum, maxIndex = arr[0], 0

    for i in range(len(arr) - k + 1):
        if arr[i] > maxNum:
            maxNum = arr[i]
            maxIndex = i

    # GET THE SUB-ARRAY FROM THIS MAX INDEX - O(N)
    return arr[maxIndex: maxIndex + k]


if __name__ == "__main__":
    print(largest_subarray([1, 4, 3, 2, 5], 4) == [4, 3, 2, 5])
    print(largest_subarray([1, 4, 3, 2, 5], 3) == [4, 3, 2])
    print(largest_subarray([1, 4, 3, 2, 5], 2) == [4, 3])
    print(largest_subarray([1, 4, 3, 2, 5], 1) == [5])
