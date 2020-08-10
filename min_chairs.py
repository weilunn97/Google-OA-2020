from heapq import heappush, heappop
from typing import List


def min_chairs(start: List[int], end: List[int]) -> int:
    """
    Time  : O(N log N)
    Space : O(N)
    """
    # THE ENDING TIMES OF ALL GUESTS CURRENTLY IN THE PARTY
    ending = []

    # NUMBER OF CHAIRS NEEDED THUS FAR
    chairs = 0

    # PROCESS EACH GUEST, BY ARRIVAL TIMES
    for s, e in sorted(zip(start, end)):

        # NO GUESTS IN PARTY / WE CAN KICK 1 GUEST OUT TO MAKE SPACE
        if not ending or s < ending[0]:
            heappush(ending, e)
            chairs += 1

        # ADD 1 CHAIR
        else:
            heappop(ending)
    return chairs


if __name__ == "__main__":
    print(min_chairs([], []) == 0)
    print(min_chairs([1], [5]) == 1)
    print(min_chairs([1, 2, 3, 5], [5, 5, 8, 9]) == 3)
    print(min_chairs([1, 2, 3, 5, 1], [5, 5, 8, 9, 10]) == 4)
    print(min_chairs([1, 2, 6, 5, 3], [5, 5, 7, 6, 8]) == 3)
