from heapq import heappush, heappop
from typing import List


def min_chairs(start: List[int], end: List[int]) -> int:
    """
    Time  : O(N log N)
    Space : O(N)
    """

    # EDGE CASE
    if len(start) < 2:
        return len(start)

    # SORT BY START TIME
    intervals = sorted([s, e] for s, e in zip(start, end))

    # SETUP A MIN HEAP TO STORE END TIMES
    # ITS SIZE REPRESENTS THE CURRENT NUMBER OF GUESTS
    endTimes = []
    minChairs = 0

    # PROCESS EACH INTERVAL
    for i in intervals:

        print(endTimes)

        # RECORD THE CURRENT NUMBER OF GUESTS
        minChairs = max(minChairs, len(endTimes))

        # SEE IF WE CAN EXPEL ANY GUESTS
        while endTimes and endTimes[0] <= i[0]:
            heappop(endTimes)

        # ADD THE CURRENT GUEST IN
        heappush(endTimes, i[1])

    return minChairs


if __name__ == "__main__":
    print(min_chairs([1, 2, 6, 5, 3], [5, 5, 7, 6, 8]) == 3)
