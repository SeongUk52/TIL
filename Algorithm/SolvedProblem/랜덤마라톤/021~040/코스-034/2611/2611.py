from collections import deque, defaultdict

def find_route(N, M, lines, connect):
    # 초기화
    maxi = [0] * (N + 1)
    route = [[] for _ in range(N + 1)]
    route[1] = [1]

    # 큐 생성 및 BFS
    q = deque([1])
    while q:
        x = q.popleft()
        for xx, cnt in lines[x]:
            if maxi[xx] < maxi[x] + cnt:
                maxi[xx] = maxi[x] + cnt
                route[xx] = route[x] + [xx]
            connect[xx] -= 1
            if connect[xx] == 0:
                q.append(xx)

    return maxi, route

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    N, M = int(data[0]), int(data[1])
    lines = defaultdict(list)
    connect = [0] * (N + 1)

    idx = 2
    for _ in range(M):
        x, y, k = map(int, data[idx:idx + 3])
        idx += 3
        lines[x].append((y, k))
        connect[y] += 1

    maxi, route = find_route(N, M, lines, connect)
    print(maxi[1])  # 최대 값 출력
    print(" ".join(map(str, route[1])))  # 경로 출력

if __name__ == "__main__":
    solve()