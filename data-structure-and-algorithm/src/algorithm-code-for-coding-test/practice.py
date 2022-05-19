a = int(input())
b = int(input())

c = list(map(int, str(b)))

for n in reversed(c):
    print(a * n)
print(a * b)