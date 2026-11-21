# Lakshay - 25BEC056
# Part A - Question 3: In-place sequence reversal using start and stop indices


def reverse_inplace(arr, start, stop):
    if start >= stop:
        return

    print(f"Swap arr[{start}]={arr[start]} with arr[{stop}]={arr[stop]} -> state: {arr}")
    arr[start], arr[stop] = arr[stop], arr[start]

    reverse_inplace(arr, start + 1, stop - 1)


if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50, 60]
    print(f"Original sequence: {nums}")
    print("\nTrace of recursive swaps:")
    reverse_inplace(nums, 0, len(nums) - 1)
    print(f"\nFinal reversed sequence: {nums}")
