import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def solve(n, m, l, k, arr):
    answer = 0
    for i in range(k):
        for j in range(k):
            cnt = 0
            sx, sy = min(arr[i][0], arr[j][0]), min(arr[i][1], arr[j][1])
            for x, y in arr:
                if sx <= x <= sx + l and sy <= y <= sy + l:
                    cnt += 1
            answer = max(answer, cnt)
    return k - answer

n, m, l, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
print(solve(n, m, l, k, arr))