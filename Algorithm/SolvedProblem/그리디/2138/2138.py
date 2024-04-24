import sys
input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))


def change(A, B):
    A_copy = A[:]
    cnt = 0
    for i in range(1, n):
        if A_copy[i - 1] == B[i - 1]:
            continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return cnt
    else:
        return float('infinity')


res = change(bulb, target)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
if res != float('infinity'):
    print(res)
else:
    print(-1)
