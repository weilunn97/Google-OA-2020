from collections import defaultdict
from typing import List


def statistics(fruits: List[str]) -> List[str]:
    """
    Time  : O(N)
    Space : O(N), where N = len(fruits)
    """
    # KEEPS TRACK OF A FRUIT'S [MIN, MAX, COUNT, SUM, MEAN]
    d = defaultdict(lambda: [2 ** 64, -2 ** 64, 0, 0, 0])

    # ADD EACH FRUIT INTO THE DICT - O(N)
    for f in fruits:
        fruit, price = f.split(" ")
        price = int(price)
        d[fruit][0] = min(d[fruit][0], price)
        d[fruit][1] = max(d[fruit][1], price)
        d[fruit][2] += 1
        d[fruit][3] += price
        d[fruit][4] = d[fruit][3] / d[fruit][2]
        d[fruit][4] = int(d[fruit][4]) if int(d[fruit][4]) == d[fruit][4] else d[fruit][4]

    # FOR EACH FRUIT, CALCULATE THE MIN, MAX, MEAN - O(N)
    return [f"{f} {d[f][0]} {d[f][1]} {d[f][-1]}" for f in sorted(d.keys())]


def computeStats(prices: List[int]) -> str:
    minimum = min(prices)
    maximum = max(prices)
    mean = sum(prices) / len(prices)
    mean = int(mean) if int(mean) == mean else mean
    return f"{minimum} {maximum} {mean}"


if __name__ == "__main__":
    print(statistics(["banana 90", "apple 100", "apple 260"]) == ["apple 100 260 180", "banana 90 90 90"])
    print(statistics(["grapefruit 120", "grape 200", "grapefruit 150", "grapefruit 150", "grape 180"]) == [
        "grape 180 200 190", "grapefruit 120 150 140"])
    print(statistics(["apple 100", "apple 101"]) == ["apple 100 101 100.5"])
