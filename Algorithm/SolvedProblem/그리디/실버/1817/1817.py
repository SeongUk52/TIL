n, m = map(int, input().split())
result = 0
temp = m
if n > 0:
    arr = list(map(int, input().split()))
    result += 1
for i in range(n):
    temp -= arr[i]
    if temp < 0:
        temp = m - arr[i]
        result += 1
print(result)
