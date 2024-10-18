n, k = map(int, input().split())
ll = list(map(int, input().split()))
for i in range(n - 1, 0, - 1):
    if k <= 0:
        break
    for j in range(i):
        if ll[j] > ll[j + 1]:
            temp = ll[j]
            ll[j] = ll[j + 1]
            ll[j + 1] = temp
            k -= 1
        if k <= 0:
            break
if k > 0:
    print(-1)
else:
    print(*ll)
