import sys
import heapq
input = sys.stdin.readline

def dijkstra(graph,start):
    distance = {i:[float('infinity'),[]]for i in graph}
    distance[start] = [0,[start]]
    q = [(0,start)]

    while q:
        cdist,cvert = heapq.heappop(q)
        if cdist > distance[cvert][0]:
            continue
        for neight, weight in graph[cvert].items():
            dist = cdist + weight

            if dist <= distance[neight][0]:
                distance[neight][1] = distance[cvert][1][:]
                distance[neight][1].append(neight)
                distance[neight][0] = dist
                heapq.heappush(q,(dist,neight))


    return distance

n = int(input())
m = int(input())
graph = {i:{} for i in range(1,n+1)}

for i in range(m):
    a,b,c = map(int,input().split())
    if graph[a].get(b,None):
        if graph[a][b]<c:
            continue
    graph[a][b] = c
s,e = map(int,input().split())
dist = dijkstra(graph,s)
print(dist[e][0])
print(len(dist[e][1]))
for i in dist[e][1]:
    print(i, end=' ')