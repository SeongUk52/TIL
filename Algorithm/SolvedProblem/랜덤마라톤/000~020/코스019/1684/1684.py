import math

n = int(input())
v = list(map(int, input().split()))
m = min(v)
t = [v[k] - m for k in range(n) if v[k] != m]
g = t[0]
for k in range(1, len(t)): g = math.gcd(g, t[k])
print(g)
