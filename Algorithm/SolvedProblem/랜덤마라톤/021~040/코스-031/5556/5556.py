N = int(input())
K = int(input())
tiles = [list(map(int, input().split())) for _ in range(K)]

for i, j in tiles:
    i = min(i, N + 1 - i)
    j = min(j, N + 1 - j)
    answer = (min(i, j) - 1) % 3 + 1
    print(answer)