import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = []
for _ in range(N):
    ground.extend(map(int, sys.stdin.readline().split()))
time = [0 for i in range(257)]
height = 0
for g in range(257):
    block = B
    for i in ground:
        if i <= g:
            time[g] += g - i
            block -= g - i
        else:
            time[g] += 2 * (i - g)
            block += i - g
    if block >= 0 and time[g] <= time[height]:
        height = g

print(time[height], height)
