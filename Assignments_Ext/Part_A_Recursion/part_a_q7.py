# Part A - Question 7: Recursive Tower of Hanoi for n disks


def hanoi(n, src, dst, aux, step=[0]):
    if n == 1:
        step[0] += 1
        print(f"Step {step[0]:>2}: Move disk 1 from {src} -> {dst}")
        return

    hanoi(n - 1, src, aux, dst, step)

    step[0] += 1
    print(f"Step {step[0]:>2}: Move disk {n} from {src} -> {dst}")

    hanoi(n - 1, aux, dst, src, step)


if __name__ == "__main__":
    n_disks = 3
    print(f"Tower of Hanoi solution for n = {n_disks} disks:")
    hanoi(n_disks, "A", "C", "B")
