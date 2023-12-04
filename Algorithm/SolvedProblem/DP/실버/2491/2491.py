n = int(input())
arr = list(map(int,input().split()))

dpInc = [1] * n
dpDec = [1] * n

for i in range(n - 1):
    if arr[i + 1] >= arr[i]:
        dpInc[i + 1] += dpInc[i]
    if arr[i] >= arr[i + 1]:
        dpDec[i + 1] += dpDec[i]

print(max(max(dpInc), max(dpDec)))