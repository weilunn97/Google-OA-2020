from bisect import bisect_left
from typing import List


def stores_and_houses(houses: List[int], stores: List[int]) -> List[int]:
    """
    Time  : O(S log S + H log S)
    Space : O(1), where H = len(houses), S = len(stores)
    """
    # SETUP THE RESULT
    res = []

    # SORT THE STORES
    stores = sorted(stores)

    # FOR EACH HOUSE
    for h in houses:
        pos = bisect_left(stores, h)

        # CASE 1 - INSERT AT END
        if pos == len(stores):
            res.append(stores[-1])

        # CASE 2 - INSERT AT FRONT
        elif pos == 0:
            res.append(stores[0])

        else:
            res.append(stores[pos] if stores[pos] - h < h - stores[pos - 1] else stores[pos - 1])

    return res


if __name__ == "__main__":
    print(stores_and_houses([5, 10, 17], [1, 5, 20, 11, 16]) == [5, 11, 16])
    print(stores_and_houses([2, 4, 2], [5, 1, 2, 3]) == [2, 3, 2])
    print(stores_and_houses([4, 8, 1, 1], [5, 3, 1, 2, 6]) == [3, 6, 1, 1])
