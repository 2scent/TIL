# 알고리즘 / 기술면접 완전 정복 올인원

> 본 문서는 [알고리즘 / 기술면접 완전 정복 올인원](https://storage.googleapis.com/static.fastcampus.co.kr/prod/uploads/202104/163434-24/[%ED%8C%A8%EC%8A%A4%ED%8A%B8%EC%BA%A0%ED%8D%BC%EC%8A%A4]-%EA%B5%90%EC%9C%A1%EA%B3%BC%EC%A0%95%EC%86%8C%EA%B0%9C%EC%84%9C-%EC%98%AC%EC%9D%B8%EC%9B%90-%ED%8C%A8%ED%82%A4%EC%A7%80---%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5.pdf) 강의를 보고 제 주관대로 정리한 글입니다.

---

# 배열 (Array)

- 데이터를 나열하고, 각 데이터에 인덱스로 접근할 수 있는 자료구조
- 파이썬에서는 리스트 타입으로 배열을 이용할 수 있는데, 여러 추가 기능을 제공하기 때문에 기본적인 배열과는 차이가 있을 수 있음

## 배열의 특징

- 같은 종류의 데이터를 순차적으로 저장 및 관리하기 용이하다.
- 데이터의 빠른 접근이 가능하다.
  - 처음 데이터 위치에서 인덱스를 이용하여 상대적인 위치로 접근
- 데이터 추가, 삭제가 어렵다.
  - 배열의 최대 길이는 미리 정해놔야 함
  - 배열의 중간에 데이터를 추가하거나 삭제하려면, 그 뒤의 데이터들도 이동해야하기 때문에 효율적이지 못함
- <b>배열의 첫 번째 인덱스는 0</b>

## 예시

```python
arr1 = [1, 2, 3, 4, 5]
print(arr1[3]) # 4

arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr2[2][0]) # 7
```

# 큐 (Queue)

- 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 자료구조
- FIFO(First-In, First-Out)
- [큐 동작 확인](https://visualgo.net/en/list?mode=Queue)

## 큐의 주요 기능

- **enqueue**: 큐 뒤쪽에 데이터 삽입
- **dequeue**: 큐 앞쪽의 데이터를 삭제 및 반환
- **peek**: 큐 앞쪽의 데이터 조회

## 파이썬 리스트를 이용한 큐의 간단한 구현

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.items:
            return self.items.pop()
        print('Queue is empty!')

    def peek(self):
        if self.items:
            return self.items[-1]
        print('Queue is empty!')
```

# 스택 (Stack)

- 데이터를 한쪽에서만 넣거나 뺄 수 있는 자료구조
- LIFO(Last-In, First-Out) 또는 FILO(First-In, Last-Out)
- [스택 동작 확인](https://visualgo.net/en/list?mode=Stack)

## 스택의 주요 기능

- **push**: 스택에 데이터 삽입
- **pop**: 스택에서 데이터 삭제 및 반환
- **peek**: 스택의 데이터 조회

## 파이썬 리스트를 이용한 스택의 간단한 구현

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        print('Stack is empty!')

    def peek(self):
        if self.items:
            return self.items[-1]
        print('Stack is empty!')
```

# 링크드 리스트 (Linked List)

## 링크드 리스트의 특징

- 연결 리스트라고도 함
- 배열의 순차적인 데이터 구조와 다르게 떨어진 데이터들을 포인터로 연결(Link)해서 관리하는 자료구조

## 링크드 리스트의 용어

- 노드 (Node): 데이터의 기본 저장 단위, (데이터, 포인터)로 구성
- 포인터 (Pointer): 각 노드에서 다음 또는 이전 노드를 가리키는 역할

## 전통적인 배열과 비교했을 때, 링크드 리스트의 장단점

### 장점

- 배열과 다르게 미리 저장 공간을 할당하지 않아도 됨

### 단점

- 노드끼리의 연결을 위해 _포인터_ 라는 별도의 저장 공간이 필요함
- 처음부터 각 노드에 차례대로 접근해야 하므로 검색 속도가 느림

## 간단한 링크드 리스트 구현

```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
```

## 더블 링크드 리스트 (Double Linked List) 특징

- 이중 연결 리스트라고도 함
- 양방향으로 연결돼 있어서 양쪽으로 노드 검색이 가능하다는 장점이 있음

## 간단한 더블 링크드 리스트 구현

```python
class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        new_node = Node(data, cur_node)
        cur_node.next = new_node
        self.tail = new_node

    # tail부터 시작해서 before_data를 가진 노드 앞에 data를 가진 새로운 노드를 추가
    def insert_before(self, data, before_data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
            return

        cur_node = self.tail
        while cur_node.data != before_data:
            cur_node = cur_node.prev

        if cur_node:
            new_node = Node(data, cur_node.prev, cur_node)
            cur_node.prev.next = new_node
            cur_node.prev = new_node

    def search_from_head(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next

    def search_from_tail(self, data):
        node = self.tail
        while node:
            if node.data == data:
                return node
            node = node.prev

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
```

# 시간 복잡도 (Time Complexity)

## 알고리즘 복잡도 계산이 필요한 이유

- 어떤 문제를 해결하기 위한 알고리즘은 다양할 수 있기 때문에 그 중에서 어느 알고리즘이 더 좋은지 분석할 필요가 있음

## 알고리즘 복잡도 특징

- 시간 복잡도: 알고리즘 실행 속도
- 공간 복잡도: 알고리즘이 사용하는 메모리 크기
- **요즘에는 시간 복잡도가 더 중요!**
- 시간 복잡도를 구할 때는 **반복문** 이 가장 중요함

## 알고리즘 성능 표기법

- Big O (빅-오) 표기법: O(N)
  - *가장 많이 사용하는 표기법*으로 **최악의 실행 시간** 을 표기
- Ω (오메가) 표기법: Ω(N)
  - 최상의 실행 시간을 표기
- Θ (세타) 표기법: Θ(N)
  - 평균 실행 시간을 표기

## Big-O 표기법 (Big-O Notation)

- O(입력)
- 입력 n에 따라 결정되는 시간 복잡도 함수
- O(1) < O( 𝑙𝑜𝑔𝑛 ) < O(n) < O(n 𝑙𝑜𝑔𝑛 ) < O( 𝑛2 ) < O( 2𝑛 ) < O(n!)
- 입력 n에 따라 시간 복잡도가 기하급수적으로 늘어날 수 있음

![Big O Notation](images/algorithm-technical-interview-all-in-one/big-o-notation.jpg)

## 예시 - 1부터 n까지의 합을 구하는 두 알고리즘 비교

```python
# 1부터 1씩 증가하면서 n까지 더하는 함수
def sum_all_1(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    return total

# 1부터 n까지의 합은 n(n + 1) / 2라는 공식을 이용한 함수
def sum_all_2(n):
    return int(n * (n + 1) / 2)
```

- `sum_all_1(n)`는 n의 값에 따라 for문의 반복 횟수가 달라지기 때문에 **O(n)**
- `sum_all_2(n)`는 n의 값과 무관하게 특정한 연산만 수행하기 때문에 **O(1)**
- **O(1)** 복잡도를 가진 `sum_all_2(n)`이 **O(n)** 복잡도를 가진 `sum_all_1(n)`보다 더 좋은 알고리즘이라 할 수 있다.
