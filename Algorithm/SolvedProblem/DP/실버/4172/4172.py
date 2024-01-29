from math import *
seq = [1 for _ in range(1000000+1)]
for i in range(1,1000000+1):
    seq[i] = (seq[floor(i-sqrt(i))] + seq[floor(log(i))] + seq[floor(i*sin(i)*sin(i))]) % 1000000
while True:
    n = int(input())
    if n == -1:
        break
    print(seq[n])