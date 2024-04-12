import sys
from collections import deque
input = sys.stdin.readline

p = [1, 2]
for i in range(2, 46):
    p.append(p[i-2]+p[i-1])
T = int(input())

for j in range(T):
    n = int(input())
    result = deque()
    flag = 46
    while n:
        for k in range(flag):
            if p[k] <= n:
                t = p[k]
                flag = k
        n -= t
        result.appendleft(t)
    print(*result)
