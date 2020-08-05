def maximum_time(t: str) -> str:
    """
    Time  : O(1)
    Space : O(1)
    """
    if t[0] == '?':
        if t[1] == '?' or int(t[1]) <= 3:
            d0 = 2
        else:
            d0 = 1
    else:
        d0 = t[0]

    if t[1] == '?':
        if d0 == '2':
            d1 = 3
        else:
            d1 = 9
    else:
        d1 = t[1]

    d3 = 5 if t[3] == '?' else t[3]
    d4 = 9 if t[4] == '?' else t[4]

    return f"{d0}{d1}:{d3}{d4}"


if __name__ == "__main__":
    print(maximum_time("?4:5?") == "14:59")
    print(maximum_time("23:5?") == "23:59")
    print(maximum_time("2?:22") == "23:22")
    print(maximum_time("0?:??") == "09:59")
    print(maximum_time("1?:3?") == "19:39")
    print(maximum_time("?9:?3") == "19:53")
    print(maximum_time("?0:?3") == "20:53")
