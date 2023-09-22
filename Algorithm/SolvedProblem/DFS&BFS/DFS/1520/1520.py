import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(row,col):
    if row == m-1 and col == n-1:
        return 1

    if cnt[row][col] != -1:
        return cnt[row][col]

    ways = 0
    for i in range(4):
        newRow = row + keyRow[i]
        newCol = col + keyCol[i]
        if 0 <= newRow <m and 0 <= newCol < n:
            if graph[row][col] > graph[newRow][newCol]:
                ways += dfs(newRow,newCol)
    cnt[row][col] = ways
    return cnt[row][col]

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
cnt = [[-1] * n for _ in range(m)]
result = [0]

keyRow = [1, -1, 0, 0]
keyCol = [0, 0, 1, -1]
print(dfs(0,0))
