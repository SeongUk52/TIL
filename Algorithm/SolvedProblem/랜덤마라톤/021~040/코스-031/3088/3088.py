chk = [False] * 1000001

N = int(input())
cnt = 0

for _ in range(N):
    x, y, z = map(int, input().split())
    if not (chk[x] or chk[y] or chk[z]):
        cnt += 1
    chk[x] = chk[y] = chk[z] = True

print(cnt)