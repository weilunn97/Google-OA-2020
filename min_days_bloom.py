from typing import List


def min_days_bloom(roses: List[int], k: int, n: int) -> int:
    """
    Time  : O(N log MAX)
    Space : O(N),
    WHERE N = LEN(ROSES), AND MAX = MAX(ROSES)
    """
    start, end = 0, max(roses)
    best = None
    while start < end:
        mid = start + int((end - start) / 2)
        if is_valid(roses, k, n, mid):
            best = mid
            end = mid - 1
        else:
            start = mid + 1

    return best


def is_valid(roses, k, n, day):
    bloomed = [int(r <= day) for r in roses]
    bouquets = 0
    consec = 0
    for b in bloomed:
        if b:
            consec += 1
            if consec == k:
                bouquets += int(consec >= k)
                consec = 0
        else:
            consec = 0
    return bouquets == n


if __name__ == "__main__":
    print(min_days_bloom([1, 2, 4, 9, 3, 4, 1], 2, 2) == 4)
