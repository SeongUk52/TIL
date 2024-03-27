n, l = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

temp = arr[0]
cnt = 1

for i in arr:
    if i - temp > l - 1:
        cnt += 1
        temp = i

print(cnt)
