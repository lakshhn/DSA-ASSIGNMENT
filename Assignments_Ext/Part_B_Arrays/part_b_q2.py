# Lakshay - 25BEC056
# Part B - Question 2: Shallow copy vs Deep copy

import copy


if __name__ == "__main__":
    orig = [[1, 2, 3], ["a", "b", "c"]]

    shallow = copy.copy(orig)
    deep = copy.deepcopy(orig)

    print("Original state:")
    print("  orig:   ", orig)
    print("  shallow:", shallow)
    print("  deep:   ", deep)

    orig[0][0] = 999

    print("\nAfter mutating inner list orig[0][0] = 999:")
    print("  orig:   ", orig)
    print("  shallow:", shallow, "<- affected because inner list is shared")
    print("  deep:   ", deep, "<- unchanged")
