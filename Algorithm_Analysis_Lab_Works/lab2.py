# Lakshay - 25BEC056
# Lab 2: Prefix Averages (Quadratic vs Linear Time)

import time
import math
import random


def prefix_average1(arr):
    n = len(arr)
    res = [0.0] * n
    for i in range(n):
        total = 0.0
        for j in range(i + 1):
            total += arr[j]
        res[i] = total / (i + 1)
    return res


def prefix_average2(arr):
    n = len(arr)
    res = [0.0] * n
    total = 0.0
    for i in range(n):
        total += arr[i]
        res[i] = total / (i + 1)
    return res


def median_time(fn, arr, trials=5):
    times = []
    for _ in range(trials):
        t0 = time.perf_counter()
        fn(arr)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    times.sort()
    return times[len(times) // 2]


def validate():
    test_cases = [
        ("Empty", []),
        ("Singleton", [42.0]),
        ("Positive", [1, 2, 3, 4, 5]),
        ("Negative", [-2, -4, -6, -8]),
        ("Mixed", [10, -5, 20, -10, 50]),
    ]
    print("Validation:")
    for desc, seq in test_cases:
        r1 = prefix_average1(seq)
        r2 = prefix_average2(seq)
        match = len(r1) == len(r2) and all(
            math.isclose(a, b, rel_tol=1e-9) for a, b in zip(r1, r2)
        )
        status = "Passed" if match else "Failed"
        print(f"  {desc:<12}: {status} -> {[round(x, 2) for x in r2]}")


def benchmark():
    print("\nBenchmarking (prefix_average1 vs prefix_average2):")
    sizes = [500, 1000, 2000, 4000, 8000]
    for n in sizes:
        arr = [random.uniform(1.0, 100.0) for _ in range(n)]
        t1 = median_time(prefix_average1, arr)
        t2 = median_time(prefix_average2, arr)
        speedup = t1 / t2 if t2 > 0 else 0
        print(f"  n = {n:<5} | O(n^2): {t1:.6f} s | O(n): {t2:.6f} s | Speedup: {speedup:.1f}x")


if __name__ == "__main__":
    validate()
    benchmark()
