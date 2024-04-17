def summary(arr):
    result = 0
    while len(arr) >= 2:
        a = arr.pop()
        b = arr.pop()
        if a * b > a:
            result += a * b
        else:
            arr.append(b)
            result += a
    if arr:
        result += arr.pop()
    return result


n = int(input())
arr = [int(input()) for _ in range(n)]
parr = []
marr = []
for i in arr:
    if i > 0:
        parr.append(i)
    else:
        marr.append(i)
parr.sort()
marr.sort(reverse=True)
result = 0
result += summary(parr)
result += summary(marr)
print(result)
