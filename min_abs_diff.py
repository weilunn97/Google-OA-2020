from typing import List


def min_abs_diff(items: List[int]) -> int:
    """
    Time  :
    Space :
    """
    # EDGE CASE
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return items[0]

    total = sum(items)
    minDiff = [2 ** 64]
    memo = dict()
    calls = [0]
    backtrack(0, items, 0, total, minDiff, memo, calls)
    return minDiff[0]


def backtrack(i, items, curr, total, minDiff, memo, calls):
    key = f"{i},{curr}"

    # HIT MEMO
    if memo.get(key) is not None:
        return memo.get(key)

    # BASE CASE - REACHED THE END OF ARRAY
    if i == len(items):
        # print(f"Curr : {curr} | Total : {total} | Diff : {2 * curr - total}")
        minDiff[0] = min(minDiff[0], abs(2 * curr - total))
        return minDiff[0]

    # CHOOSE TO TAKE IT OR LEAVE IT
    calls[0] += 2
    memo[key] = min(backtrack(i + 1, items, curr + items[i], total, minDiff, memo, calls),
                    backtrack(i + 1, items, curr, total, minDiff, memo, calls))
    return memo.get(key)


if __name__ == "__main__":
    print(min_abs_diff([1, 2, 3, 4, 5]) == 1)
    print(min_abs_diff([10, 10, 9, 9, 2]) == 0)
    print(min_abs_diff([10]) == 10)
    print(min_abs_diff([]) == 0)
