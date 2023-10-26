n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + arr[i][0], n + 1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])