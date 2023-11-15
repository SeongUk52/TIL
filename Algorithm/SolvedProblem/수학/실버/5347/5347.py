import math

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    result = math.lcm(n, m)
    print(result)

