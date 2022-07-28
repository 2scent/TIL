from doubly_linked_list import Node, DoublyLinkedList


class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.get_length()

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insert_at(self.size() + 1, node)

    def pop(self):
        return self.data.pop_at(self.size())

    def peek(self):
        return self.data.get_at(self.size()).data
