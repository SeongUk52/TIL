import sys

data = sys.stdin.read().split()
t = int(data[0])
idx = 1

for _ in range(t):
    n = int(data[idx])
    arr = map(int, data[idx + 1:idx + 1 + n])
    target = int(data[idx + 1 + n])
    idx += 2 + n

    dp = [1] + [0] * target
    for num in arr:
        for j in range(num, target + 1):
            dp[j] += dp[j - num]

    print(dp[target])