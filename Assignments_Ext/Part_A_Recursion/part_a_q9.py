# Lakshay - 25BEC056
# Part A - Question 9: Converting tail-recursive sum to iterative version


def sum_tail(arr, idx=0, acc=0):
    if idx >= len(arr):
        return acc
    return sum_tail(arr, idx + 1, acc + arr[idx])


def sum_iter(arr):
    acc = 0
    for val in arr:
        acc += val
    return acc


if __name__ == "__main__":
    sample = [5, 10, 15, 20, 25]
    print(f"Input: {sample}")
    print("Tail-recursive result:", sum_tail(sample))
    print("Iterative result:     ", sum_iter(sample))
