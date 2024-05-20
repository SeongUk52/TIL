from collections import deque
import sys
input = sys.stdin.readline

monkeyDR = [1, -1, 0, 0]
monkeyDC = [0, 0, 1, -1]
horseDR = [1, 2, 2, 1, -1, -2, -2, -1]
horseDC = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs():
    visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append((0, 0, 0, 0))

    while q:
        r, c, spent, result = q.popleft()
        if visited[r][c][spent]:
            continue
        visited[r][c][spent] = True
        if r == h - 1 and c == w - 1:
            print(result)
            return

        if spent < k:
            for i in range(8):
                newR = r + horseDR[i]
                newC = c + horseDC[i]

                if 0 <= newR < h and 0 <= newC < w:
                    if not visited[newR][newC][spent + 1] and graph[newR][newC] == 0:
                        q.append((newR, newC, spent + 1, result + 1))

        for i in range(4):
            newR = r + monkeyDR[i]
            newC = c + monkeyDC[i]

            if 0 <= newR < h and 0 <= newC < w:
                if not visited[newR][newC][spent] and graph[newR][newC] == 0:
                    q.append((newR, newC, spent, result + 1))

    print(-1)


k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
bfs()
