# Part C - Question 10: Circular array Deque (Double-Ended Queue)


class EmptyDequeError(Exception):
    pass


class CircularDeque:
    def __init__(self, cap=5):
        self.cap = cap
        self.data = [None] * cap
        self.size = 0
        self.front = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.cap

    def add_first(self, e):
        if self.is_full():
            raise OverflowError("Deque is full")
        self.front = (self.front - 1) % self.cap
        self.data[self.front] = e
        self.size += 1

    def add_last(self, e):
        if self.is_full():
            raise OverflowError("Deque is full")
        back = (self.front + self.size) % self.cap
        self.data[back] = e
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise EmptyDequeError("Deque is empty")
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return val

    def delete_last(self):
        if self.is_empty():
            raise EmptyDequeError("Deque is empty")
        back = (self.front + self.size - 1) % self.cap
        val = self.data[back]
        self.data[back] = None
        self.size -= 1
        return val


if __name__ == "__main__":
    dq = CircularDeque(cap=5)
    dq.add_last(10)
    dq.add_last(20)
    dq.add_first(5)
    print("Added last 10, 20 and added first 5")
    print("Deleted first:", dq.delete_first())
    print("Deleted last:", dq.delete_last())
