import sys
N = int(input())

in_time = [0] * 1000001
out_time = [0] * 1000001
D = [0] * 1000001

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    in_time[a] += 1
    out_time[b] += 1

for i in range(1, 1000001):
    D[i] = D[i - 1] + in_time[i] - out_time[i - 1]

Q = int(sys.stdin.readline().rstrip())
Qlist = [int(x) for x in sys.stdin.readline().split()]

for q in Qlist:
    print(D[q])
