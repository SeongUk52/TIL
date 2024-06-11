from math import ceil

n = int(input())
tl = list(map(int, input().split()))
t, p = map(int, input().split())
cnt = 0
for i in tl:
    cnt += ceil(i / t)
print(cnt)
print(n // p, n % p)
