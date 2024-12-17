from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(visited):
    global ans
    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nc < 0 or nc >= w + 2 or nr < 0 or nr >= h + 2 or miro[nr][nc] == '*' or visited[nr][nc]:
                continue
            if 'A' <= miro[nr][nc] <= 'Z':
                if chr(ord(miro[nr][nc]) + 32) not in key:
                    continue
            elif 'a' <= miro[nr][nc] <= 'z':
                if miro[nr][nc] not in key:
                    key[miro[nr][nc]] = True
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
            elif miro[nr][nc] == "$" and (nr, nc) not in visited_doc:
                ans += 1
                visited_doc.append((nr, nc))
            visited[nr][nc] = True
            queue.append([nr, nc])

T = int(input())
for _ in range(1, T + 1):
    h, w = map(int, input().split())
    miro = ['.' + input() + '.' for _ in range(h)]
    miro = ['.' * (w + 2)] + miro + ['.' * (w + 2)]
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    key = {}
    visited_doc = []

    for i in input():
        if i.isalpha():
            key[i] = True

    ans = 0
    bfs(visited)
    print(ans)