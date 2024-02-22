from itertools import count
import sys
input = sys.stdin.readline

d = {}
count = 0
n, m = map(int, input().split())

for _ in range(n):
    data = input().rstrip()
    d[data] = True

for _ in range(m):
    data = input().rstrip()
    if data in d:
        count += 1

print(count)
