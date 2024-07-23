n, m = map(int, input().split())
vec = [[]for _ in range(n)]
for _ in range(m):
    p = list(map(int, input().split()))
    for i in range(n):
        vec[i].append(p[i])
total = 0
ans = []
for i in range(n):
    vec[i].sort()
    ans.append(vec[i][int(m / 2)])
    for j in vec[i]:
        total += abs(j - ans[-1])

print(total)
print(*ans)
