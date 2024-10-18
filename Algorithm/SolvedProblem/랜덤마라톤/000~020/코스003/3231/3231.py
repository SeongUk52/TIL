result = 0
n = int(input())
ll = [0] * (n + 1)
for i in range(n):
    ll[int(input())] = i
for i in range(1, n):
    if ll[i] > ll[i + 1]:
        result += 1
print(result)
