import sys

x, b = map(int, sys.stdin.readline().split())
n = 0
result = []

flag = 0
if x < 0 < b:
    x *= -1
    flag = 1

while(x):
    q, r = divmod(x, b)
    if r < 0:
        r -= b
        q += 1
    result.append(r)
    x = q

if not result:
    result.append(0)
result.reverse()

if flag:
    result[0] *= -1
print(''.join(map(str, result)))
