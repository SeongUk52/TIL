import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]

default_len, r = divmod(m - sum(map(len, data)), n - 1)
result = data[0]

for idx in range(1, n):
    gap = default_len + 1 if (data[idx][0].islower() or idx + r == n) and r > 0 else default_len
    result += '_' * gap + data[idx]
    r -= gap > default_len

print(result)