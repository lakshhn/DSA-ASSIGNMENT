# Lakshay - 25BEC056
# Part A - Question 2: Recursive factorial, sum, and power


def fact(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * fact(n - 1)


def sum_n(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    return n + sum_n(n - 1)


def power(x, n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return x * power(x, n - 1)


if __name__ == "__main__":
    print("Factorial of 5:", fact(5))
    print("Sum of first 10 natural numbers:", sum_n(10))
    print("2 raised to power 8:", power(2, 8))
