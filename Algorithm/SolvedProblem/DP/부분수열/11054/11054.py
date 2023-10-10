n = int(input())
a = list(map(int,input().split()))
dpi = [0] * n
dpd = [0] * n

for k in range(n):
    dpi[k] = 1
    for i in range(k):
        if a[i] < a[k]:
            dpi[k] = max(dpi[k], dpi[i] + 1)

for k in range(n - 1, -1, -1):
    dpd[k] = 1
    for i in range(n - 1, k - 1, -1):
        if a[i] < a[k]:
            dpd[k] = max(dpd[k], dpd[i] + 1)

maxi = 0
for i in range(n):
    suma = dpi[i] + dpd[i]
    if suma > maxi:
        maxi = suma

maxi -= 1
print(maxi)