import sys
input = sys.stdin.readline


h, n = map(int, input().split())

diff = abs(h - n) + 1

arr = [[0 for _ in range(diff)] for i in range(diff)]

for i in range(diff):
    arr[0][i] = 1


for i in range(1, diff):
    for j in range(i, diff):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

print(arr[-1][-1])
