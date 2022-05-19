class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = None
        self.tail = None

    # 리스트 순회
    def traverse(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    # 리스트 길이 반환
    def get_length(self):
        return self.node_count

    # 특정 원소 참조
    def get_at(self, pos):
        if pos <= 0 or pos > self.node_count:
            return None

        i = 1
        cur = self.head
        while i < pos:
            cur = cur.next
            i += 1
        return cur

    # 원소 삽입
    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.node_count + 1:
            return False

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            if pos == self.node_count + 1:
                prev = self.tail
            else:
                prev = self.get_at(pos - 1)
            new_node.next = prev.next
            prev.next = new_node

        if pos == self.node_count + 1:
            self.tail = new_node

        self.node_count += 1
        return True

    # 원소 삭제
    def pop_at(self, pos):
        if pos < 1 or pos > self.node_count:
            raise IndexError

        if pos == 1:
            cur = self.head
            self.head = cur.next
            if self.node_count == 1:
                self.tail = self.head
        else:
            prev = self.get_at(pos - 1)
            cur = prev.next
            prev.next = cur.next
            if pos == self.node_count:
                self.tail = prev

        self.node_count -= 1
        return cur.data

    # 리스트 병합
    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.node_count += L.node_count
