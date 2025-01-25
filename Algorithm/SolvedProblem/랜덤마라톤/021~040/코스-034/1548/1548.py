n = int(input())
data = sorted(map(int, input().split()))

if n > 2:
    result = 2
    for start in range(n - 2):
        end = start + 2
        while end < n and data[start] + data[start + 1] > data[end]:
            result = max(result, end - start + 1)
            end += 1
    print(result)
else:
    print(n)