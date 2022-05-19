from doubly_linked_list import Node, DoublyLinkedList


class LinkedListQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.get_length()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        node = Node(item)
        self.data.insert_at(self.size() + 1, node)

    def dequeue(self):
        return self.data.pop_at(1)

    def peek(self):
        return self.data.get_at(1).data
