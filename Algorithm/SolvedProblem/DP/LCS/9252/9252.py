arr1 = list(input())
arr2 = list(input())

dp = [[0] * (len(arr2) + 1) for _ in range(len(arr1) + 1)]

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr2[j] == arr1[i]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(max(dp[-1]))
if max(dp[-1]) > 0:
    arr3 = []
    x = len(arr1)
    y = len(arr2)
    while x != 0 and y != 0:
        if dp[x - 1][y] == dp[x][y]:
            x -= 1
        elif dp[x][y - 1] == dp[x][y]:
            y -= 1
        else:
            x -= 1
            y -= 1
            arr3.append(arr1[x])

    arr3.reverse()
    for i in arr3:
        print(i, end="")