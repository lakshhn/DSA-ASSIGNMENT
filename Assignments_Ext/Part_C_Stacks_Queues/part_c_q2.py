# Part C - Question 2: Stack class using a Python list


class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Cannot pop from an empty stack")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyStackError("Cannot view top of an empty stack")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    s = Stack()
    print("Stack created. is_empty:", s.is_empty())

    s.push(10)
    s.push(20)
    s.push(30)
    print("Pushed 10, 20, 30. Size:", s.size())
    print("Top:", s.top())

    print("Popped:", s.pop())
    print("New top:", s.top())
