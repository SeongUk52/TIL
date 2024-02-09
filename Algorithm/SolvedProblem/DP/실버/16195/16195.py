from sys import stdin


if __name__ == '__main__':
    MAX = 1001
    divisor = 1000000009
    dp = [[0] * MAX for _ in range(MAX)]

    dp[1][1] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 2
    dp[3][3] = 1

    for i in range(4, MAX):
        for j in range(1, i + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % divisor

    t = int(stdin.readline())

    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        print(sum(dp[n][1:m + 1]) % divisor)
