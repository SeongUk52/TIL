n = int(input())
maze = []
dp = [[0] * 4 for _ in range(n)]
dp[0] = [0, 1, 2, 3]
for _ in range(n - 2):
    inputs = input()
    maze.append(inputs.index("0"))

for i in range(1, n - 1):
    for j in range(4):
        differ = abs(j - maze[i - 1])
        if differ == 3:
            differ = 1
        dp[i][j] = dp[i - 1][j] + differ + 1

for i in range(4):
    dp[n - 1][i] = dp[n - 2][i] + 4 - i

print(min(dp[-1]))
