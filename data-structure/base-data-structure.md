# 기본 자료구조

> 파이썬(Python)을 기준으로 기본적인 자료구조에 대해서 간단하게 정리한 문서입니다.

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
