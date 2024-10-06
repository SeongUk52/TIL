import sys

R, C, T = map(int, sys.stdin.readline().split())
pan = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cur = []
cleaner = []


def spread():
    while cur:
        x, y, value = cur.pop()
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if (nx, ny) in cleaner:
                continue
            pan[nx][ny] += value // 5
            count += 1
        pan[x][y] -= (value // 5) * count


def clean(a, b):
    # 위에 회전
    x, y = a, 1
    index = 1
    temp = 0
    while True:
        nx = x + dx[index]
        ny = y + dy[index]
        if nx == R or ny == C or nx == -1 or ny == -1:
            index = (index - 1) % 4
            continue
        if x == a and y == 0:
            break
        pan[x][y], temp = temp, pan[x][y]  # swap
        x, y = nx, ny
    x, y = b, 1
    index = 1
    temp = 0
    while True:
        nx = x + dx[index]
        ny = y + dy[index]
        if nx == R or ny == C or nx == -1 or ny == -1:
            index = (index + 1) % 4
            continue
        if x == b and y == 0:
            break
        pan[x][y], temp = temp, pan[x][y]
        x, y = nx, ny


for i, line in enumerate(pan):
    for j, value in enumerate(line):
        if value > 0:
            cur.append((i, j, value))
        if value == -1:
            cleaner.append((i, j))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
a = cleaner[0][0]
b = cleaner[1][0]
for t in range(T):
    spread()
    clean(a, b)
    for i, line in enumerate(pan):
        for j, value in enumerate(line):
            if value > 0:
                cur.append((i, j, value))
print(sum(cur[i][2] for i in range(len(cur))))
