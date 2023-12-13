n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dpMax = graph[0][:]
dpMin = graph[0][:]

for i in range(1,n):
    tempMin = dpMin[:]
    tempMax = dpMax[:]
    dpMin[0] = min(tempMin[0], tempMin[1]) + graph[i][0]
    dpMin[1] = min(tempMin) + graph[i][1]
    dpMin[2] = min(tempMin[1], tempMin[2]) + graph[i][2]

    dpMax[0] = max(tempMax[0], tempMax[1]) + graph[i][0]
    dpMax[1] = max(tempMax) + graph[i][1]
    dpMax[2] = max(tempMax[1], tempMax[2]) + graph[i][2]


print(max(dpMax), min(dpMin))