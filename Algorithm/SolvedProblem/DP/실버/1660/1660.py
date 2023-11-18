n = int(input())

dpt = [0] * 130
dp = [0] * 130
dpr = [0] * (n + 1)

for i in range(n + 1):
    dpr[i] = i

for i in range(1, 130):
    dpt[i] = dpt[i - 1] + i
    dp[i] = dp[i - 1] + dpt[i]

for i in range(n + 1):
    for j in range(130):
        if i < dp[j]:
            break
        dpr[i] = min(dpr[i], dpr[i - dp[j]] + 1)

print(dpr[-1])