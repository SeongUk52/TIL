import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n):
    dp[i + 1] = dp[i] + arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(dp[b] - dp[a - 1])