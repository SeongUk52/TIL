dp = dict()
DIV = 1_000_000_007


def fibo(n):
    if dp.get(n) is not None:
        return dp[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % DIV
        dp[n // 2 - 1] = fibo(n // 2 - 1) % DIV
        return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
    else:
        dp[n // 2 + 1] = fibo(n // 2 + 1) % DIV
        dp[n // 2] = fibo(n // 2) % DIV
        return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2


print(fibo(int(input())) % DIV)
