from collections import deque
import sys
input = sys.stdin.readline
r_dir = [-1, 0, 0, 1]
c_dir = [0, -1, 1, 0]


def bfs():
    global s_size, eat, cnt, is_eat, s_r, s_c
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((s_r, s_c, 0))
    candies = []
    canT = float('infinity')
    while q:
        row, col, t = q.popleft()
        if visited[row][col]:
            continue

        visited[row][col] = True

        for i in range(4):
            new_row = row + r_dir[i]
            new_col = col + c_dir[i]
            if 0 <= new_row < n and 0 <= new_col < n and not visited[new_row][new_col]:
                newVal = graph[new_row][new_col]
                if newVal == 0 or newVal == s_size:
                    q.append((new_row, new_col, t + 1))
                elif newVal < s_size:
                    if t + 1 <= canT:
                        canT = t + 1
                    else:
                        continue
                    candies.append((new_row, new_col))
    if candies:
        candies.sort(key=lambda x: (x[0], x[1]))
        new_row = candies[0][0]
        new_col = candies[0][1]
        eat += 1
        if eat == s_size:
            eat = 0
            s_size += 1
        graph[s_r][s_c] = 0
        graph[new_row][new_col] = 9
        s_r = new_row
        s_c = new_col
        cnt += canT
        return
    is_eat = False


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            s_r = i
            s_c = j

s_size = 2
eat = 0
cnt = 0

is_eat = True

while is_eat:
    bfs()
print(cnt)
