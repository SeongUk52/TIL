arr1 = list(input())
arr2 = list(input())

dp = [[0 for _ in range(len(arr1) + 1)] for _ in range(len(arr2) + 1)]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            dp[j][i] = dp[j - 1][i - 1] + 1
maxi = 0
for i in dp:
    if max(i) > maxi:
        maxi = max(i)

print(maxi)