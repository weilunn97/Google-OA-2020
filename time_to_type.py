def time_to_type(kb: str, text: str) -> int:
    """
    Time  : O(N)
    Space : O(1)
    """
    # KEEP A LOOKUP OF {CHAR : POS}
    kb = {kb[i]: i for i in range(len(kb))}

    # SUM UP THE TIME
    return kb[text[0]] + sum([abs(kb[text[i]] - kb[text[i - 1]]) for i in range(1, len(text))])


if __name__ == "__main__":
    print(time_to_type("abcdefghijklmnopqrstuvwxy", "cba") == 4)
    print(time_to_type("abcdefghijklmnopqrstuvwxy", "dcba") == 6)
