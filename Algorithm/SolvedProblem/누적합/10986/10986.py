n, m = map(int, input().split())

arr = list(map(int, input().split()))

r = [0] * m

ps = 0

for i in range(n):
    ps += arr[i]
    r[ps % m] += 1

ans = r[0]

for i in range(m):
    ans += r[i] * (r[i] - 1) // 2

print(ans)