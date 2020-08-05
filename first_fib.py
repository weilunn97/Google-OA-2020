def first_fib() -> int:
    """
    Time  : O(N * K^N)
    Space : O(1), WHERE N = NUMBER OF NODES IN THE TREE
    """
    n0 = 1
    n1 = 1

    while True:
        curr = n0 + n1
        if count_factors(curr) == 1000:
            return curr
        n1 = curr
        n0 = n1


def count_factors(curr):
    num_factors = 0
    for div in range(1, curr // 2 + 1):
        quotient = curr / div
        num_factors += 2 * int(quotient == int(quotient))
    print(f"{curr} has {num_factors} factors")
    return num_factors


if __name__ == "__main__":
    print(first_fib() == 498454011879264)
