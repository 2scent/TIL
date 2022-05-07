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

- 점근 표기법의 하나
- 알고리즘의 복잡도를 표현할 때 흔히 쓰임
- 입력의 크기가 n일 때 비례, 계수는 별로 중요하지 않음

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
