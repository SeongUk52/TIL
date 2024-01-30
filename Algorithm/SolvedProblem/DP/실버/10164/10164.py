import math

n, m, k = map(int, input().split())
dotN1 = (k - 1) // m + 1
dotM1 = k - (dotN1 - 1) * m
dotN2 = n - (dotN1 - 1)
dotM2 = m - (dotM1 - 1)

if k == 0:
    print((math.factorial(n + m - 2) // (math.factorial(n - 1) * math.factorial(m - 1))))
else:
    first = (math.factorial(dotN1 + dotM1 - 2) // (math.factorial(dotN1 - 1) * math.factorial(dotM1 - 1)))
    second = (math.factorial(dotN2 + dotM2 - 2) // (math.factorial(dotN2 - 1) * math.factorial(dotM2 - 1)))
    print(first * second)
