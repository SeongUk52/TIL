import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    cnt = int((n * 3) / 20 + 0.5)
    ll = [int(input()) for _ in range(n)]
    ll.sort()
    if cnt > 0:
        ll = ll[cnt:-cnt]
    avg = int(sum(ll) / (n - cnt * 2) + 0.5)
    print(avg)
