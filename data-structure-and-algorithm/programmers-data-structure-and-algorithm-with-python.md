# 어서와! 자료구조와 알고리즘은 처음이지?

> 본 문서는 [어서와! 자료구조와 알고리즘은 처음이지?](https://programmers.co.kr/learn/courses/57) 강의를 보고 제 주관대로 정리한 글입니다.

---

# 선형 배열 (Linear Array)

- 같은 종류의 데이터 줄지어 늘어놓은 것
- 각각의 원소는 **인덱스**라는 번호가 있는데, 일반적으로 **0부터 시작함**
- **_파이썬에서는 리스트(list)라는 데이터 타입으로 배열 사용_**
  - 일반적인 배열보다 여러 추가 기능이 있음
  - 일반적인 배열과 달리 여러 데이터 타입 사용 가능

## 파이썬 리스트의 연산들

### 리스트의 길이와 무관하게 상수 시간 O(1)에 실행할 수 있는 연산

- 원소 덧붙이기 `.append()`
- 끝에서 꺼내기 `.pop()`

### 리스트 길이에 비례하는 선형 시간 O(n)이 걸리는 연산

- 원소 삽입하기 `.insert()`
- 원소 삭제하기 `.del()`
- 원소 탐색하기 `.index()`

### 정렬

- `sorted()`
  - 파이썬 내장 함수
  - 정렬된 새로운 리스트를 반환
- `.sort()`
  - 리스트의 메서드
  - 해당 리스트를 정렬함
- 역순으로 정렬하고 싶으면 `reverse=True`
- 문자열의 경우 사전 순서(알파벳 순서)를 따름
  - 문자열 길이로 하고 싶다면 key를 이용
  - e.g., key = lambda x: len(x)

```python
L = [{'name': 'John', 'score': 83},
     {'name': 'Paul', 'score': 92}]

# 이름 순서대로 정렬
L.sort(key=lambda x: x['name'])

# 점수 높은 순으로 정렬
L.sort(key=lambda x: x['score'], reverse=True)
```

## 탐색

### 선형 탐색(Linear Search)

- 앞에서 부터 순서대로 하나씩 비교
- 최악의 경우 모든 원소를 다 비교: O(n)

```python
# 찾고자 하는 값이 있으면 해당 인덱스를, 없으면 -1을 반환
def linear_search(L, x):
    for i, value in enumerate(L):
        if value == x:
            return i
    return -1
```

### 이진 탐색 (Binary Search)

- 탐색하고자 하는 배열이 정렬돼 있는 경우에만 가능
  - **선형 탐색에 비해 항상 좋다고 할 수 없음**
- 한 번 비교가 일어날 때마다 리스트 반씩 줄임 (divide & conquer): O(log n)

```python
'''
1. 첫 인덱스를 lower, 마지막 인덱스를 upper, lower와 upper의 중간값을 middle에 할당
2. middle에 있는 값과 탐색하고자 하는 값 x를 비교
    - 두 값이 같으면 middle을 반환
    - x가 더 크면, lower에 middle + 1을 할당
    - x가 더 작으면, upper에 middle - 1을 할당
3. x가 있는 인덱스를 찾거나, lower > upper가 될 때까지 2번 반복
    - x를 못 찾으면, -1을 반환
'''
def binary_search(L, x):
    result = -1

    lower = 0
    upper = len(L) - 1

    while upper >= lower:
        middle = (upper + lower) // 2

        if L[middle] == x:
            result = middle
            break
        elif L[middle] > x:
            upper = middle - 1
        else:
            lower = middle + 1

    return result
```

# 재귀 알고리즘 (Recursive Algorithm)

## 재귀 함수 (Recursive Function)

- 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
- **종결 조건이 매우 중요**

### 1부터 n까지 모든 자연수의 합 구하기 예제

```python
def recursive_sum(n):
    if n <= 1:  # 종결 조건
        return n
    return n + recursive_sum(n - 1)

def iterative_sum(n):
    result = 0
    while n >= 0:
        result += n
        n -= 1
    return result
```

|                               Recursive                               |        Iterative         |
| :-------------------------------------------------------------------: | :----------------------: |
|                                 O(n)                                  |           O(n)           |
| 직관적이지만 함수 호출과 같은 <br> 추가 비용이 들기 때문에 비효율적임 | 재귀함수에 비해 효율적임 |

### 팩토리얼 예시

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n)
```

### 피보나치 예시

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### 재귀적 이진 탐색 예시

```python
def recursive_binary_search(L, x, lower, upper):
    if lower > upper:
        return -1
    middle = (lower + upper) // 2
    if x == L[middle]:
        return middle
    elif x < L[middle]:
        return recursive_binary_search(L, x, lower, middle - 1)
    else:
        return recursive_binary_search(L, x, middle + 1, upper)
