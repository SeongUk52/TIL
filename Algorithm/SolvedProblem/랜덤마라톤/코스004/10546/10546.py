import sys
input = sys.stdin.readline

n = int(input())
ll = dict()
for i in range(n):
    a = input().rstrip()
    if a not in ll:
        ll[a] = 1
    else:
        ll[a] += 1
for i in range(n - 1):
    b = input().rstrip()
    ll[b] -= 1
for i, j in ll.items():
    if j == 1:
        print(i)
        break
