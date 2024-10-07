import math

m, n = map(int, input().split())
m = abs(m)
n = abs(n)
if m == n == 0:
    print(0)
elif math.gcd(n, m) == 1:
    print(1)
else:
    print(2)
