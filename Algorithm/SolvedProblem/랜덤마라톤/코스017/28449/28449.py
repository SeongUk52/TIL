import sys
input = sys.stdin.readline
from bisect import bisect_left

N, M = map(int, input().split())
hi = [*map(int, input().split())]
hi.sort()
arc = [*map(int, input().split())]
arc.sort()
result = [0, 0, 0]
for i in range(N):
    val = hi[i]
    idx = bisect_left(arc, val)
    idx2 = bisect_left(arc, val+1)
    result[2] += idx2 - idx
    result[1] += M - idx2
    result[0] += idx


print(*result)
