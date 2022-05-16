class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)

        cur = len(self.data) - 1
        parent = cur // 2

        while parent and self.data[cur] > self.data[parent]:
            self.data[cur], self.data[parent] = self.data[parent], self.data[cur]
            cur = parent
            parent //= 2

    def remove(self):
        if len(self.data) <= 1:
            return None

        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        data = self.data.pop(-1)
        self.max_heapify(1)

        return data

    def max_heapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = i * 2

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = i * 2 + 1

        biggest = i

        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[left] > self.data[biggest]:
            biggest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[right] > self.data[biggest]:
            biggest = right

        if biggest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[biggest], self.data[i] = self.data[i], self.data[biggest]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.max_heapify(biggest)