```

# 알고리즘 복잡도 (Complexity of Algorithm)

- 시간 복잡도 (Time Complexity)
  - 문제의 크기와 이를 해결하는 데 걸리는 시간 사이의 관계
  - 평균 시간 복잡도 (Average Time Complexity)
    - 임의의 입력 패턴을 가정했을 때 소요되는 시간의 평균
  - 최악 시간 복잡도 (Worst-case Time Complexity)
    - 가장 긴 시간을 소요하게 만드는 입력에 따라 소요되는 시간
- 공간 복잡도 (Space Complexty)
  - 문제의 크기와 이를 해결하는 데 필요한 메모리 공간 사이의 관계

## Big-O Notation

- 점근 표기법 중의 하나
- 알고리즘의 복잡도를 표현할 때 흔히 쓰임
- 입력의 크기가 n일 때, 얼마나 비례하는지 나타냄
- 계수는 별로 중요하지 않음

### 선형 시간 알고리즘 - O(n)

- e.g., n개의 무작위로 나열된 수에서 최댓값을 찾기 위해 선형 탐색 알고리즘을 적용
  - 최댓값 - 끝까지 다 살펴보기 전까지는 알 수 없음
  - Average case: O(n)
  - Worst case: O(n)

### 로그 시간 알고리즘 - O(logn)

- e.g., n개의 크기 순으로 정렬된 수에서 특정 값을 찾기 위해 이진 탐색 알고리즘을 적용

### 이차 시간 알고리즘 - O(n<sup>2</sup>)

- e.g., 삽입 정렬 (Insertion Sort)
  - Best case: O(n)
  - Worst case: O(n<sup>2</sup>)

### 보다 낮은 복잡도를 가지는 정렬 알고리즘

- e.g., 병합 정렬 (Merge Sort) - O(nlogn)
  - 정렬 문제에 대해 O(nlogn)보다 낮은 복잡도를 갖는 알고리즘은 없다는 게 수학적으로 증명됨

# 연결 리스트 (Linked List)

## 추상 자료형 (Abstract Data Type)

- Data
  - e.g., 정수, 문자열, 레코드 등
- Operations
  - 삽입, 삭제, 순회 등
  - 정렬, 탐색 등

## 단일 연결 리스트 (Singly Linked List)

![단일 연결 리스트](images/singly-linked-list.png)

### Node

- Data
  - e.g., 문자열, 레코드, 또 다른 연결 리스트 등
- Link (next)

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
```

### SinglyLinkedList

- Properties
  - 첫 노드를 가리키는 `head`
  - 마지막 노드를 가리키는 `tail`
  - 총 노드의 수
- 예시에서 첫 인덱스는 0이 아닌 1

```python
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
```

### 배열과 비교

|                |       배열       |      연결 리스트       |
| :------------: | :--------------: | :--------------------: |
|   저장 공간    |   연속한 위치    |      임의의 위치       |
| 특정 원소 참조 | 매우 간편 - O(1) | 선형탐색과 유사 - O(n) |

### 삽입의 시간 복잡도

- 맨 앞에 삽입하는 경우: O(1)
- 중간에 삽입하는 경우: O(n)
- 맨 끝에 삽입하는 경우: O(1)
  - `tail` 덕분

### 삭제의 시간 복잡도

- 맨 앞에 삭제하는 경우: O(1)
- 중간에 삭제하는 경우: O(n)
- 맨 끝에 삭제하는 경우: O(n)

### 연결 리스트의 강점

- 삽입과 삭제가 유연함
- 이를 위해 새로운 메서드들을 추가
  - `insert_after(prev, new_node)`
  - `pop_after(prev)`
- 맨 앞의 노드를 해결하기 위해 더미 노드를 추가

```python
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
```

## 양방향 연결 리스트 (Doubly Linked List)

- 한쪽이 아닌 양쪽으로 링크 연결
- **정방향, 역방향 둘다 진행 가능**

