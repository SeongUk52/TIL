from sys import stdin

input = stdin.readline
DAY = 86400

c, h = map(int, input().split())
timeline = sorted(int(h) * 3600 + int(m) * 60 + int(s) for _ in range(c + h) for h, m, s in [input().split(':')])

prev, total_passing = -40, 0
for time in timeline:
    total_passing += min(40, time - prev)
    prev = time

print(DAY - total_passing)