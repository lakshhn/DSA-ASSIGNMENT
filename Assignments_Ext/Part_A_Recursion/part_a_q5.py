# Part A - Question 5: Naive recursive Fibonacci and call counts for n=5

call_counts = {}


def fib(n):
    call_counts[n] = call_counts.get(n, 0) + 1

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def print_recursion_tree_for_5():
    tree = """
Recursion Tree for fib(5):

                       fib(5)
                     /        \
              fib(4)            fib(3)
             /      \          /      \
        fib(3)      fib(2)    fib(2)  fib(1)
       /     \      /    \    /    \
    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
    /    \
 fib(1) fib(0)
"""
    print(tree)


if __name__ == "__main__":
    call_counts.clear()
    val = fib(5)

    print(f"fib(5) = {val}")
    print_recursion_tree_for_5()

    print("Call counts per subproblem:")
    for arg in sorted(call_counts.keys(), reverse=True):
        print(f"  fib({arg}) called {call_counts[arg]} time(s)")
