dirX = [- 1, 0, 1, 0]
dixY = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while True:
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = 2

    if arr[r + 1][c] != 0 and arr[r][c + 1] != 0 and arr[r - 1][c] != 0 and arr[r][c - 1] != 0:
        if arr[r - dirX[d]][c - dixY[d]] != 1:
            r -= dirX[d]
            c -= dixY[d]
        else:
            break

    else:
        d = (4 + d - 1) % 4
        if arr[r + dirX[d]][c + dixY[d]] == 0:
            r += dirX[d]
            c += dixY[d]

print(cnt)
