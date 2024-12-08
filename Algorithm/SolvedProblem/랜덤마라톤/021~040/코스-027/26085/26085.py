dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

cnt0 = sum(row.count(0) for row in arr)
cnt1 = sum(row.count(1) for row in arr)

if cnt0 % 2 == 1 or cnt1 % 2 == 1:
    print(-1)
    exit()

for i in range(r):
    for j in range(c):
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < r and 0 <= ny < c and arr[i][j] == arr[nx][ny]:
                print(1)
                exit()

print(-1)