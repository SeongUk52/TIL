N, K = map(int, input().split())
num_list = [int(input()) for _ in range(N)]
point = 0
M = 0

for i in range(N):
    target = num_list[point]
    M += 1
    if target == K:
        print(M)
        break
    point = target
else:
    print(-1)
