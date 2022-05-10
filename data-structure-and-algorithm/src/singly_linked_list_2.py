class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = Node(None)  # dummy node
        self.tail = None
        self.head.next = self.tail

    # 리스트 순회
    def traverse(self):
        result = []
        cur = self.head
        while cur.next:
            cur = cur.next
            result.append(cur.data)
        return result

    # 리스트 길이 반환
    def get_length(self):
        return self.node_count

    # 특정 원소 참조
    def get_at(self, pos):
        if pos < 0 or pos > self.node_count:
            return None

        i = 0
        cur = self.head
        while i < pos:
            cur = cur.next
            i += 1
        return cur

    # 특정 원소 다음에 원소 삽입
    def insert_after(self, prev, new_node):
        new_node.next = prev.next
        if prev.next is None:
            self.tail = new_node
        prev.next = new_node
        self.node_count += 1
        return True

    # 특정 원소 삽입
    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.node_count + 1:
            return False

        if pos != 1 and pos == self.node_count + 1:
            prev = self.tail
        else:
            prev = self.get_at(pos - 1)
        return self.insert_after(prev, new_node)

    # 특정 원소 다음의 원소 삭제
    def pop_after(self, prev):
        if prev.next is None:
            return None

        cur = prev.next
        prev.next = cur.next
        if cur.next is None:
            self.tail = prev
        self.node_count -= 1

        return cur.data

    # 특정 원소 삭제
    def pop_at(self, pos):
        if pos < 1 or pos > self.node_count:
            raise IndexError

        return self.pop_after(self.get_at(pos - 1))

    # 리스트 병합
    def concat(self, L):
        self.tail.next = L.head.next
        if L.tail:
            self.tail = L.tail
        self.node_count += L.node_count
