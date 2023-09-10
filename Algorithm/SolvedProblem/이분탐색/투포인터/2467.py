import sys

sys.setrecursionlimit(1000000)


def tp(points, start, end, mini, n, result):
    newmin = points[start] + points[end]
    if abs(newmin) <= abs(mini[0]):
        mini = [newmin, points[start], points[end]]
        result[0] = mini[:]
    if newmin == 0:
        return
    if newmin > 0:
        if end - 1 <= start:
            return
        tp(points, start, end - 1, mini, n,result)
    if newmin < 0:
        if start + 1 >= end:
            return
        tp(points, start + 1, end, mini, n,result)


n = int(input())
points = list(map(int, input().split()))
mini = [float('infinity'), 0, 0]
result = [[]]
tp(points, 0, n - 1, mini, n , result)
print(result[0][1],result[0][2])
