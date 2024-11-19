from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        elif graph[i][j] == 'B':
            bx, by = i, j

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(x, y, dx, dy):
    steps = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        steps += 1
    return x, y, steps

def bfs(rx, ry, bx, by):
    q = deque([(rx, ry, bx, by, 0)])
    visited = set([(rx, ry, bx, by)])

    while q:
        rx, ry, bx, by, moves = q.popleft()
        if moves > 10:
            return -1
        if graph[rx][ry] == 'O':
            return moves

        for dx, dy in directions:
            nrx, nry, r_steps = move(rx, ry, dx, dy)
            nbx, nby, b_steps = move(bx, by, dx, dy)

            if graph[nbx][nby] == 'O':
                continue

            if (nrx, nry) == (nbx, nby):
                if r_steps > b_steps:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, moves + 1))

    return -1

print(bfs(rx, ry, bx, by))
