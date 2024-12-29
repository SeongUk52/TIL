def mypow(x, y, mod):
    res = 1
    while y:
        if y % 2:
            res = res * x % mod
        x = x * x % mod
        y //= 2
    return res


a, b, n = map(int, input().split())
mod = 10 ** 9 + 7
n -= 1
w = mypow(2, 31, mod)
print(mypow(w, n, mod))
