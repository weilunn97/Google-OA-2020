from typing import List


def water_flowers(items: List[int], c1: int, c2: int) -> int:
    """
    Time  : O(N)
    Space : O(1)
    """
    # EDGE CASE
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return 1

    # SETUP DOUBLE POINTERS
    front, back = 0, len(items) - 1
    fVol, bVol = c1, c2
    refills = 2  # FOR INITIAL FILL

    # LOOP TILL CROSS
    while front < back:
        # WATER FRONT
        refills += int(fVol < items[front])
        fVol = c1 if fVol < items[front] else fVol
        fVol -= items[front]

        # WATER BACK
        refills += int(bVol < items[back])
        bVol = c2 if bVol < items[back] else bVol
        bVol -= items[back]

        front += 1
        back -= 1

    # FINAL WATERING
    if front == back:
        refills += int(fVol + bVol < items[front])

    return refills


if __name__ == "__main__":
    print(water_flowers([2, 4, 5, 1, 2], 5, 7) == 3)
    print(water_flowers([1, 1, 1, 1, 1, 1, 1], 5, 7) == 2)
    print(water_flowers([5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7], 5, 7) == 11)
    print(water_flowers([5], 5, 7) == 1)
    print(water_flowers([], 5, 7) == 0)
