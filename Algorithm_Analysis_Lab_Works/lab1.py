# Lab 1: Benchmarking Algorithmic Growth Rates

import time
import math
import random


def list_index(arr, idx):
    return arr[idx]


def bin_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def lin_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def count_pairs(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] > 0:
                count += 1
    return count


def subset_enum(arr):
    res = [[]]
    for x in arr:
        res += [sub + [x] for sub in res]
    return res


def median_time(fn, *args, trials=5):
    times = []
    for _ in range(trials):
        t0 = time.perf_counter()
        fn(*args)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    times.sort()
    return times[len(times) // 2]


def run_benchmarks():
    print("1. Constant Growth O(1) - List Indexing")
    for n in [10000, 50000, 100000, 250000, 500000]:
        arr = list(range(n))
        t = median_time(list_index, arr, n // 2)
        print(f"  n = {n:<8} | Time: {t:.8f} s")

    print("\n2. Logarithmic Growth O(log n) - Binary Search")
    for n in [10000, 50000, 100000, 250000, 500000]:
        arr = list(range(n))
        t = median_time(bin_search, arr, -1)
        norm = t / math.log2(n)
        print(f"  n = {n:<8} | Time: {t:.8f} s | T / log2(n): {norm:.2e}")

    print("\n3. Linear Growth O(n) - Linear Search")
    for n in [10000, 50000, 100000, 200000, 400000]:
        arr = list(range(n))
        t = median_time(lin_search, arr, -1)
        norm = t / n
        print(f"  n = {n:<8} | Time: {t:.8f} s | T / n: {norm:.2e}")

    print("\n4. Linearithmic Growth O(n log n) - Merge Sort")
    for n in [1000, 2000, 4000, 8000, 16000]:
        arr = [random.randint(1, 100000) for _ in range(n)]
        t = median_time(merge_sort, arr)
        norm = t / (n * math.log2(n))
        print(f"  n = {n:<8} | Time: {t:.8f} s | T / (n log2 n): {norm:.2e}")

    print("\n5. Quadratic Growth O(n^2) - Pair Counter")
    for n in [200, 400, 800, 1600, 3200]:
        arr = [random.randint(-100, 100) for _ in range(n)]
        t = median_time(count_pairs, arr)
        norm = t / (n ** 2)
        print(f"  n = {n:<8} | Time: {t:.8f} s | T / n^2: {norm:.2e}")

    print("\n6. Exponential Growth O(2^n) - Subset Enumeration")
    for n in [10, 12, 14, 16, 18, 20]:
        arr = list(range(n))
        t = median_time(subset_enum, arr, trials=3)
        norm = t / (2 ** n)
        print(f"  n = {n:<8} | Time: {t:.8f} s | T / 2^n: {norm:.2e}")

    print("\nSummary:")
    summary = [
        ("List Indexing", "O(1)", "Flat lookup"),
        ("Binary Search", "O(log n)", "Very slow growth"),
        ("Linear Search", "O(n)", "T(n) grows with n"),
        ("Merge Sort", "O(n log n)", "Efficient divide & conquer"),
        ("Pair Counter", "O(n^2)", "4x time when n doubles"),
        ("Subset Enum", "O(2^n)", "Doubles with each +1"),
    ]
    for name, bound, desc in summary:
        print(f"  {name:<16} | {bound:<10} | {desc}")


if __name__ == "__main__":
    run_benchmarks()