![양방향 연결 리스트](images/doubly-linked-list.png)

### Node

- 이전 노드를 가리키는 `prev` 추가

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None
```

### DoublyLinkedList

- 처음와 끝에 더미 노드
- 데이터를 담고 있는 노드들은 모두 같은 모양

```python
class DoublyLinkedList:
    def __init__(self):
        self.node_count = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    # 리스트 정방향 순회
    def traverse(self):
        result = []
        cur = self.head
        while cur.next.next:
            cur = cur.next
            result.append(cur.data)
        return result

    # 리스트 역방향 순회
    def reverse(self):
        result = []
        cur = self.tail
        while cur.prev.prev:
            cur = cur.prev
            result.append(cur.data)
        return result

    # 특정 원소 참조
    def get_at(self, pos):
        if pos <= 0 or pos > self.node_count:
            return None

        if pos > self.node_count // 2:  # 찾고자 하는 원소가 뒤쪽에 있으면 tail부터 찾음
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

    # 특정 원소 다음에 원소 삽입
    def insert_after(self, prev, new_node):
        next = prev.next
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.node_count += 1
        return True

    # 특정 원소 이전에 원소 삽입
    def insert_before(self, next, new_node):
        prev = next.prev
        new_node.prev = prev
        new_node.next = next
        prev.next = new_node
        next.prev = new_node
        self.node_count += 1
        return True

    # 특정 원소 삽입
    def insert_at(self, pos, new_node):
        if pos < 1 or pos > self.node_count + 1:
            return False

        return self.insert_after(self.get_at(pos - 1), new_node)

    # 특정 원소 다음 원소 삭제
    def pop_after(self, prev):
        cur = prev.next
        next = cur.next
        prev.next = next
        next.prev = prev

        self.node_count -= 1

        return cur.data

    # 특정 원소 이전 원소 삭제
    def pop_before(self, next):
        cur = next.prev
        prev = cur.prev
        prev.next = next
        next.prev = prev

        self.node_count -= 1

        return cur.data

    # 특정 원소 삭제
    def pop_at(self, pos):
        if pos < 1 or pos > self.node_count:
            raise IndexError

        return self.pop_after(self.get_at(pos - 1))

    # 리스트 병합
    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.node_count += L.node_count
```

# 스택 (Stack)

- 자료를 보관할 수 있는 선형 구조
- 넣을 때는 한쪽 끝에서 밀어 넣어야 하고 - Push 연산
- 꺼낼 때는 같은 쪽에서 뽑아 꺼내야 한다 - Pop 연산
- 후입선출 (LIFO - Last In, First Out)

![스택](images/stack.png)

## 스택에서 발생할 수 있는 오류

- 비어있는 스택에서 데이터를 꺼내려고 할 때 - 스택 언더플로우 (Stack Underflow)
- 꽉 찬 스택에 데이터를 넣으려 할 때 - 스택 오버플로우 (Stack Overflow)

## 스택의 구현

### 연산의 정의

- `size()` - 현재 스택에 들어있는 데이터 원소의 수를 구함
- `isEmpty()` - 현재 스택이 비어 있는지 판단
- `push(x)` - 데이터 원소 x를 스택에 추가
- `pop()` - 스택의 맨 위에 저장된 데이터 원소를 제거 및 반환
- `peek()` - 스택의 맨 위에 저장된 데이터 원소를 반환 (제거하지 않음)

### 배열(파이썬의 리스트)을 이용한 구현

```python
class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
```

### 연결 리스트를 이용한 구현

> 연결 리스트 관련 코드는 [doubly_linked_list.py](src/doubly_linked_list.py) 참고

```python
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
```

## 수식의 후위 표기법

### 중위 표기법 (Infix Notation)

- 연산자가 피연사자들의 **사이**에 위치
- e.g., (A + B) \* (C + D)

### 후위 표기법 (Postfix Notation)

- 연산자가 피연산자들의 **뒤**에 위치
- e.g., A B + C D + \*

### 중위 표기법 -> 후위 표기법 예시

- **_A \* B + C_** -> **_A B \* C +_**
- **_A + B \* C_** -> **_A B C \* +_**
- **_A + B + C_** -> **_A B + C +_**
- **_(A + B) \* C_** -> **_A B + C \*_**
- **_A \* (B + C)_** -> **_A B C + \*_**
- **_(A + B) \* (C + D)_** -> **_A B + C D + \*_**
- **_(A + (B - C)) \* D_** -> **_A B C - + D \*_**
- **_A \* (B - (C + D))_** -> **_A B C D + - \*_**

### 중위 표기법 -> 후위 표기법 알고리즘 설계 및 구현

1. 연산자의 우선 순위 설정
2. 중위 표현식을 왼쪽부터 한 글자씩 읽어서
   1. 피연산자면 그냥 출력
   2. '('일 경우, 스택에 Push
   3. ')'일 경우, '('가 나올 때까지 스택에서 Pop
   4. 연산자면 스택에서 이보다 높거나 같은 우선순위 것들을 Pop
   5. 현재 연산자는 스택에 Push
3. 스택에 남아 있는 연산자는 모두 Pop

> 스택 관련 코드는 [array_stack.py](src/array_stack.py) 참고

```python
# 1
precedences = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def infix_to_postfix(expr):
    op_stack = ArrayStack()

    result = ''

    # 2
    for c in expr:
        # 2-1
        if c not in '*/+-()':
            result += c
            continue

        # 2-2
        if c == '(':
            op_stack.push(c)
            continue

        # 2-3
        if c == ')':
            t = op_stack.pop()
            while t != '(':
                result += t
                t = op_stack.pop()
            continue

        # 2-4
        while not op_stack.is_empty() and precedences[op_stack.peek()] >= precedences[c]:
            result += op_stack.pop()

        # 2-5
        op_stack.push(c)

    # 3
    while not op_stack.is_empty():
        result += op_stack.pop()

    return result
