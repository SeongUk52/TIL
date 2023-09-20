import sys
input = sys.stdin.readline

def dfs(graph,row,col,r,c,max,visited,depth):
    visited[ord(graph[row][col])-65] = True
    if depth>max[0]:
        max[0] = depth
    keyRow = [1,-1,0,0]
    keyCol = [0,0,1,-1]
    for i in range(4):
        newRow = row + keyRow[i]
        newCol = col + keyCol[i]
        if (0 <= newRow < r and 0 <= newCol < c):
            n =graph[newRow][newCol]
            if visited[ord(n)-65] == False:
                dfs(graph,newRow,newCol,r,c,max,visited,depth+1)
                visited[ord(n)-65] = False
max = [0]
r,c = map(int,input().split())
graph = [list(input()) for i in range(r)]
visited = [False for _ in range(26)]
dfs(graph,0,0,r,c,max,visited,1)
print(max[0])