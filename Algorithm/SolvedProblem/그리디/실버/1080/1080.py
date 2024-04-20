def flip(mat, x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            mat[i][j] = (mat[i][j] + 1) % 2


n, m = map(int, input().split())
matA = [list(map(int, input())) for _ in range(n)]
matB = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n - 2):
    for j in range(m - 2):
        if matA[i][j] != matB[i][j]:
            flip(matA, i, j)
            cnt += 1

if matA == matB:
    print(cnt)
else:
    print(-1)
