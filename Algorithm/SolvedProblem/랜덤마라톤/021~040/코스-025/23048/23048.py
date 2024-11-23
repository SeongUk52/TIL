import math

MAX = 500001
N = int(input())
DP = list(range(MAX))
Color = [0] * MAX
Color[1] = 1
K = 2

for i in range(2, int(math.sqrt(MAX)) + 1):
    if DP[i]:
        for j in range(i * i, MAX, i):
            DP[j] = 0

for i in range(2, N + 1):
    if DP[i]:
        Color[i] = K
        for j in range(i * i, N + 1, i):
            Color[j] = K
        K += 1

print(K - 1)
print(" ".join(map(str, Color[1:N + 1])))