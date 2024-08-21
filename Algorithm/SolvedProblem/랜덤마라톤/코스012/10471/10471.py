w, p = map(int, input().split())
l = list(map(int, input().split()))
room = [False] * (w + 1)
room[w] = True
for i in range(p):
    room[l[i]] = True
    room[w - l[i]] = True
    for j in range(i + 1, p):
        room[l[j] - l[i]] = True
answer = [i for i in range(w + 1) if room[i]]

print(*answer)