```

### 후위 표기법 수식 계산 알고리즘 설계 및 구현

1. 후위 표현식을 왼쪽부터 한 글자씩 읽어서
   1. 피연산자면 스택에 Push
   2. 연산자를 만나면 스택에서 Pop -> (1), 또 Pop -> (2)
      - (2) 연산 (1)을 계산하고, 이 결과를 스택에 Push
2. 수식의 끝에 도달하면 스택에서 Pop -> 이것이 계산 결과

> 스택 관련 코드는 [array_stack.py](src/array_stack.py) 참고

```python
def split_tokens(expr):
    tokens = []
    val = 0
    val_processing = False
    for c in expr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            val_processing = True
        else:
            if val_processing:
                tokens.append(val)
                val = 0
            val_processing = False
            tokens.append(c)
    if val_processing:
        tokens.append(val)

    return tokens


def infix_to_postfix(token_list):
    precedences = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    op_stack = ArrayStack()
    postfix_list = []

    for token in token_list:
        if type(token) is int:
            postfix_list.append(token)
            continue

        if token == '(':
            op_stack.push(token)
            continue

        if token == ')':
            t = op_stack.pop()
            while t != '(':
                postfix_list.append(t)
                t = op_stack.pop()
            continue

        while not op_stack.is_empty() and precedences[op_stack.peek()] >= precedences[token]:
            postfix_list.append(op_stack.pop())

        op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return postfix_list


def postfix_eval(token_list):
    val_stack = ArrayStack()

    # 1
    for token in token_list:
        # 1-1
        if type(token) is int:
            val_stack.push(token)
            continue

        # 1-2
        val1 = val_stack.pop()
        val2 = val_stack.pop()

        if token == '*':
            val_stack.push(val2 * val1)
            continue

        if token == '/':
            val_stack.push(val2 / val1)
            continue

        if token == '+':
            val_stack.push(val2 + val1)
            continue

        if token == '-':
            val_stack.push(val2 - val1)
            continue

    # 2
    return val_stack.pop()


def calculate_postfix(expr):
    tokens = split_tokens(expr)
    postfix = infix_to_postfix(tokens)
    val = postfix_eval(postfix)
    return val
