from bisect import bisect_right
from typing import List


def closestPrice(pizzas: List[float], toppings: List[float], x: int) -> float:
    """
    Time  : O()
    Space : O(),
    """

    # EDGE CASE - NO TOPPINGS
    if not toppings:
        minDiff = min([abs(p - x) for p in pizzas])
        return [p for p in pizzas if abs(p - x) == minDiff][0]

    # KEEP TRACK OF THE MIN DIFF
    minDiff = 2 ** 64

    # GENERATE ALL POSSIBLE TOPPING COMBINATIONS - O(T^2)
    t = [0] + \
        toppings.copy() + \
        [toppings[i] + toppings[j] for i in range(len(toppings) - 1) for j in range(i + 1, len(toppings))]

    print(f"\n\nPizzas : {sorted(pizzas)}, Target = {x}")
    print(f"tCombi : {t}")

    # FOR EACH PIZZA - O(P LOG T^2)
    for p in sorted(set(pizzas)):

        # FIND THE CLOSEST TOPPING COMBINATION - O(LOG T^2)
        moneyLeft = x - p
        pos = bisect_right(t, moneyLeft)
        if pos == 0:
            print(f"NO MONEY FOR TOPPINGS")
            minDiff = minDiff if abs(minDiff) < abs(moneyLeft - t[0]) else moneyLeft - t[0]
            continue
        if pos == len(t):
            print(f"BOUGHT ALL TOPPINGS")
            minDiff = minDiff if abs(minDiff) < abs(t[-1] - moneyLeft) else t[-1] - moneyLeft
            continue

        # WE KNOW THIS FOR SURE T[POS - 1] < MONEY_LEFT <= T[POS]
        leftDiff = t[pos - 1] - moneyLeft
        diff = t[pos] - moneyLeft
        print(f"Left : {leftDiff} | Curr : {diff}")
        print(f"Inserting Pizza ({p}) @ t[{pos}] = {t[pos]}")

        # UPDATE THE MIN DIFF
        minDiff = minDiff if abs(minDiff) < abs(leftDiff) else leftDiff
        minDiff = minDiff if abs(minDiff) < abs(diff) else diff
        print(f"Min Diff : {minDiff}")

    return x + minDiff


if __name__ == "__main__":
    print(closestPrice([11.75, 12.37, 10], [], 12) == 11.75)
    print(closestPrice([10, 14, 15], [], 13) == 14)
    print(closestPrice([1], [1, 2], 10) == 4)
    print(closestPrice([800, 850, 900], [100, 150], 1000) == 1000)
    print(closestPrice([850, 900], [200, 250], 1000) == 1050)
    print(closestPrice([1100, 900], [200, 250], 1000) == 900)
    print(closestPrice([800, 800, 800, 800], [100], 1000) == 900)
