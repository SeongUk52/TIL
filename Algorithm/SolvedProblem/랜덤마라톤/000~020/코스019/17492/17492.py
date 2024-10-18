import sys

n = int(sys.stdin.readline().rstrip())
maps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

white = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            white += 1

row = [-1, 1, 0, 0, -1, -1, 1, 1]
col = [0, 0, -1, 1, -1, 1, -1, 1]
result = 0

def bt(nowWhite):
    global result
    if nowWhite == 1:
        result = 1
        return

    for y in range(n):
        for x in range(n):
            if maps[y][x] != 2:
                continue
            for d in range(8):
                ny = y + row[d]
                nx = x + col[d]
                nny = ny + row[d]
                nnx = nx + col[d]

                if 0 <= ny < n and 0 <= nx < n and 0 <= nny < n and 0 <= nnx < n:
                    if maps[ny][nx] == 2 and maps[nny][nnx] == 0:
                        maps[y][x] = 0
                        maps[ny][nx] = 0
                        maps[nny][nnx] = 2
                        bt(nowWhite - 1)
                        maps[y][x] = 2
                        maps[ny][nx] = 2
                        maps[nny][nnx] = 0

bt(white)

print("Possible" if result == 1 else "Impossible")
