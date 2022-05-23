import sys
from collections import deque


def turn(d, c):
    if c == 'L':
        return (d - 1) % 4
    return (d + 1) % 4


N = int(sys.stdin.readline())
# N * N의 2차원 배열을 0(빈 칸)으로 초기화
board = [[0] * N for _ in range(N)]

K = int(sys.stdin.readline())
# 사과의 위치를 1로 저장
for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = 1

L = int(sys.stdin.readline())
times = {}
for _ in range(L):
    X, C = sys.stdin.readline().split()
    times[int(X)] = C

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 0: 위쪽, 1: 오른쪽, 2: 아래쪽, 3: 왼쪽
direction = 1
time = 0
# 뱀 머리의 현재 위치
y, x = 0, 0
# 뱀 몸통
snake = deque([(y, x)])
# 뱀 몸통의 위치를 2로 저장
board[y][x] = 2

while True:
    time += 1
    y, x = y + dy[direction], x + dx[direction]

    if y < 0 or y >= N or x < 0 or x >= N or board[y][x] == 2:
        break

    if board[y][x] != 1:
        del_y, del_x = snake.popleft()
        board[del_y][del_x] = 0
    board[y][x] = 2
    snake.append((y, x))
    if time in times.keys():
        direction = turn(direction, times[time])

print(time)
