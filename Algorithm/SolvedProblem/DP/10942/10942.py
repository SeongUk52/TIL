import sys
input = sys.stdin.readline

n = int(input())
ll = list(map(int, input().split()))
m = int(input())
dp = [[False] * (n+1) for i in range(n+1)]

# 팰린드롬 여부 초기화
for i in range(1, n+1):
    dp[i][i] = True

# 길이가 2인 팰린드롬 초기화
for i in range(1, n):
    if ll[i - 1] == ll[i]:
        dp[i][i + 1] = True

# 팰린드롬 여부 갱신
for k in range(3, n+1):
    for i in range(1, n-k+2):
        j = i + k - 1
        dp[i][j] = ll[i - 1] == ll[j - 1] and dp[i + 1][j - 1]

for i in range(m):
    s, e = map(int, input().split())
    if dp[s][e]:
        print('1')
    else:
        print('0')
