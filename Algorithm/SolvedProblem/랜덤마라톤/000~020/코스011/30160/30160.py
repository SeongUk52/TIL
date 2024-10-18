n = int(input())
a = list(map(int, input().split()))
oddimos = [0] * n
imos = [0] * n
oddimos[0], imos[0] = a[0], a[0]
for i, v in enumerate(a):
    if i == 0:
        continue
    imos[i] = imos[i - 1] + v
    oddimos[i] = oddimos[i - 1] + (2 * i + 1) * v

ans = [a[0]]
for i in range(1, n):
    k = i + 1
    p = ans[-1]
    xk = 2 * k * imos[i] - oddimos[i]
    ans.append(p + xk)

print(*ans)
