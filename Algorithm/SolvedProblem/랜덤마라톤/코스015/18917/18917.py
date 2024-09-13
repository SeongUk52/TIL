import sys

input = sys.stdin.readline
M = int(input())
sum = 0
xor = 0

for i in range(M):
  q = list(map(int, input().split()))
  if q[0] == 1:
    sum += q[1]
    xor ^= q[1]
  elif q[0] == 2:
    sum -= q[1]
    xor ^= q[1]
  elif q[0] == 3:
    print(sum)
  else:
    print(xor)
