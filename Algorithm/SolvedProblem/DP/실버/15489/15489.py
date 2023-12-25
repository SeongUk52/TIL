arr = [[1] * (i + 1) for i in range(30)]

for i in range(2, 30):
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

result = 0

r, c, w = map(int, input().split())

for i in range(w):
    for j in range(i + 1):
        result += arr[r + i - 1][c + j - 1]

print(result)