import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
price = [0] + list(map(int, input().split()))
friend = [i for i in range(n + 1)]


def find(n):
    if friend[n] != n:
        friend[n] = find(friend[n])
    return friend[n]


def union(a, b):
    a, b = find(a), find(b)
    if price[a] < price[b]:
        friend[b] = a
    else:
        friend[a] = b


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)


result = 0

for i in range(1, n + 1):
    if friend[i] == i:
        result += price[i]

if result > k:
    print("Oh no")
else:
    print(result)
