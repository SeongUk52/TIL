n = int(input())
drug = dict()
for i in range(n):
    effect, name = map(int, input().split())
    drug[effect] = name
r = int(input())
for _ in range(r):
    l = list(map(int, input().split()))
    result = []
    for i in l[1:]:
        if not i in drug:
            result = ["YOU", "DIED"]
            break
        result.append(drug[i])
    print(*result)
