import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

n, m, x = map(int, input().split())
graph = {i : {} for i in range(n + 1)}
for i in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c

shortest_distances = dijkstra(graph, x)
for i in range(1,n+1):
    shortest_distances[i] += dijkstra(graph, i)[x]
shortest_distances[0] = 0
print(max(shortest_distances.values()))