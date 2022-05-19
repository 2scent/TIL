# 보통의 취준생을 위한 코딩 테스트 with 파이썬

> 본 문서는 [보통의 취준생을 위한 코딩 테스트 with 파이썬](https://roadbook.co.kr/267)을 읽고 제 주관대로 정리한 글입니다.

---

# 제1장 - 코딩 테스트 준비, 6개월이면 충분하다

- <백준> 플래티넘 5 or <코드포스> 파란색 랭크를 달성하면 대부분 기업의 코딩 테스트를 통과할 수 있다.

## <백준> 난이도 등급

![백준 난이도](images/algorithm-code-for-coding-test/difficulty-curve.svg)

## <코드포스> 계정 랭크

![코드포스 랭크](images/algorithm-code-for-coding-test/codeforces-rating-system.jpg)

## 저자의 실수

1. 자신의 실력보다 어려운 문제에 대한 도전을 두려워했다.
2. 문제를 보고 정답을 모를 때 해답을 보며 자신의 것으로 만들지 않았다.
3. 풀어본 문제에 대하여 사색의 시간을 갖지 않았다.

- 핵심 알고리즘 10개를 기반으로 <백준>, solved.ac, <코드포스> 등을 통해 문제 해결 능력을 기르자
- 복기를 통해 제대로 풀지 못한 문제는 해답을 보며 정확하게 내 것으로 만들도록 노력하자
- 아는 문제라도 왜 그 답이 맞는지 증명할 수 있어야 하며, 더 나은 방법은 없는지 한 번 더 생각해보자

# 제2장 - 코딩 테스트의 주적, 시간 복잡도

- 코딩 테스트에서는 보통 컴퓨터가 1초당 1억 번 연산할 수 있다고 가정한다.

## 시간 복잡도의 빅오 표현법

- 입력값 n에 따른 컴퓨터 연산횟수를 대문자 O를 이용한 함수로 나타내는 표현법
- 최악 시간 복잡도

|   빅오 표현법    | 입력값 |  총 연산횟수  |                      비고                      |
| :--------------: | :----: | :-----------: | :--------------------------------------------: |
|      O(n!)       |   n    |      n!       |                                                |
| O(2<sup>n</sup>) |   n    | 2<sup>n</sup> |                                                |
| O(n<sup>2</sup>) |   n    | n<sup>2</sup> |                                                |
|       O(n)       |   n    |       n       |                                                |
|     O(logn)      |   n    |     logn      | 밑은 2 또는 10이 될 수 있으나 크게 중요치 않음 |
|       O(1)       |  무관  |     상수      |                                                |

<img src="images/algorithm-code-for-coding-test/big-o-notation.png" alt="빅오표기법" width="400">

# 제5장 - 구현의 기초적인 문제

## 입출력에 관한 기본

### 출력

> <백준> [Hello World](https://www.acmicpc.net/problem/2557)

- `print()`를 이용해 'Hello World!'만 출력하면 되는 매우 간단한 문제다.

```python
print('Hello World!')
```

### 입력

#### 숫자 하나 입력받기

```python
"""
입력
3

결과
num = 3
"""
num = int(input())
```

#### 한 줄 입력받기

```python
"""
입력
3 5

결과
a = 3, b = 5
"""
a, b = map(int, input().split())
```

#### 리스트를 통해 한 줄 입력받기

```python
"""
입력
1 2 3 4 5 6 7 8 9

결과
num[0] = 1, num[1] = 2, ..., num[7] = 8, num[8] = 9
"""
num = list(map(int, input().split()))
```

#### 한 줄로 여러 문자열 입력받기

```python
"""
입력
abc def

결과
a = 'abc', b = 'def'
"""
a, b = input().split()
```

#### 문자열 여러 줄 입력받기 - 1

```python
"""
입력
ABCDEF
BCDEFA
CDEFAB

결과
str[0] = 'ABCDEF', str[1] = 'BCDEFA', str[2] = 'CDEFAB'
"""
str = [input() for _ in range(3)]
```

#### 문자열 여러 줄 입력받기 - 2

```python
"""
입력
0101
1010
0101
1010

결과
arr[0][0] = 0, arr[0][1] = 1, arr[0][2] = 0, arr[0][3] = 1
arr[1][0] = 1, arr[1][1] = 0, arr[1][2] = 1, arr[1][3] = 0
arr[2][0] = 0, arr[2][1] = 1, arr[2][2] = 0, arr[2][3] = 1
arr[3][0] = 1, arr[3][1] = 0, arr[3][2] = 1, arr[3][3] = 0
"""
arr = [list(map(int, input())) for _ in range(4)]
```

#### 2차원 배열 입력받기

```python
"""
입력
1 2 3 4 5
6 7 8 9 10
5 4 3 2 1

결과
arr[0][0] = 1, arr[0][1] = 2, arr[0][2] = 3, arr[0][3] = 4, arr[0][4] = 5
arr[1][0] = 6, arr[1][1] = 7, arr[1][2] = 8, arr[1][3] = 9, arr[1][4] = 10
arr[2][0] = 5, arr[2][1] = 4, arr[2][2] = 3, arr[2][3] = 2, arr[2][4] = 1
"""
arr = [list(map(int, input().split())) for _ in range(3)]
```

### 사칙연산

> <백준> [사칙연산](https://www.acmicpc.net/problem/10869)

- 두 개의 자연수를 입력받고, 각 사칙연산의 결과를 출력하는 문제다.
- 파이썬의 나눗셈 연산(/)은 기본적으로 소수점 이하를 포함하는 결과가 나오기 때문에 `int()`를 이용해 정수형으로 변환해준다.

```python
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)
```

## if문

> <백준> [두 수 비교하기](https://www.acmicpc.net/problem/1330)

- if, elif, else를 이용해 적절하게 분기해서 출력하면 된다.

```python
a, b = map(int, input().split())

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('==')
```

## for문(컴퓨팅 사고력 향상)

### for문 예제 1

> <백준> [별 찍기 - 1](https://www.acmicpc.net/problem/2438)

```python
# 파이써닉한 방법
n = int(input())

for i in range(1, n + 1):
    print('*' * i)
```

```python
# C언어 계열 방법
n = int(input())

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    print()
```

### for문 예제 2

> <백준> [별 찍기 - 2](https://www.acmicpc.net/problem/2439)

```python
# 파이써닉한 방법
n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * i)
```

```python
# C언어 계열 방법
n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end='')
    print()
```

### for문 예제 3

> <백준> [별 찍기 - 5](https://www.acmicpc.net/problem/2442)

```python
# 파이써닉한 방법
n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))
```

```python
# C언어 계열 방법
n = int(input())

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
```

## 함수

> <백준> [사칙연산](https://www.acmicpc.net/problem/10869)

```python
def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a / b)

def mod(a, b):
    return a % b

a, b = map(int, input().split())

print(sum(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))
print(mod(a, b))
```
