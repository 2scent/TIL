class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def get(self, index):
        node = self.head
        count = 0

        while count < index:
            node = node.next
            count += 1

        return node

    def delete(self, index):
        if index == 0:
            del_node = self.head
            self.head = self.head.next
            return del_node.data

        prev = self.get(index - 1)
        del_node = prev.next
        prev.next = del_node.next
        return del_node.data


n, k = map(int, input().split())

L = LinkedList()
for i in range(1, n + 1):
    L.insert(i)

result = []

# 구현한 리스트의 인덱스는 0부터 시작하기 때문에 k-1을 저장한다.
idx = k - 1
while L.head:
    # 인덱스가 리스트의 범위를 초과하면 다시 처음부터 접근해야 하기 때문에 나머지 연산을 한다.
    idx %= n
    result.append(str(L.delete(idx)))
    # 사람을 한 명 지웠으므로 k가 아닌 k-1을 더해 다음 인덱스를 가리킨다.
    idx += (k - 1)
    n -= 1

print('<', end='')
print(', '.join(result), end='')
print('>')
