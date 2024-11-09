import sys

input = sys.stdin.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            dot1, dot2, dot3 = points[i], points[j], points[k]
            d1 = (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2
            d2 = (dot2[0] - dot3[0]) ** 2 + (dot2[1] - dot3[1]) ** 2
            d3 = (dot3[0] - dot1[0]) ** 2 + (dot3[1] - dot1[1]) ** 2
            if 2 * max(d1, d2, d3) == d1 + d2 + d3:
                cnt += 1
print(cnt)
