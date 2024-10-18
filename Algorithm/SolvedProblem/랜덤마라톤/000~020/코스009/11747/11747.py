n = int(input())
d = []
while len(d) < n:
    d += list(input().split())
d = "".join(d)
answer = 0
for i in range(n):
    ll = []
    for j in range(n - i):
        ll.append(int(d[j:j + i + 1]))
    while answer in ll:
        answer += 1
    if answer < 10 ** (i + 1):
        break

print(answer)
