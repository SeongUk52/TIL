def dfs(depth, now, debt):
    global cash
    cash = max(cash, now)
    now -= debt
    if depth == n - 1:
        return
    dfs(depth + 1, now, 0)
    able = now * k
    if now + able < p[depth]:
        return
    now += able
    for i in range(depth + 1, n):
        dfs(i, (p[i] - p[depth]) * (now // p[depth]) + now, able)


n, m, k = map(int, input().split())
p = list(map(int, input().split()))
loan = 0
cash = m
stock = 0

dfs(0, cash, 0)

print(cash)
