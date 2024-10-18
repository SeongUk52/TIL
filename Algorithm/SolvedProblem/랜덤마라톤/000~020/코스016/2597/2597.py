l = int(input())
points = [sorted(list(map(int, input().split()))) for _ in range(3)]

for i in range(3):
    if points[i][0] == points[i][1]:
        continue
    mid = (points[i][0] + points[i][1]) / 2
    if mid < l - mid:
        for j in range(i + 1, 3):
            for k in range(2):
                if points[j][k] < mid:
                    points[j][k] = mid - points[j][k]
                else:
                    points[j][k] -= mid
            if points[j][0] > points[j][1]:
                temp = points[j][0]
                points[j][0] = points[j][1]
                points[j][1] = temp
        l = l - mid
    else:
        for j in range(i + 1, 3):
            for k in range(2):
                if mid < points[j][k]:
                    points[j][k] = mid - (points[j][k] - mid)
            if points[j][0] > points[j][1]:
                temp = points[j][0]
                points[j][0] = points[j][1]
                points[j][1] = temp
        l = mid

print("{:.1f}".format(l))
