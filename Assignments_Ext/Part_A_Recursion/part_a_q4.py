# Part A - Question 4: Recursive check if a sequence is sorted non-decreasingly


def is_sorted(arr, idx=0):
    if len(arr) <= 1 or idx >= len(arr) - 1:
        return True

    if arr[idx] > arr[idx + 1]:
        return False

    return is_sorted(arr, idx + 1)


if __name__ == "__main__":
    seq1 = [2, 5, 8, 12, 19, 25]
    seq2 = [2, 5, 15, 8, 19, 25]
    seq3 = [10]
    seq4 = []

    print(f"{seq1} -> sorted: {is_sorted(seq1)}")
    print(f"{seq2} -> sorted: {is_sorted(seq2)}")
    print(f"{seq3} -> sorted: {is_sorted(seq3)}")
    print(f"{seq4} -> sorted: {is_sorted(seq4)}")
