import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 한도를 늘려줌

def dfs(start, depth):
    print(f"a{start + 1} ", end="")  # a1, a2... 형식으로 출력
    if depth == n * (n - 1) // 2:
        return

    for i in range(n):
        if graph[start][i] == 1 and cnt[i] < n - 2:
            cnt[start] += 1
            cnt[i] += 1
            graph[start][i] = 0
            graph[i][start] = 0
            dfs(i, depth + 1)


# 입력 처리 및 초기화
n = int(input())
graph = [[1 if i != j else 0 for j in range(n)] for i in range(n)]
cnt = [0] * n

# dfs 호출
dfs(0, 0)
print("a1")