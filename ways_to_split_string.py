from collections import Counter


def ways_to_split_string(s: str) -> int:
    """
    Time  : O(N), linear pass through our string
    Space : O(N), to keep a count of elements for each string
    """
    # EDGE CASE
    if len(s) < 2:
        return 0

    # SETUP A PARTITION OF S[0], S[1:] FIRST
    front = Counter(s[0])
    back = Counter(s[1:])
    count = 0

    # LOOP TILL OOB
    for i in range(len(s) - 1):
        print(front, back)
        # CHECK THE UNIQUE CHARS IN FRONT AND BACK
        count += int(len(front) == len(back))

        # MOVE THE PARTITION
        front[s[i + 1]] = front.get(s[i + 1], 0) + 1
        back[s[i + 1]] = back.get(s[i + 1], 0) - 1

        # REMOVE FROM BACK IF NECESSARY
        if back.get(s[i + 1]) == 0:
            del back[s[i + 1]]

    return count


if __name__ == "__main__":
    print(ways_to_split_string("aaaa") == 3)
    print(ways_to_split_string("bac") == 0)
    print(ways_to_split_string("ababa") == 2)
