import sys
input = sys.stdin.readline

N = int(input())
dot = []
for _ in range(N):
    dot.append([*map(int, input().split())])

dot.append(dot[0])
plus = 0
minus = 0
for i in range(N):
    plus += dot[i][0]*dot[i+1][1]
    minus += dot[i][1]*dot[i+1][0]

S = abs(plus-minus)/2
print(round(S,1))