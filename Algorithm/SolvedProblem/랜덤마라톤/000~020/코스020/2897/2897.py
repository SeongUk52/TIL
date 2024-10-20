r, c = map(int, input().split())
pl = [input() for _ in range(r)]
n = [0] * 5

for i in range(r - 1):
    for j in range(c - 1):
        if '#' not in (temp := pl[i][j:j+2] + pl[i+1][j:j+2]):
            n[temp.count('X')] += 1

print(*n, sep="\n")
