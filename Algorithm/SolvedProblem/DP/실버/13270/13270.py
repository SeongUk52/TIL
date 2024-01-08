MAX = 1e9

n = int(input())
a = 1
b = 2

dpMin = [0] + [MAX] * 10000
dpMax = [0] * 10001

while b <= n:
    for i in range(b, n + 1):
        dpMin[i] = min(dpMin[i], dpMin[i - b] + a)
        dpMax[i] = max(dpMax[i], dpMax[i - b] + a)
    b += a
    a = b - a


print(dpMin[n], dpMax[n])