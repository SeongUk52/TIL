from math import sqrt, ceil

k = int(input())
j = []
for i in range(2, ceil(sqrt(k)) + 1):
    while k % i == 0:
        j.append(i)
        k //= i
if k > 1: j.append(k)

print(len(j), *j)
