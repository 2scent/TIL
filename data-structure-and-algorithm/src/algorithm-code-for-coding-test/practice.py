n, k = map(int, input().split())
number_list = list(input())

stack = []
delete_count = k

for number in number_list:
    while stack and delete_count > 0 and number > stack[-1]:
        stack.pop()
        delete_count -= 1

    stack.append(number)

# 없앨 횟수가 남았으면 제일 뒤부터 제거해야 하기 때문에 n-k번째까지 출력
print(''.join(stack[:n - k]))
