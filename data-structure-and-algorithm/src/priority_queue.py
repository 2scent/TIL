from doubly_linked_list import Node, DoublyLinkedList


# 값이 작을수록 우선순위가 높은 큐
class PriorityQueue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.get_length()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        node = Node(item)
        cur = self.data.head
        while cur.next.next and item >= cur.next.data:
            cur = cur.next
        self.data.insert_after(cur, node)

    def dequeue(self):
        return self.data.pop_at(1)

    def peek(self):
        return self.data.get_at(1).data
