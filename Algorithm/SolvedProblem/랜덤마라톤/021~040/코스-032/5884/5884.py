n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

# 좌표별 고유 번호 부여
xx, yy = {}, {}
c1, c2 = 0, 0
cn1, cn2 = [0] * (n + 1), [0] * (n + 1)

for x, y in points:
    if x not in xx:
        c1 += 1
        xx[x] = c1
    cn1[xx[x]] += 1

for x, y in points:
    if y not in yy:
        c2 += 1
        yy[y] = c2
    cn2[yy[y]] += 1

if c1 <= 3 or c2 <= 3:
    print(1)
    exit()

x = [[] for _ in range(c1 + 1)]
y = [[] for _ in range(c2 + 1)]

for x_coord, y_coord in points:
    x[xx[x_coord]].append(yy[y_coord])
    y[yy[y_coord]].append(xx[x_coord])

for i in range(1, c1 + 1):
    cnt = sum(1 for nxt in x[i] if cn2[nxt] == 1)
    if c2 - cnt <= 2:
        print(1)
        exit()

for i in range(1, c2 + 1):
    cnt = sum(1 for nxt in y[i] if cn1[nxt] == 1)
    if c1 - cnt <= 2:
        print(1)
        exit()

print(0)