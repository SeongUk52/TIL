import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}
answer = 0

for _ in range(n):
    memo[input().rstrip()] = 1
    answer += 1
for _ in range(m):
    inputs = list(input().rstrip().split(sep=","))
    for i in inputs:
        if i in memo.keys():
            if memo[i] == 1:
                memo[i] = 0
                answer -= 1
    print(answer)
