R, C = map(int, input().split())
Filter = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

cnt = sum(
    sorted(Filter[i][j] for i in range(r, r + 3) for j in range(c, c + 3))[4] >= T
    for r in range(R - 2) for c in range(C - 2)
)

print(cnt)