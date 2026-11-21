# Lakshay - 25BEC056
# Part D - Question 3: Singly Linked List operations (insert_first, insert_last, delete_first, traversal)


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert_first(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def insert_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def delete_first(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list")
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return val

    def traverse(self):
        curr = self.head
        elements = []
        while curr:
            elements.append(curr.val)
            curr = curr.next
        return elements


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_first(20)
    sll.insert_first(10)
    sll.insert_last(30)
    sll.insert_last(40)
    print("List after insertions:", sll.traverse())
    print("Deleted first:", sll.delete_first())
    print("List after delete_first:", sll.traverse())
