import sys
import heapq

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    x = int(sys.stdin.readline())

    heapq.heappush(heap, x)

result = 0

if len(heap) == 1:
    result = heapq.heappop(heap)

while heap:
    if result == 0:
        result = heapq.heappop(heap) + heapq.heappop(heap)
        continue

    result = result * 2 + heapq.heappop(heap)

print(result)
