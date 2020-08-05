from collections import Counter


def str_to_num(s):
    charCounts = [0] * 26
    for char in s:
        charCounts[ord(char) - ord('a')] += 1
    for count in charCounts:
        if count > 0:
            return count


def countNumsSmallerThanMe(num, countA):
    return sum(countA.get(i, 0) for i in range(1, num))


def compare_strings(A: str, B: str) -> int:
    """
    Time  : O(A + B)
    Space : O(1)
    """
    # CONVERT A AND B INTO A LIST OF NUMBERS - O(A + B)
    A = [str_to_num(s) for s in A.split(" ")]
    B = [str_to_num(s) for s in B.split(" ")]

    # GET A COUNT OF SIZES IN A - O(A)
    A = Counter(A)

    # SETUP THE RESULT - O(B)
    return [countNumsSmallerThanMe(num, A) for num in B]


if __name__ == "__main__":
    print(compare_strings("abcd aabc bd", "aaa aa") == [3, 2])
    print(compare_strings("aaa bb cc", "a bbb ccc") == [0, 2, 2])
