import sys; input = sys.stdin.readline
from math import inf

def solve():
    N, K = map(int, input().split())
    dolls = list(map(int, input().split()))

    ryan = []
    for i in range(N):
        if dolls[i] == 1:
            ryan.append(i)

    if len(ryan) < K:
        print(-1)
        return

    answer = inf
    for i in range(len(ryan) - K + 1):
        answer = min(answer, ryan[i + K - 1] - ryan[i] + 1)
    print(answer)

solve()
