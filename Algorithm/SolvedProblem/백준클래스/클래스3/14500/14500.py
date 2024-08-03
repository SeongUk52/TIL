n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

maximum = 0


def dfs(x, y, tmp, cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
            continue
        visited[ny][nx] = True
        dfs(nx, ny, tmp + graph[ny][nx], cnt + 1)
        visited[ny][nx] = False


def fy(x, y):
    global maximum
    tmp = graph[y][x]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        arr.append(graph[ny][nx])
    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[y][x])
    elif length == 3:
        maximum = max(maximum, sum(arr) + graph[y][x])
    return


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, graph[i][j], 1)
        fy(j, i)
        visited[i][j] = False

print(maximum)
