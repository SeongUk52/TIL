import math

a, b = map(int, input().split(":"))
div = math.gcd(a, b)
print(a // div, ":", b // div, sep="")
