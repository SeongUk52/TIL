n = int(input())
graph = []
for i in range(3):
    graph += map(int, input().split())
isCan = False
for i in range(0, graph[0] + 1):
    a = i
    d = graph[0] - a
    e = graph[5] - d
    b = graph[2] - e
    c = graph[1] - b
    f = graph[4] - c

    if a >= 0 and b >= 0 and c >= 0 and d >= 0 and e >= 0 and f >= 0:
        print(1)
        print(a, d)
        print(b, e)
        print(c, f)
        isCan = True
        break

if not isCan:
    print(0)
