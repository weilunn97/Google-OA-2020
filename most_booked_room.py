from collections import Counter
from typing import List


def most_booked_room(items: List[str]) -> str:
    """
    Time  : O(N)
    Space : O(N)
    """
    # EDGE CASE
    if len(items) == 0:
        return ""

    # KEEP ONLY THE CHECK-INS
    items = Counter([i[1:] for i in items if i[0] == '+'])

    # GET ALL ROOMS WITH THE HIGHEST BOOKING - O(N)
    items = [k for k, v in items.items()]

    # GET THE ROOM WITH THE SMALLEST LEXICAL NAME - O(N)
    smallest = items[0]
    for i in items:
        smallest = i if i < smallest else smallest

    return smallest


if __name__ == "__main__":
    print(most_booked_room(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E"]) == "1A")
    print(most_booked_room(["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", "-1A", "+1A"]) == "1A")
    print(most_booked_room(
        ["+2A", "-2A", "+2A", "-2A", "+2A", "-2A", "+2B", "-2B", "+2B", "+1E", "-1E", "+1E", "-1E", "-2B", "+2B", "+2A",
         "-2A", "-2B", "+2B", "-2B", "+1E", "-1E", "+1E", "-1E"]) == "1E")