```

# 큐 (Queue)

- 자료를 보관할 수 있는 선형 구조
- 넣을 때는 한쪽 끝에서 밀어 넣어야 하고 -> Enqueue 연산
- 꺼낼 때는 반대 쪽에서 뽑아 꺼내야 한다 -> Dequeue 연산
- 선입선출 (FIFO - First In, First Out)
- e.g., 경기장 입장을 기다리는 대기열

![큐](images/queue.png)

## 큐의 구현

### 연산의 정의

- `size()` - 현재 큐에 들어 있는 데이터 원소의 수를 구함
- `isEmpty()` - 현재 큐가 비어 있는지를 판단
- `enqueue(x)` - 데이터 원소 x를 큐에 추가
- `dequeue()` - 큐의 맨 앞에 저장된 데이터 원소를 제거 및 반환
- `peek()` - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)

### 배열(파이썬의 리스트)을 이용한 구현

```python
class ArrayQueue:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]
```

### 배열로 구현한 큐의 시간 복잡도

|     연산     | 시간 복잡도 |
| :----------: | :---------: |
|   `size()`   |    O(1)     |
| `is_empty()` |    O(1)     |
| `enqueue()`  |    O(1)     |
| `dequeue()`  |  **O(n)**   |
|   `peek()`   |    O(1)     |

- 배열의 맨 앞 원소를 꺼내려면 그 뒤의 원소들을 순차적으로 앞으로 이동해야 하기 때문에 Dequeue 연산은 O(n)의 시간이 걸림

### 연결 리스트를 이용한 구현

> 연결 리스트 관련 코드는 [doubly_linked_list.py](src/doubly_linked_list.py) 참고

```python
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
```

### 연결 리스트로 구현한 큐의 시간 복잡도

|     연산     | 시간 복잡도 |
| :----------: | :---------: |
|   `size()`   |    O(1)     |
| `is_empty()` |    O(1)     |
| `enqueue()`  |    O(1)     |
| `dequeue()`  |    O(1)     |
|   `peek()`   |    O(1)     |

- 연결 리스트를 이용한 큐의 시간 복잡도는 연결 리스트를 어떻게 구현했냐에 따라 달라질 수 있다.
- 큐의 `enqueue()`, `dequeue()`, `peek()` 연산들은 연결 리스트의 맨 앞뒤 원소에만 접근하기 때문에 연결 리스트의 `head`와 `tail`를 이용해서 **O(1)** 시간에 처리할 수 있다.

### 큐의 활용

- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우
- 자료를 생성하는 작업이 여러 곳에서 일어나는 경우
- 자료를 이용하는 작업이 여러 곳에서 일어나는 경우
- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우
- 자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우

## 환형 큐 (Circular Queue)

- **정해진 개수**의 저장 공간을 빙 돌려가며 이용

![환형 큐](images/circular-queue.gif)

### 연산의 정의

- `size()` - 현재 큐에 들어 있는 데이터 원소의 수를 구함
- `isEmpty()` - 현재 큐가 비어 있는지를 판단
- **`is_full()` - 큐에 데이터 원소가 꽉 차 있는지를 판단**
- `enqueue(x)` - 데이터 원소 x를 큐에 추가
- `dequeue()` - 큐의 맨 앞에 저장된 데이터 원소를 제거 및 반환
- `peek()` - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)

### 배열(파이썬의 리스트)을 이용한 구현

```python
class CircularQueue:
    def __init__(self, n):
        self.max_count = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.max_count

    def enqueue(self, x):
        if self.is_full():
            raise IndexError('Queue is full!')

        self.rear = (self.rear + 1) % self.max_count
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')

        self.front = (self.front + 1) % self.max_count
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty!')

        return self.data[(self.front + 1) % self.max_count]
```

## 우선순위 큐 (Priority Queue)

- 큐가 선입선출 (FIFO - First In, First-Out) 방식을 따르지 않고, 원소들의 우선순위에 따라 큐에서 빠져나오는 방식
- e.g., 운영체제의 CPU 활용

### 우선순위 큐의 구현

1. Enqueue 할 때 우선순위 순서를 유지하도록
2. Dequeue 할 때 우선순위 높은 것을 선택

- 어느 것이 유리할까? - 둘 다 O(n)의 복잡도를 가지지만 1번이 더 유리함
  - 1번은 이미 우선순위 순으로 정렬돼 있기 때문에 항상 모든 원소를 다 뒤져볼 필요는 없음
  - 2번의 경우 항상 모든 원소를 다 뒤져서 우선순위를 비교해야 함

1. 선형 배열 이용
2. 연결 리스트 이용

- 어느 것이 유리할까?
  - **시간 복잡도 관점 - 리스트의 중간에 원소를 삽입해야 할 경우가 많은 우선순위 큐 특성상 연결 리스트가 유리**
  - 공간 복잡도 관점 - 선형 배열이 유리

```python
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
```
