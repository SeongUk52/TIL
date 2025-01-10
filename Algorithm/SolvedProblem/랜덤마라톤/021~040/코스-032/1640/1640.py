from collections import deque

# 입력 받기
n, m = map(int, input().split())
v = [0] * n
w = [0] * m

for i in range(n):
    s = input().strip()
    for j in range(m):
        if int(s[j]) % 2:
            v[i] ^= 1
            w[j] ^= 1

# 거리 배열 초기화
dist = [[-1] * (m + 1) for _ in range(n + 1)]

# 초기 값 설정
t1 = sum(v)
t2 = sum(w)
dist[t1][t2] = 0
queue = deque([(t1, t2)])

# BFS 탐색
while queue:
    x, y = queue.popleft()
    if x == 0 and y == 0:
        print(dist[x][y])
        exit()

    for nx, ny in [(x - 1, m - y), (x + 1, m - y), (n - x, y - 1), (n - x, y + 1)]:
        if 0 <= nx <= n and 0 <= ny <= m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

print(-1)