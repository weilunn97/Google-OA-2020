from typing import List


def min_days_bloom(roses: List[int], k: int, n: int) -> int:
    """
    Time  : O(N log MAX)
    Space : O(N),
    WHERE N = LEN(ROSES), AND MAX = MAX(ROSES)
    """

    # EDGE CASE - NOT ENOUGH FLOWERS TO MAKE N BOUQUETS
    if len(roses) < k * n:
        return -1

    # START A BINARY SEARCH FOR THE MINIMUM DAY NEEDED TO MAKE N BOUQUETS
    lo, hi = 0, len(roses) - 1

    while lo < hi:

        # GET MIDDLE DAY
        mid = lo + (hi - lo) // 2

        # LINEAR SCAN ROSES TO SEE IF WE CAN MAKE N BOUQUETS OF K FLOWERS EACH
        canMakeNBouquets = canMake(roses, k, n, mid)
        print(f"Day {mid} : {canMakeNBouquets}")

        # CASE 1 - WE'VE (MORE THAN) ENOUGH ROSES TO MAKE N BOUQUETS
        if canMakeNBouquets:
            hi = mid

        # CASE 2 - WE NEED MORE ROSES TO MAKE N BOUQUETS
        else:
            lo = mid + 1

    return lo


def canMake(roses: List[int], k: int, n: int, day: int) -> bool:
    bouquets = 0
    currFlowers = 0
    for r in roses:
        if r <= day:
            currFlowers += 1
            if currFlowers == k:
                bouquets += 1
                currFlowers = 0
        else:
            currFlowers = 0

    return bouquets == n


if __name__ == "__main__":
    print(min_days_bloom([1, 2, 4, 9, 3, 4, 1], 2, 2) == 4)
