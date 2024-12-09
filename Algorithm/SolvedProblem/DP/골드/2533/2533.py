import sys

sys.setrecursionlimit(2000000)


def solve():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    tree = [[] for _ in range(N + 1)]
    for i in range(1, len(data) - 1, 2):
        u, v = int(data[i]), int(data[i + 1])
        tree[u].append(v)
        tree[v].append(u)

    # DP 테이블 초기화
    dp = [[0, 0] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    def dfs(node):
        visited[node] = True
        dp[node][0] = 0  # 노드가 얼리 아답터가 아님
        dp[node][1] = 1  # 노드가 얼리 아답터임

        for neighbor in tree[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                dp[node][0] += dp[neighbor][1]  # 자식은 얼리 아답터여야 함
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])  # 자식 자유 선택 가능

    dfs(1)
    # 루트에서 최소값 선택
    print(min(dp[1][0], dp[1][1]))


solve()