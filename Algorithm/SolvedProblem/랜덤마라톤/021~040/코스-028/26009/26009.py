from collections import deque

INF = int(1e9)
MoveY = [-1, 0, 1, 0]
MoveX = [0, -1, 0, 1]
MoveR = [-1, 1, 1, -1]
MoveC = [1, 1, -1, -1]

def bfs(n, m, grid):
    queue = deque([(0, 0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        y, x, steps = queue.popleft()

        if y == n - 1 and x == m - 1:
            return steps

        for i in range(4):
            ny, nx = y + MoveY[i], x + MoveX[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and grid[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((ny, nx, steps + 1))

    return -1

def main():
    n, m = map(int, input().split())
    k = int(input())
    grid = [[0] * m for _ in range(n)]

    for _ in range(k):
        r, c, d = map(int, input().split())
        r -= 1
        c -= 1
        grid[r][c] = 1
        nr, nc = r, c - d
        for i in range(4):
            for _ in range(d):
                nr += MoveR[i]
                nc += MoveC[i]
                if 0 <= nr < n and 0 <= nc < m:
                    grid[nr][nc] = 1

    result = bfs(n, m, grid)
    if result == -1:
        print("NO")
    else:
        print("YES")
        print(result)

main()