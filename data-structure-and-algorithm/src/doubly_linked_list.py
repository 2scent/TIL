class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        cur = self.head
        while cur.next.next:
            cur = cur.next
            result.append(cur.data)
        return result

    def reverse(self):
        result = []
        cur = self.tail
        while cur.prev.prev:
            cur = cur.prev
            result.append(cur.data)
        return result

    def get_at(self, pos):
        if pos <= 0 or pos > self.node_count:
            return None

        if pos > self.node_count // 2:
            i = 0
            cur = self.tail
            while i < self.node_count - pos + 1:
                cur = cur.prev
                i += 1
        else:
            i = 0
            cur = self.head
            while i < pos:
                cur = cur.next
                i += 1
        return cur

    def insert_after(self, prev, new_node):
        next = prev.next
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.node_count += 1
        return True

    def insert_before(self, next, new_node):
        prev = next.prev
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.node_count += 1
        return True

    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.node_count + 1:
            return False

        return self.insert_after(self.get_at(pos - 1), new_node)

    def pop_after(self, prev):
        cur = prev.next
        next = cur.next
        prev.next = next
        next.prev = prev

        self.node_count -= 1

        return cur.data

    def pop_before(self, next):
        cur = next.prev
        prev = cur.prev
        prev.next = next
        next.prev = prev

        self.node_count -= 1

        return cur.data

    def pop_at(self, pos):
        if pos < 1 or pos > self.node_count:
            raise IndexError

        return self.pop_after(self.get_at(pos - 1))

    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.node_count += L.node_count
