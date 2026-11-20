# Part C - Question 8: Circular array queue


class EmptyQueueError(Exception):
    pass


class CircularQueue:
    def __init__(self, cap=5):
        self.cap = cap
        self.data = [None] * cap
        self.size = 0
        self.front = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.cap

    def enqueue(self, val):
        if self.is_full():
            raise OverflowError("Queue is full")
        ins_idx = (self.front + self.size) % self.cap
        self.data[ins_idx] = val
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return val

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.data[self.front]


if __name__ == "__main__":
    q = CircularQueue(cap=5)
    for item in [10, 20, 30, 40]:
        q.enqueue(item)
        print(f"Enqueued {item}")

    print("First:", q.first())
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())

    q.enqueue(50)
    q.enqueue(60)
    print("Enqueued 50, 60")
    print("Current first:", q.first())
