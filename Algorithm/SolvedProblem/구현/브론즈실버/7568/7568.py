n = int(input())

ll = []

for _ in range(n):
    ll.append(list(map(int,input().split())))


rank = [1] * n

for i in range(n):
    for j in range(n):
        if ll[j][0] > ll[i][0] and ll[j][1] > ll[i][1]:
            rank[i] += 1

print(*rank)